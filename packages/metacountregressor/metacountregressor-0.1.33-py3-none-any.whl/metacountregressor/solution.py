"""
   Solution Logic
"""

import ast
import itertools
import math
#from bdb import GENERATOR_AND_COROUTINE_FLAGS
#from dis import dis
import os
#from pyexpat.errors import XML_ERROR_INCOMPLETE_PE
import random
import sys
import time
import warnings
from collections import Counter
from functools import wraps
#from tabnanny import verbose
#from telnetlib import XAUTH
from tempfile import TemporaryFile
import traceback
import latextable
import numpy as np
import pandas as pd
import psutil
import scipy.special as sc
#rom scipy.integrate import quad
import statsmodels.api as sm
from scipy.integrate import quad
from scipy.optimize import minimize
from scipy.stats import boxcox, gamma, lognorm, nbinom, norm, poisson, t
#import sklearn
from sklearn import preprocessing

from sklearn.metrics import mean_absolute_error as MAE
from sklearn.metrics import mean_squared_error as MSPE
from sklearn.model_selection import train_test_split
from statsmodels.tools.numdiff import approx_fprime, approx_hess
#from tabulate import tabulate
from texttable import Texttable

from ._device_cust import device as dev
#from optimparallel import minimize_parallel
#import pareto
from .pareto_file import Pareto, Solution

#import aesara
#import aesara.tensor as T


np.seterr(divide='ignore', invalid='ignore')
warnings.simplefilter("ignore")


# defube the computation boundary limits
min_comp_val = 1e-200
max_comp_val = 1e+300
log_lik_min = -1e+200
log_lik_max = 1e+200
log_lik_max = 0

# Setup Limits, and Batches for custom GPU code
EXP_UPPER_LIMIT = np.float64(np.log(np.finfo(np.float64).max) - 10.0)
def _unpack_tuple(x): return x if len(x) > 1 else x[0]


import base64
import hashlib


def make_hash_sha256(o):
    hasher = hashlib.sha256()
    hasher.update(repr(make_hashable(o)).encode())
    return base64.b64encode(hasher.digest()).decode()

def make_hashable(o):
    if isinstance(o, (tuple, list)):
        return tuple((make_hashable(e) for e in o))

    if isinstance(o, dict):
        return tuple(sorted((k,make_hashable(v)) for k,v in o.items()))

    if isinstance(o, (set, frozenset)):
        return tuple(sorted(make_hashable(e) for e in o))

    return o


def batches_idx(batch_size, n_samples):
    batch_size = n_samples if batch_size is None else min(
        n_samples, batch_size)
    n_batches = n_samples//batch_size + int(n_samples % batch_size != 0)

    return [(batch*batch_size, batch*batch_size + batch_size)
            for batch in range(n_batches)]


def measure_usage(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        process = psutil.Process()
        memory_info = process.memory_info()
        current_memory_usage_gb = memory_info.rss / 1_000_000_000

        print(f"Current memory usage: {current_memory_usage_gb:.2f} GB")

        initial_cpu = psutil.cpu_percent()
        initial_memory = psutil.virtual_memory().used

        result = func(*args, **kwargs)

        peak_cpu = psutil.cpu_percent() - initial_cpu
        peak_memory = (psutil.virtual_memory().used -
                       initial_memory) & 0xffffffff
        peak_memory_gb = peak_memory/1073741824
        print(f"Peak CPU usage for {func.__name__}: {peak_cpu}%")
        print(f"Peak memory usage for {func.__name__}: {peak_memory} bytes")
        print(f"Peak memory usage for {func.__name__}: {peak_memory_gb} gpu")
        return result
    return wrapper


#pylance: disable-reportUnboundVariable
class ObjectiveFunction(object):
    """
        this is the objective function to minimise MLE
    """

    def __init__(self, x_data, y_data, **kwargs):
        self.other_bic = False
        if self.other_bic:
            print('change this to false latter ')
        offset = None
        self.group_halton = None
        self.group_halton_test = None
        self.panels =1
        self.group_names = []
        self.Last_Sol = None
        self.fixed_fit = None
        self.rdm_fit = None
        self.rdm_cor_fit = None
        self.dist_fit = None
        self.zi_fit = None
        self.MAE = None
        self.best_obj_1 = 100000000
        self._obj_1 = 'bic'
        self._obj_2 = 'MAE'
        self.full_model = None
        self.GP_pararameter = 0
        self.is_multi = 0
        self.complexity_level = 6
        self._max_iterations_improvement = 150000
        self.generated_sln = set()
        self.ave_mae = 0
        #defualt paraamaters for hs
        self.agorithm ='hs'
        self._hms = 20
        self._hmcr = .5
        self._max_imp = 100000
        self._panels = .3
        self.is_multi = True
        
        
        self._max_characteristics = 40
        
        
        
        self.beta_dict = dict

        acceptable_keys_list = ['_par', '_max_imp', '_hmcr', 'steps',
                                'algorithm', '_random_seed', '_max_time',
                                'forcedvariables', '_obj_1', '_obj_2', '_par',
                                'Manuel_Estimate', 'test_percentage', 'is_multi',
                                'complexity_level', '_hms', '_mpai', 'group', '_max_characteristics']
        for k in kwargs.keys():
            if k in acceptable_keys_list:
                self.__setattr__(k, self.tryeval(kwargs[k]))

        if 'complexity_level' in kwargs:
            self.complexity_level = kwargs['complexity_level']
     
        if 'instance_number' in kwargs:
            self.instance_number = str(kwargs['instance_number'])
        else:
            self.instance_number = 0 #set an arbitrary instance number    
       
        if not hasattr(self, '_obj_1'):
            raise Exception

        
        if 'pvalue_penalty' in kwargs:
            self.pvalue_penalty = float(kwargs['pvalue_penalty'])
        else:

            self.pvalue_penalty = .5  # penaly to apply for each violation of pvalues
        self.pvalue_exceed = 0
        self._maximize = False  # do we maximize or minimize?
        #self._random_forest_identify_transformations(x_data, y_data)
        #data_names = self._random_forest_preprocess(x_data, y_data)
        x_data = sm.add_constant(x_data)
        self._input_data(x_data, y_data)
        if y_data.ndim == 1:
            y_data = pd.DataFrame(y_data)

        # split the data for testing
        if self._obj_1 == 'MAE' or self._obj_2 == "MAE" or self._obj_1 == 'MSE' or self._obj_2 == "MSE":
            if 'test_percentage' in kwargs:
                self.test_percentage = float(kwargs['test_percentage'])
                if self.test_percentage == 0:
                    self.is_multi = False
            
            else:
                    
                self.test_percentage = 0
                self.is_multi = False
            if 'panels' in kwargs:
                self.group_names = np.asarray(x_data[kwargs['group']].astype(
                    'category').cat._parent.dtype.categories)
            
                x_data[kwargs['group']] = x_data[kwargs['group']].astype(
                    'category').cat.codes
                self.complexity_level = 6
            # create test dataset
         

           
                try:
                    x_data[kwargs['panels']] = x_data[kwargs['panels']].rank(method='dense').astype(int)
                    x_data[kwargs['panels']] -= x_data[kwargs['panels']].min() - 1

                    N = len(np.unique(x_data[kwargs['panels']].values))
                    id_unique = np.unique(x_data[kwargs['panels']].values)
                   
                except KeyError:
                    N = len(np.unique(x_data[kwargs['panels']]))
                   
                training_size = int((1-self.test_percentage)*N)
                ids = np.random.choice(N, training_size, replace=False) 
                ids = id_unique[ids]
                #train_idx = [ii for ii, id_val in enumerate(df[id_key]) if id_val in ids]
                #test_idx = [ii for ii, id_val in enumerate(df[id_key]) if id_val not in ids]

                train_idx = [ii for ii, id_val in enumerate(x_data[kwargs['panels']]) if id_val in ids]
                test_idx = [ii for ii, id_val in enumerate(x_data[kwargs['panels']]) if id_val not in ids]

                df_train = x_data.loc[train_idx, :]
                df_test = x_data.loc[test_idx, :]
                y_train =y_data.loc[train_idx, :]
                y_test=y_data.loc[test_idx, :]

            else:
                N = len(x_data)
                training_size = int((1-self.test_percentage)*N)
                ids = np.random.choice(N, training_size, replace=False) 
                id_unique = np.array([i for i in range(N)])
                ids = id_unique[ids]
            
                train_idx = [ii for ii in range(len(id_unique)) if id_unique[ii] in ids]
                test_idx  = [ii for ii in range(len(id_unique)) if id_unique[ii] not in ids]

                

                df_train = x_data.loc[train_idx, :]
                df_test = x_data.loc[test_idx, :]
                y_train =y_data.loc[train_idx, :]
                y_test=y_data.loc[test_idx, :]
                
         

            #new_data_test = sm.add_constant(x_data)
            #self._input_data(new_data_test[data_names], y_data)
            #self._x_data, self._x_data_test, self._y_data, self.y_data_test = train_test_split(new_data_test[data_names], y_data, test_size = self.test_percentage, random_state=self.get_random_seed())
            #data_names = self._random_forest_preprocess()
   
            
            
        self._characteristics_names = list(self._x_data.columns)
        #self._characteristics_names = [x for x in self._characteristics_names if not 'ID' in x]
        print('to do, drop the id and panels')
        
        self._max_group_all_means = 1
        
        
        exclude_this_test = [4]

          
        if 'panels' in kwargs:
            self.panels = np.asarray(df_train[kwargs['panels']])
            self.panels_test = np.asarray(df_test[kwargs['panels']])
            self.ids = np.asarray(
               df_train[kwargs['panels']]) if kwargs['panels'] is not None else None
            self.ids_test = np.asarray(
               df_test[kwargs['panels']]) if kwargs['panels'] is not None else None
            groupll = np.asarray(df_train[kwargs['group']].astype(
                    'category').cat.codes)
            group_test = np.asarray(df_test[kwargs['group']].astype(
                    'category').cat.codes)
            X, Y, panel, group = self._arrange_long_format(
                df_train, y_train, self.ids, self.ids, groupll)
            self.group_halton = group.copy()
            
            self.group_dummies = pd.get_dummies(group)
            Xnew, Ynew, panel_info = self._balance_panels(X, Y,  panel)
            self.panel_info = panel_info
            self.N, self.P = panel_info.shape
            Xnew.drop(kwargs['panels'], axis=1, inplace=True)
            Xnew.drop(kwargs['group'], axis=1, inplace=True)
            K = Xnew.shape[1]
            self._characteristics_names = list(Xnew.columns)
            XX = Xnew.values.reshape(self.N, self.P, K).copy()
            self.group_dummies = self.group_dummies.values.reshape(self.N, self.P, -1)
            self.group_halton = self.group_halton.reshape(self.N, self.P)[:, 0]
            YY = Ynew.values.reshape(self.N, self.P, 1).copy()
            self._x_data = XX.copy()
            self._y_data = YY.copy()
           #Xalt, Yalt, group_info = self._balance_panels(X, Y,  group)
            X, Y, panel, group = self._arrange_long_format(df_test, y_test, self.ids_test, self.panels_test, group_test)
            if np.max(group) > 50:
                exclude_this_test = [4]
                self._max_group_all_means = 0
            else:
                exclude_this_test = []    
            self.group_halton_test = group.copy()
            X, Y, panel_info = self._balance_panels(X, Y,  panel)
            X.drop(kwargs['panels'], axis=1, inplace=True)
            X.drop(kwargs['group'], axis=1, inplace=True)
            self.N_test, self.P_test = panel_info.shape
           
            self.G  = 1
            self._Gnum = self.group_dummies.shape[2]
            self.group_dummies_test = pd.get_dummies(group)
            self.group_dummies_test = self.group_dummies_test.values.reshape(self.N_test, self.P_test, -1)
            K = X.shape[1]
            self.columns_names = X.columns
            X = X.values.reshape(self.N_test, self.P_test, K)
            self.group_halton_test = self.group_halton_test.reshape(self.N_test, self.P_test)[:, 0]
            Y = Y.values.reshape(self.N_test, self.P_test, 1)
            self._x_data_test = X.copy()
            self.y_data_test = Y.copy()
            
            self._samples,  self._panels, self._characteristics = self._x_data.shape

            # i dont think i need this X, Y, group_info = self._balance_panels(XX, YY,  group)
          
        else:
            self.G = None
            self._Gnum = 1
            self._max_group_all_means = 0
            self.ids = np.asarray(train_idx)
            self.ids_test = np.asarray(test_idx)
            groupll = None
            X, Y, panel, group = self._arrange_long_format(
                df_train, y_train, self.ids, self.ids, groupll)
            
            
          
            Xnew, Ynew, panel_info = self._balance_panels(X, Y,  panel)
            self.panel_info = panel_info
            self.N, self.P = panel_info.shape
           
            K = Xnew.shape[1]
            self._characteristics_names = list(Xnew.columns)
            XX = Xnew.values.reshape(self.N, self.P, K).copy()
            #self.group_dummies = self.group_dummies.values.reshape(self.N, self.P, -1)
            #self.group_halton = self.group_halton.reshape(self.N, self.P)[:, 0]
            YY = Ynew.values.reshape(self.N, self.P, 1).copy()
            self._x_data = XX.copy()
            self._y_data = YY.copy()
           #Xalt, Yalt, group_info = self._balance_panels(X, Y,  group)
            if self.is_multi:
                X, Y, panel, group = self._arrange_long_format(df_test, y_test, self.ids_test, self.ids_test, None)
                if np.max(group) > 50:
                    exclude_this_test = [4]
                else:
                    exclude_this_test = []    
                #self.group_halton_test = group.copy()
                X, Y, panel_info = self._balance_panels(X, Y,  panel)
                
                self.N_test, self.P_test = panel_info.shape
            
                
                #self.group_dummies_test = pd.get_dummies(group)
            # self.group_dummies_test = self.group_dummies_test.values.reshape(self.N_test, self.P_test, -1)
                K = X.shape[1]
                self.columns_names = X.columns
                X = X.values.reshape(self.N_test, self.P_test, K)
                #self.group_halton_test = self.group_halton_test.reshape(self.N_test, self.P_test)[:, 0]
                Y = Y.values.reshape(self.N_test, self.P_test, 1)
                self._x_data_test = X.copy()
                self.y_data_test = Y.copy()
            
            
            
            
            
            
            
            
            
            self._samples, self._panels, self._characteristics = self._x_data.shape
            
        # draws and pvalue
        
        if 'Offset' in self._characteristics_names:
            offset = True
        self.have_offset = offset
        if self.have_offset is not None:
            try:
                # offset for training data
                # define offset
                val_od = self.get_named_indices(['Offset'])
                self._offsets = self._x_data[:, : , val_od]
                #elf._offsets = self._x_data['Offset'].to_numpy()
                #self._offsets = np.reshape(self._offsets, (-1, 1))
                # drop the offset from the data
                self._x_data = np.delete(self._x_data, val_od, axis =2)
                self._characteristics_names = [x for x in self._characteristics_names if not 'Offset' in x]
                self._characteristics = len(self._characteristics_names)
                #self._x_data.drop(columns=['Offset'], inplace=True)

                # offset for testing data
                if self.is_multi:
                    
                    # define offset
                    self._offsets_test = self._x_data_test[:, : , val_od]
                    #self._offsets_test = self._x_data_test['Offset'].to_numpy()
                   # self._offsets_test = np.reshape(
                     #   self._offsets_test, (-1, 1))
                    # drop the offset from the data
                    self._x_data_test = np.delete(self._x_data_test, val_od, axis =2)
                    #self._x_data_test.drop(columns=['Offset'], inplace=True)
            except:
                # if no offset, set as 0
                self._offsets = np.zeros((self.N,self.P, 1))
                if self.is_multi:
                    self._offsets_test = np.zeros((self.N_test, self.P_test, 1))
        else:
            self._offsets = np.zeros((self.N,self.P, 1))
            if self.is_multi:
                self._offsets_test = np.zeros((self.N_test, self.P_test, 1))
        
        if self.is_multi:
            
            self.pareto_printer = Pareto(self._obj_1, self._obj_2, True)
            
            self._pareto_population = list()
        self.Ndraws = 200  # todo: change back
        self.draws1 = None
        self.initial_sig = 1  # pass the test of a single model
        self.pvalue_sig_value = .1
        self.observations = self._x_data.shape[0]
        self.batch_size = None
        # open the file in the write mode
        self.grab_transforms = 0
       
        
        
        
        if not isinstance(self._characteristics, int):
            raise Exception
        if not isinstance(self._x_data, pd.DataFrame):
            print('Estimating as Panel Data...')
        else:    
            self._characteristics_names = list(self._x_data.columns)
        # define the variables
        #self._transformations = ["no", "sqrt", "log", "exp", "fact", "arcsinh", 2, 3]
        self._transformations = ["no", "sqrt", "log", "arcsinh"]
        self._transformations = ["no", "sqrt", "log", 'arcsinh']

        self._distribution = ['triangular', 'uniform', 'normal', 'ln_normal', 'tn_normal', 'lindley']
        self._distribution = ['triangular', 'uniform', 'normal', 'ln_normal', 'tn_normal']
        #self._distribution = ['triangular', 'uniform', 'normal']
        if self.G is not None:
            
            self._distribution = ["trad| " + item for item in self._distribution
                                  ] + ["grpd| " + item for item in self._distribution]
            
            

        # output information
        self.convergence = None
        self.coeff_names = None
        self._interactions = None  # was 2
        self.coeff_ = None

        self.significant = 0
        # define the states of our explanaotory variables
        
        self._discrete_values = self.define_alphas(self.complexity_level, exclude_this_test, kwargs.get('Keep_Fit', []))
        self._discrete_values = self._discrete_values + \
            [[x for x in self._distribution]] * self._characteristics

        
        
        if 'model_types' in kwargs:
            model_types = kwargs['model_types']
        else:
            model_types = [[0,1]] # add 2 for Generalized Poisson    
        
        
        self._discrete_values = self._discrete_values + self.define_poissible_transforms(self._transformations) + model_types

        self._model_type_codes = ['p', 'nb',
                                  'gp', "pl", ["nb-theta", 'nb-dis']]
        self._variable = [True] * len(self._discrete_values)
        self._lower_bounds = [None] * \
            len(self._discrete_values)  # TODO have continus
        self._upper_bounds = [None] * \
            len(self._discrete_values)  # TODO have continous
        # model specs
        self.endog = None
        # solution parameters
        self._min_characteristics = 4
        
        
        self._max_hurdle = 4
    

        for_testing_purposes = 0
        if "Manual_Fit" in kwargs and  kwargs['Manual_Fit'] is not None:
            for_testing_purposes = 0
            print('off for now turn back on')
        if for_testing_purposes:
            self.initial_sig = 1  # pass the test of a single model
            self.pvalue_sig_value = 1
            
            #['added_random3','added_random4', 'added_random5']
            #['added_random4', 'added_random5']
            # embed the solution to how you want it
            a = self.modify_initial_fit(kwargs['Manual_Fit'])
            self.makeRegression(a)
            #self.make_regression_from_terms(['const', 'fixed1', 'fixed2', 'fixed3'], ['random3'], ['random1', 'random2'],
                                           # ['normal']*12, 0)
        find_constant = 0
        hard_code = 0
        if hard_code:
            manual_fit_spec = {
                        'fixed_terms': ['Constant', 'US', 'RSMS', 'MCV'],
                        'rdm_terms': ['RSHS:normal', 'AADT:normal', 'Curve50:normal'],
                        'rdm_cor_terms': [],
                        'grouped_terms': [],
                        'hetro_in_means': [],
                        'transformations': ['no', 'log', 'log', 'no', 'no','no', 'no'],
                        'dispersion': 1
                    }
            a = self.modify_initial_fit(manual_fit_spec)
            self.makeRegression(a)
            print(1)
        
        
        if find_constant:
            constant_values_total = [0, 0, 0]
            dispersion_values_total = [0, 0, 0]

            for _ in range(100):
                i = 0
                constant_values = []
                dispersion_values = []
                
                while i < 3:
                    manual_fit_spec = {
                        'fixed_terms': ['const'],
                        'rdm_terms': [],
                        'rdm_cor_terms': [],
                        'grouped_terms': [],
                        'hetro_in_means': [],
                        'transformations': ['no'],
                        'dispersion': i
                    }
                    a = self.modify_initial_fit(manual_fit_spec)
                    self.makeRegression(a)
                    constant_values.append(self.beta_dict['const'][0][1])
                    dispersion_values.append(self.beta_dict.get(self._model_type_codes[i], [[0,0],[0,0]])[0][1])
                    
                    i += 1

                # Add the values of this iteration to the total
                constant_values_total = [sum(x) for x in zip(constant_values_total, constant_values)]
                dispersion_values_total = [sum(x) for x in zip(dispersion_values_total, dispersion_values)]

            # Calculate the averages
            constant_values_avg = [x / 100 for x in constant_values_total]
            dispersion_values_avg = [x / 100 for x in dispersion_values_total]
           
        
        
        
            
        self.solution_analyst = None
        if 'Manuel_Estimate' in kwargs:
            self.make_regression_from_terms(['const', 'fixed1', 'fixed2', 'fixed3'],
                                            ['random4', 'random5'], ['random1', 'random2', 'random3'], ['normal']*19, 0)
       

    def _balance_panels(self, X, y, panels):  # ToDO re
        """Balance panels if necessary and produce a new version of X and y.

        If panels are already balanced, the same X and y are returned. This
        also returns panel_info, which keeps track of the panels that needed
        balancing.
        """
        
        _, K = X.shape
        _, p_obs = np.unique(panels, return_counts=True)
        p_obs = (p_obs).astype(int)
        N = len(p_obs)  # This is the new N after accounting for panels
        P = np.max(p_obs)  # panels length for all records
        if not np.all(p_obs[0] == p_obs):  # Balancing needed
            y = y.values.reshape(
                X.values.shape[0], 1) if y is not None else None

            Xbal, ybal = np.zeros((N*P, K)), np.zeros((N*P, 1))
            panel_info = np.zeros((N, P))
            cum_p = 0  # Cumulative sum of n_obs at every iteration
            for n, p in enumerate(p_obs):
                # Copy data from original to balanced version
                Xbal[n*P:n*P + p, :] = X.values[cum_p:cum_p + p, :]
                # TODO? predict mode in xlogit?
                ybal[n*P:n*P + p, :] = y[cum_p:cum_p +
                                         p, :] if y is not None else None

                panel_info[n, :p] = np.ones(p)
                cum_p += p
        else:  # No balancing needed
            Xbal, ybal = X, y
            panel_info = np.ones((N, P))
        ybal = ybal if y is not None else None

        return Xbal, ybal, panel_info

    def poisson_lognormal_pmf(self, x, mu, sigma):
        def integrand(lam):
            return np.exp(-lam) * (lam**x) / math.factorial(x) * lognorm.pdf(lam, sigma, scale=np.exp(mu))
        return np.nan_to_num(quad(integrand, 0, np.inf)[0], nan=0)

    def _random_forest_call_r(self):
        import rpy2.rinterface as rinterface
        import rpy2.robjects as robjects
        import rpy2.robjects as ro
        from rpy2.robjects import pandas2ri
        r = robjects.r
        r['source']('testML.R')
        pandas2ri.activate()
        RF_function_r = robjects.globalenv['RF_plot']
        RF_function_corr_r = robjects.globalenv['RF_plot_corr']
        r_df = ro.conversion.py2rpy(self._x_data)
        y_dy = ro.conversion.py2rpy(self._y_data)
        RF_function_r(r_df, y_dy)

        print('did this work')
        RF_function_corr_r(r_df, y_dy)

    def print_system_utilization(self):
        # Get CPU usage
        cpu_percent = psutil.cpu_percent()
        cpu_count = psutil.cpu_count()
        print(f"Current CPU Count: {cpu_count}%")
        print(f"Current CPU usage: {cpu_percent}%")

        # Get memory usage
        mem_info = psutil.virtual_memory()
        mem_percent = mem_info.percent
        mem_total = round(mem_info.total / (1024 * 1024), 2)  # Convert to MB
        mem_used = round(mem_info.used / (1024 * 1024), 2)  # Convert to MB
        mem_free = round(mem_info.available /
                         (1024 * 1024), 2)  # Convert to MB
        print(
            f"Current memory usage: {mem_percent}% ({mem_used} MB used / {mem_total} MB total)")

   
    
    def _arrange_long_format(self, X, y, ids, panels=None, groups=None):
        if ids is not None:
            pnl = panels if panels is not None else np.ones(len(ids))
            group = groups if groups is not None else ids
           
            cols = np.zeros(len(ids), dtype={'names': ['panels', 'groups', 'ids'],
                                             'formats': ['<f4', '<f4', '<f4']})
            cols['panels'], cols['groups'], cols['ids'] = pnl, group, ids
            sorted_idx = np.argsort(cols, order=['panels', 'groups', 'ids'])
            X, y = X.iloc[sorted_idx], y.iloc[sorted_idx]
            if pnl is not None:
                pnl = pnl[sorted_idx]
            if group is not None:
                group = group[sorted_idx]
                
        return X, y, pnl, group
        
        
        pandas_sort = 1
        if pandas_sort:
            if ids is not None:
                # if panels is not None:
                # panels = sorted_df['panels'].values
                #self.P_i = ((np.unique(panels, return_counts=True)[1])).astype(int)
                #self.P = np.max(self.P_i)
                #self.N = len(self.P_i)
                pnl = panels if panels is not None else np.ones(len(ids))
                df = X

                df['panels'], df['ids'] = pnl, ids
                new = 0
                if new:
                    cols = np.zeros(len(ids), dtype={'names': ['panels', 'ids'],
                                                     'formats': ['<f4', '<f4']})
                    cols['panels'], cols['ids'] = pnl, ids
                    sorted_idx = np.argsort(cols, order=['panels', 'ids'])
                    X, y = X[sorted_idx], y[sorted_idx]
                    if panels is not None:
                        panels = panels[sorted_idx]
                    return X, y, panels

                df = pd.concat([X.reset_index(drop=True),
                               y.reset_index(drop=True)], axis=1)
                sorted_df = df.sort_values(
                    ['panels', 'ids']).reset_index(drop=True)

                X, y, panels = sorted_df.iloc[:, :-
                                              3], sorted_df.iloc[:, -3:-2], sorted_df.iloc[:, -2]
                if panels is not None:
                    #panels = panels[sorted_idx]
                    P_i = (
                        (np.unique(panels, return_counts=True)[1])).astype(int)
                    P = np.max(P_i)
                    N = len(P_i)
                print(1)
                return X, y, panels

        if ids is not None:
            X = np.asarray(X)
            y = np.asarray(y)
            pnl = panels if panels is not None else np.ones(len(ids))

            cols = np.zeros(len(ids), dtype={'names': ['panels', 'ids'],
                                             'formats': ['<f4', '<f4']})
            cols['panels'], cols['ids'] = pnl, ids
            sorted_idx = np.argsort(cols, order=['panels', 'ids'])
            X, y = X[sorted_idx], y[sorted_idx]
            if panels is not None:
                panels = panels[sorted_idx]

        return X, y, panels

    def _random_forest_identify_transformations(self, x_data, y_data):
        # let's use the pprint module for readability
        import inspect
        from pprint import pprint

        from sklearn import preprocessing
        from sklearn.ensemble import RandomForestRegressor

        for i in x_data.columns:
            df_subset = x_data[[i]]
            a = np.random.random((1, 4))
            a = a*20
            print("Data = ", a)

# normalize the data attributes
            normalized = preprocessing.normalize(a)
            print("Normalized Data = ", normalized)

            df = self.apply_func(
                df_subset, i, [np.log, np.sqrt, preprocessing.normalize])
            print(df)
            rf = RandomForestRegressor(
                n_estimators=300, max_features='sqrt', max_depth=5, random_state=18).fit(df, y_data)

            names_in = np.array(df.columns)
            a, b = zip(*sorted(zip(rf.feature_importances_, names_in)))
            print(a)
            print(b)

    def _random_forest_preprocess(self, x_data, y_data):
        #import shap
        # let's use the pprint module for readability
        from pprint import pprint

        from sklearn.ensemble import RandomForestRegressor

# import inspect module
        import inspect
        rf = RandomForestRegressor(
            n_estimators=300, max_features='sqrt', max_depth=5, random_state=18).fit(x_data, y_data)
        pprint(inspect.getmembers(RandomForestRegressor))
        names_in = np.array(x_data.columns)

        print(rf.feature_importances_)
        a, b = zip(*sorted(zip(rf.feature_importances_, names_in)))
        b = list(b)
        number_of_elements = len(b)
        perc = (1/number_of_elements)
        print('the minimum perce', perc)
        if number_of_elements < 15:
            val_rand = 19999
        else:
            val_rand = 100
        features_saved = 0
        for i, j in enumerate(a):
            if j*val_rand < perc:
                print(b[i])
            else:
                features_saved += 1

        list1 = b
        list2 = ['const', 'offset']
        #index_list = [(i,string1.casefold().find(string2.casefold())) for i,string1 in enumerate(list1) for string2 in list2 if string1.casefold().find(string2.casefold()) != -1]
        index_list = [i for i, string1 in enumerate(
            list1) for string2 in list2 if string1.casefold().find(string2.casefold()) != -1]
        a = [list1[i] for i in index_list]
        print('saving', features_saved, 'out of ', len(b))
        b = b[-features_saved:]
        data_names = list(set(b+a))

        print(data_names)
        #from bs4 import BeautifulSoup
        #explainer = shap.TreeExplainer(rf)
        #shap_values = explainer.shap_values(self._x_data)
        # shap.initjs()
       # dis = shap.force_plot(explainer.expected_value, shap_values[0,:], self._x_data.iloc[0,:], matplotlib = True)

        return data_names

    def _input_data(self, x_data, y_data):
        # input the data to be used
        self._all_data = pd.concat([y_data, x_data], axis=1)
        self._y_data = y_data  # input predictors
        self._x_data = sm.add_constant(x_data)  # add_constant predictor

    def get_indexes_of_ints(self):
        result = []
        for i, sublst in enumerate(self._discrete_values):
            if all(isinstance(x, int) for x in sublst):
                result.append(i)
        return result

    def get_dispersion_paramaters(self, betas, dispersion):

        if dispersion == 0:
            return None, None
        elif dispersion == 2 or dispersion == 1:
            return betas[-1], None

        elif dispersion == 3:
            return None, betas[-1]
        elif dispersion == 4:
            return betas[-1], betas[-2]
        elif dispersion == 'poisson_lognormal':
            return betas[-1], None

    def reset_pvalue_conditions(self):
        self.initial_sig = .5  # pass the test of a single model
        self.pvalue_sig_value = .1

    def tryeval(self, val):
        try:
            val = ast.literal_eval(val)
        except ValueError:
            pass
        return val

    def partial_poisson_pmf(self, mu, y):

        par = np.exp(-mu)*(y-mu)*mu**(y-1)/sc.gamma(y+1)

        par = np.nan_to_num(par)
        return par

    def define_alphas(self, complexity_level=4, exclude =[], include = []):
        'complexity level'
        '''
        2 is feature selection,
        3 is random paramaters
        4 is correlated random paramaters
        '''
        set_alpha = []
        for col in self._characteristics_names:
            if col == 'const' or col == 'Constant' or col == 'constant':  # no random paramaters for const
                set_alpha = set_alpha + [[1]]
            elif col == 'Offset':
                set_alpha = set_alpha + [[1]]
            # elif (self._x_data[col].nunique() >= self._samples / 2):  # if twice the samples are not unique
            #    #set_alpha = set_alpha + [[x for x in range(2)]]
            elif col in include:
                set_alpha = set_alpha + [[x for x in range(1, complexity_level) if x not in exclude]]
            
            else:
                set_alpha = set_alpha + [[x for x in range(complexity_level) if x not in exclude]]
        return set_alpha

    def pvalue_asterix_add(self, pvalues):
        pvalue_ast = list()
        for i in range(len(pvalues)):
            signif = ""
            if float(pvalues[i]) < 0.001:
                signif = "***"
            elif float(pvalues[i]) < 0.01:
                signif = "**"
            elif float(pvalues[i]) < 0.05:
                signif = "*"
            elif float(pvalues[i]) < 0.1:
                signif = "."
            else:
                signif = ""
            pvalue_ast.append(pvalues[i]+signif)
        return pvalue_ast

    def round_with_padding(self, value, round_digits):
        return(format(np.round(value, round_digits), "."+str(round_digits)+"f"))

    def get_dispersion_name(self, dispersion=0):
        if dispersion == 0:
            return []

        elif dispersion == 4:
            return self._model_type_codes[dispersion]
        elif dispersion == 'poisson_lognormal':
            return ['sigma']

        else:

            return([self._model_type_codes[dispersion]])

    def naming_for_printing(self, betas=None, no_draws=0, dispersion=0, fixed_fit=None, rdm_fit=None, rdm_cor_fit=None, zi_fit=None, obj_1 = None, model_nature=None):
        self.name_deleter = []
        group_rpm = None
        group_dist = []
        group_fit_name = []
        if fixed_fit is None:
            fixed_fit = self.none_handler(self.fixed_fit)
        if rdm_fit is None:
            rdm_fit = self.none_handler(self.rdm_fit)
        if rdm_cor_fit is None:
            rdm_cor_fit = self.none_handler(self.rdm_cor_fit)
        if zi_fit is None:
            zi_fit = self.none_handler(self.zi_fit)
        dis_fit = [x for x in   self.none_handler(
                self.dist_fit)]  # check if dis fit is name
        hetro_long = []
        big_hetro = []
        if model_nature is not None:
            if 'grouped_rpm' in model_nature:
                
                
                group_fit = model_nature.get('grouped_rpm')
                group_fit_name = [f"{j} : {i}" for j in group_fit for i in self.group_names]

                
                group_dist = np.repeat(model_nature.get('dist_fit_grouped'), len(self.group_names)).tolist()
                rdm_fit = group_fit_name + rdm_fit 
                dis_fit = group_dist +dis_fit
            
            
            
                
            hetro  = []
            
            
            if 'hetro_fit' in model_nature:
                hetro_names_for = model_nature['hetro_hold'].values()
                big_hetro = [item for sublist in hetro_names_for for item in sublist]
                name_hetro = list(model_nature['hetro_hold'].keys())
                hetro_long= []
                
                for i in name_hetro:
                    hetro = [f"{j}: hetro" for j in  model_nature['hetro_hold'][i]]
                    hetro.append(f"{hetro[0]}:{i}:sd  hetro")
                    hetro_long = hetro_long +hetro
                    
                abct = []
                for i in model_nature['transfrom_hetro']:
                    abct = abct + i + ['']
            else:
                big_hetro = []
                hetro_long = []  

        dispersion_name = self.get_dispersion_name(dispersion)

        if no_draws == 0:
            self.full_model = 1
            fixednames = [x for x in self.none_handler(fixed_fit)]
            
            randvars = [x for x in self.none_handler(rdm_fit)]
            #randvars = group_fit_name + randvars
            chol_names = [x for x in self.none_handler(rdm_cor_fit)]

          
            dis_fit = group_dist +dis_fit
            rand_vars_dis = dis_fit[:len(randvars)]
            rand_vars_dist_cor = dis_fit[len(randvars):]

            chol = [" (Chol.) " + chol_names[i] + rand_vars_dist_cor[i] + "." +
                    chol_names[j] + rand_vars_dist_cor[j] for i
                    in range(len(chol_names)) for j in range(i+1)]
            br_w_names = []
            # three cases for corr. varnames: no corr, corr list, corr Bool (All)
            br_w_names = [randvars[i] + " (Std. Dev.) " + rand_vars_dis[i]
                          for i in range(len(randvars))]
            #br_w_names = np.char.add(randvars, "sd.")
            #br_w_names = np.char.add(br_w_names, rand_vars_dis)
       # br_w_names = br_w_names.tolist()
            zi_names = [x for x in self.none_handler(zi_fit)]

            names = fixednames+randvars+chol_names + \
                br_w_names+chol + zi_names+hetro_long+dispersion_name
            self.name_deleter = fixednames + randvars + chol_names + randvars + [chol_names[i] for i
                                                                                 in range(len(chol_names)) for j in range(i+1)] + zi_names+dispersion_name  # TODO does this break
            name_delete_2 = fixednames + randvars + chol_names + randvars + [chol_names[i] + "/" +
                                                                             chol_names[j] for i
                                                                             in range(len(chol_names)) for j in range(i+1)] + zi_names+dispersion_name
            index_dict = {}
            for i, name in enumerate(name_delete_2):
                split_names = name.split('/')
                for split_name in split_names:
                    if split_name not in index_dict:
                        index_dict[split_name] = [(i, betas[i])]
                    else:
                        index_dict[split_name].append((i, betas[i]))
            self.beta_dict = index_dict

            names = np.array(names)  # TODO check order
            self.print_transform = self.transform_id_names + \
                ['']*(len(names)-len(self.transform_id_names) - len(hetro_long)-1)+ abct +[''] #this was negative 1
            self.coeff_names = names
        else:
            self.full_model = 0
            if len(self.none_handler(rdm_fit)+self.none_handler(fixed_fit)) == 0:
                self.full_model = 1
            fixednames = [x for x in self.none_handler(fixed_fit)]
            randvars = [x for x in self.none_handler(rdm_fit)]
            chol_names = [x for x in self.none_handler(rdm_cor_fit)]
            
            zi_names = [x for x in self.none_handler(zi_fit)]
            
            names = fixednames+randvars+chol_names + zi_names+big_hetro+dispersion_name

            names = np.array(names)  # TODO check order
            self.print_transform = self.transform_id_names + \
                ['']*(len(names)-len(self.transform_id_names))
            self.coeff_names = names

        if betas is not None:
            try:
                if len(betas) != len(names):
                    print('no draws is', no_draws)
                    print('fix_theano')
            except Exception as e:
                print(e)

    def summary_alternative(self, long_print=0, model=0, solution=None):
        fmt = "{:19} {:13} {:13.10f} {:13.10f}{:13.10f} {:13.3g} {:3}"
        coeff_name_str_length = 19

        if self.coeff_ is None:
            print('The current model has not been estimated yet')
            return
        if self.coeff_names is None:
            raise Exception

        if self.pvalues is None:
            raise Exception

        if isinstance(self.pvalues, str):
            raise Exception

        if not isinstance(self.pvalues, np.ndarray):
            raise Exception

        for i in range(len(self.coeff_)):
            signif = ""
           
            if self.pvalues[i] < 0.01:
                signif = "***"
            elif self.pvalues[i] < 0.05:
                signif = "**"
            elif self.pvalues[i] < 0.1:
                signif = "*"
            print(fmt.format(self.coeff_names[i][:coeff_name_str_length], self.print_transform[i], self.coeff_[i],
                             self.stderr[i], self.zvalues[i], self.pvalues[i],
                             signif
                             ))

        if not self.convergence:
            print("-" * 50)
            print("WARNING: Convergence was not reached during estimation. "
                  "The given estimates may not be reliable")
        if self.convergance is not None:
            print("-" * 85)

            print('Log-Likelihood: ', self.log_lik)
            print("-" * 85)
            self.pvalues = [self.round_with_padding(
                x, 2) for x in self.pvalues]
            signif_list = self.pvalue_asterix_add(self.pvalues)
            if model ==1:
                
                self.coeff_[-1] = np.abs(self.coeff_[-1])
                
            self.coeff_ = [self.round_with_padding(x, 2) for x in self.coeff_]
           
            self.stderr = [self.round_with_padding(x, 2) for x in self.stderr]
            self.zvalues = [self.round_with_padding(
                x, 2) for x in self.zvalues]
         
            table = Texttable()

            if long_print:
                latex_dict = {
                    'Effect': self.coeff_names,
                    'tau': self.print_transform,
                    'Coeff': self.coeff_,
                    'Std. Err': self.stderr,
                    'z-values': self.zvalues,
                    'Prob |z|>Z': signif_list
                }
                df = pd.DataFrame.from_dict(latex_dict)
                table.set_cols_align(["l"]+["l"]+["c"]*3+["l"])
                table.set_cols_dtype(['t',
                                      't',
                                      't',
                                      't',
                                      't', 't'])
            else:
               
                if model ==1 or model == 2:
                    self.coeff_[-1] = np.abs(self.coeff_[-1])
                latex_dict = {
                    'Effect': self.coeff_names,
                    'Transformation': self.print_transform,
                    'Coefficient': self.coeff_,
                    'Prob |z|>Z': signif_list
                }
                
                df = pd.DataFrame.from_dict(latex_dict)
                table.set_cols_align(["l"]+["l"]+["c"]+["l"])
                table.set_cols_dtype(['t',
                                      't',
                                      't', 't'])

            rows = df.to_numpy(dtype=str)
            table.header(df.columns)
            table.add_rows(rows, header=False)

            print(table.draw())
            if model is not None:
                caption_parts = []
                if self.algorithm is not None:
                        caption_parts.append(f"{self._model_type_codes[model]} model found through the {self.algorithm} algorithm.")

                if self.bic is not None:
                    caption_parts.append(f"BIC: {self.round_with_padding(self.bic, 2)}")

                if self.log_lik is not None:
                    caption_parts.append(f"Log-Likelihood: {self.round_with_padding(self.log_lik, 2)}")

                if self.MAE is not None:
                    caption_parts.append(f"MSPE: {self.round_with_padding(self.MAE, 2)}")

                caption = " ".join(caption_parts)
                print(latextable.draw_latex(table, caption=caption, caption_above = True))
                if solution is None:
                    file_name = self.instance_number + "/sln" + \
                        "_with_BIC_"+str(self.bic)+".tex"
                else:
                    file_name = self.instance_number + "/sln" + \
                        str(solution['sol_num']) + \
                        "_with_BIC_"+str(self.bic)+".tex"
                self.save_to_file(latextable.draw_latex(
                    table, caption=caption), file_name)
                
                
                #print('change this')
                #df = pd.read_csv("artificial_mixed_corr_2023_MOOF.csv")
  
                # updating the column value/data
               # df['Y'] = np.mean(self.lam, axis = (1,2))
                
                # writing into the file
               # df.to_csv("artificial_mixed_corr_2023_MOOF.csv", index=False)
            
    def summary(self, model=None, algorithm=None, transform_list=None, long_print=0, solution=None):
        """
                Prints in console the coefficients and additional estimation outputs
                """
        try:

            self.grab_transforms = 1
            if self.coeff_ is None:
                print('The current model has not been estimated yet')
                return
            if not self.convergence:
                print("-" * 50)
                print("WARNING: Convergence was not reached during estimation. "
                      "The given estimates may not be reliable")
            if self.convergance is not None:
                print("-" * 85)
                print('BIC: ', self.bic)
                if solution is not None:
                    if solution['bic'] != self.bic:
                        raise Exception
                print("-" * 85)
                print('Log-Likelihood: ', self.log_lik)
                print("-" * 85)
                self.pvalues = [self.round_with_padding(
                    x, 4) for x in self.none_handler(self.pvalues)]
                signif_list = self.pvalue_asterix_add(self.pvalues)
                self.coeff_ = [self.round_with_padding(
                    x, 2) for x in self.coeff_]
                self.stderr = [self.round_with_padding(
                    x, 2) for x in self.stderr]
                self.zvalues = [self.round_with_padding(
                    x, 2) for x in self.zvalues]
                latex_dict = dict()
                table = Texttable()
                if transform_list is not None:
                    if long_print:
                        latex_dict['Effect'] = self.coeff_names
                        latex_dict['Transformation'] = transform_list
                        latex_dict['Coefficient'] = self.coeff_
                        latex_dict['Standard Error'] = self.stderr
                        latex_dict['z-values'] = self.zvalues
                        latex_dict['Prob |z|>Z'] = signif_list
                        df = pd.DataFrame.from_dict(latex_dict)
                        table.set_cols_align(["l"]+["l"]+["c"]*3+["l"])
                        table.set_cols_dtype(['t',
                                              't',
                                              't',
                                              't',
                                              't', 't'])
                    else:
                        latex_dict['Effect'] = self.coeff_names
                        latex_dict['Transformation'] = transform_list
                        latex_dict['Coefficient'] = self.coeff_
                        latex_dict['Prob |z|>Z'] = signif_list
                        df = pd.DataFrame.from_dict(latex_dict)
                        table.set_cols_align(["l"]+["l"]+["c"]+["l"])
                        table.set_cols_dtype(['t',
                                              't',
                                              't', 't'])

                else:
                    if long_print:
                        latex_dict['Effect'] = self.coeff_names
                        latex_dict['Coefficient'] = self.coeff_
                        latex_dict['Standard Error'] = self.stderr
                        latex_dict['z-values'] = self.zvalues
                        latex_dict['Prob |z| >Z'] = signif_list
                        df = pd.DataFrame.from_dict(latex_dict)
                        table.set_cols_align(["l"]+["c"]*3+["l"])
                        table.set_cols_dtype(['t',
                                              't',
                                              't',
                                              't',
                                              't'])
                    else:
                        latex_dict['Variable'] = self.coeff_names
                        latex_dict['Coefficient'] = self.coeff_
                        latex_dict['Prob |z| >Z'] = signif_list
                        df = pd.DataFrame.from_dict(latex_dict)
                        table.set_cols_align(["l"]+["c"]+["l"])
                        table.set_cols_dtype(['t',
                                              't',
                                              't'])

                rows = df.to_numpy(dtype=str)
                table.header(df.columns)
                table.add_rows(rows, header=False)

                #print(table.draw())
                if model is not None:
                    if model == 0:
                        caption = "Poisson model found through the " + \
                            str(algorithm) + " algorithm. BIC: " + \
                            str(self.bic) + " Loglikihood: " + \
                            str(self.log_lik)
                    elif model == 1:
                        caption = "Negative Binomial model found through the " + \
                            str(algorithm) + " algorithm" + str(self.bic) + \
                            " Loglikihood: " + str(self.log_lik)
                    elif model == 2:
                        caption = "Generalised Poisson model found through the " + \
                            str(algorithm) + " algorithm" + str(self.bic) + \
                            " Loglikihood: " + str(self.log_lik)
                    elif model == 3:
                        caption = "Conway-Maxwell Poisson model found through the " + \
                            str(algorithm) + " algorithm" + str(self.bic) + \
                            " Loglikihood: " + str(self.log_lik)
                    else:
                        raise Exception
                else:
                    caption = "Caption Name Error"
                print(latextable.draw_latex(table, caption=caption))
                if solution is None:
                    file_name = "sln" + "_with_BIC_"+str(self.bic)+".tex"
                else:
                    file_name = "sln" + \
                        str(solution['sol_num']) + \
                        "_with_BIC_"+str(self.bic)+".tex"
                self.save_to_file(latextable.draw_latex(
                    table, caption=caption), file_name)
        except Exception as e:
            print(e)

    def save_to_file(self, content, filename):
        with open(filename, 'w') as file:
            file.write(content)

    def define_poissible_transforms(self, transforms) -> list:
        transform_set = []
        if not isinstance(self._x_data, pd.DataFrame):
            x_data = self._x_data.reshape(self.N*self.P, -1).copy()
            x_data = pd.DataFrame(x_data)
        else:
            x_data = self._x_data.copy()
        for col in x_data:

            if all(x_data[col] <= 5):
                new_transform = [['no']]
                transform_set = transform_set + new_transform
            elif col == "Offset":
                new_transform = [['no']]
                transform_set = transform_set + new_transform
            else:
                new_transform = transforms.copy()
                if (x_data[col] > 0).all() and (x_data[col] >= 100000).any():
                    unwanted = {'no', 2, 3, 'exp', 'fact'}
                    new_transform = [
                        ele for ele in new_transform if ele not in unwanted]
                if (x_data[col] <= 0).any():
                    unwanted = {'log', 'sqrt', 'fact', 'boxcox'}
                    new_transform = [
                        ele for ele in new_transform if ele not in unwanted]
                if (abs(x_data[col]) >= 120).any():
                    unwanted = {2, 3, 'exp', 'fact'}
                    new_transform = [
                        ele for ele in new_transform if ele not in unwanted]
                if (abs(x_data[col]) >= 25).any():
                    unwanted = {3, 'exp', 'fact'}
                    new_transform = [
                        ele for ele in new_transform if ele not in unwanted]
                if (abs(x_data[col]) >= 9).any():
                    unwanted = {3, 'exp', 'fact'}
                    new_transform = [
                        ele for ele in new_transform if ele not in unwanted]
                if (abs(x_data[col]) >= 7).any():
                    unwanted = {'fact'}
                    new_transform = [
                        ele for ele in new_transform if ele not in unwanted]

                transform_set = transform_set + [new_transform]
        
        return transform_set

    def validation(self, betas, y, X, Xr=None, dispersion=0, rdm_cor_fit=None, zi_list=None,  exog_infl=None, model_nature = None, halton =1):
        'validation if mu needs to be calculated'
        if X is None:
            print('should not be possible')
            
        draws_grouped = None
        XG = None
        draws=None
        if model_nature is not None:
            if "XGtest" in model_nature:
                XG = model_nature.get('XGtest')
                n_r, p_r, kgr = XG.shape
                if halton:
                    draws_grouped = self.prepare_halton(kgr, n_r, self.Ndraws, np.repeat(model_nature.get('dist_fit_grouped'), len(self.group_names)))
                else:
                   
                    X_slice_before = X[:, :, :len(self.fixed_fit)]
                    X_slice_after =  X[:, :, len(self.fixed_fit):]
                    X = np.concatenate((X_slice_before, XG, X_slice_after), axis = 2)
                   
                    
                    #X = np.concatenate((X, XG), axis=2)
        
        if Xr is None and XG is None:
            draws = None
            if dispersion != 0:
                param_number = X.shape[2] + 1
            else:
                param_number = X.shape[2]
        
        if Xr is not None and Xr.shape[2] != 0:
            
            nr, pr, kr = Xr.shape
            
            param_number = self.get_param_num(dispersion)

            if param_number != len(betas):
                print('raise efffff edit this xceptions')

            if len(self.none_handler(self.dist_fit)) != kr:

                raise Exception('Look into dist fi')
            draws = self.prepare_halton(
                kr, nr, self.Ndraws, self.dist_fit, long=False, slice_this_way=self.group_halton_test)

        eVy = self._loglik_gradient(betas, X, y, draws, X, Xr, None, False, False, dispersion=dispersion,
                                    test_set=True, return_EV=True, corr_list=rdm_cor_fit, zi_list=zi_list, exog_infl=exog_infl, draws_grouped=draws_grouped, Xgroup=XG, model_nature=model_nature)
        eVy = dev.to_cpu(eVy)
        if len(eVy) != len(X):
            raise Exception
        if np.size(y) != np.size(eVy):
            y = np.tile(y, self.Ndraws).ravel()
            eVy = eVy.ravel()
        eVy = np.nan_to_num(eVy, nan=100000, posinf=100000)
        eVy = np.clip(eVy, None, 1000)
        mae = np.nan_to_num(MAE(np.squeeze(y), np.squeeze(eVy)), nan=100000, posinf=100000)
        mspe = np.nan_to_num(MSPE(np.squeeze(y), np.squeeze(eVy)), nan=100000, posinf=100000)
        
        return mspe

    def get_solution_vector(self, fixed_vars, random_vars, random_var_cor, distribution_vars, dispersion=None):
        alpha, alpha_rdm, alpha_rdm_cor = self.modify(
            fixed_vars, random_vars, random_var_cor)  # TODO handle distrubution

        distributions = alpha_rdm.copy()
        transformations = ['no']*len(alpha)  # todo add transformations
        cnt = 0
        joined_alpha = np.add(alpha_rdm, alpha_rdm_cor)
        for i, x in enumerate(joined_alpha):
            if x:
                distributions[i] = distribution_vars[cnt]
                cnt += 1
            else:
                distributions[i] = 'normal'
        dispersion2 = [dispersion]
        vector = alpha+distributions+transformations+dispersion2
        vector = self.modify_vector(vector, alpha, alpha_rdm, alpha_rdm_cor)

        return vector

    def reconstruct_vector(self, data_dict):
        '''Reconstructs the original input vector from a dictionary of data.'''

        # Get all the "alpha" components and reconstruct the first part of the vector
        alpha_parts = [data_dict[key] for key in ['alpha', 'alpha_rdm', 'alpha_cor_rdm', 'alpha_grouped', 'alpha_hetro']]
        first_part = [sum(x * (idx+1) for idx, x in enumerate(parts)) for parts in zip(*alpha_parts)]
        
        # Concatenate the first part with the 'distributions' and 'transformations' lists
        vector = first_part + data_dict['distributions'] + data_dict['transformations']
        
        # Append the 'dispersion' value
        vector.append(data_dict['dispersion'])
        
        return vector
    
    
    
    def get_distinct_model_parts(self, vector):
        '''gets the parts of the modal we are searching for
        for elements in vector:
        1: variables included
        2: radnom paramaters included
        3: correlated random paramaters
        4: grouped_random_paramaters
        5: herogeneoty_in _means


        a: how to transofrm the orignal data
        b: grab dispersion '''

        # todo: better way
        alpha = [0 if x != 1 else 1 for x in vector[:self._characteristics]]
        alpha_rdm = [
            0 if x != 2 else 1 for x in vector[:self._characteristics]]
        distributions = vector[self._characteristics:self._characteristics * 2]
        transformations = vector[self._characteristics *
                                 2:self._characteristics * 3]
       
        
        dispersion = vector[self._characteristics*3]
        if len(alpha_rdm) != len(distributions):
            raise Exception('error straight away')

        alpha_cor_rdm = [
            0 if x != 3 else 1 for x in vector[:self._characteristics]]
        # todo grab dictionary this is getting too combersome
        alpha_grouped= [
            0 if x != 4 else 1 for x in vector[:self._characteristics]]
        
        alpha_hetro= [
            0 if x != 5 else 1 for x in vector[:self._characteristics]]
        
        return {
        'alpha': alpha,
        'alpha_rdm': alpha_rdm,
        'alpha_cor_rdm': alpha_cor_rdm,
        'alpha_grouped': alpha_grouped,
        'alpha_hetro': alpha_hetro,
        'distributions': distributions,
        'transformations': transformations,
    
        'dispersion': dispersion
    }

    # TODO implement the interactions

    def generate_list_of_interactions(self, characteristics, combinations=2):
        # todo: add more interactions through combinations
        'generate a list of interactions to select from'
        list_of_interactions = list()
        for i, j in enumerate(self._characteristics_names):
            for k, l in enumerate(self._characteristics_names):
                if k > i:
                    list_of_interactions.append(str(j) + ":" + str(l))
        list_of_interactions.append(0)
        return list_of_interactions

    def get_characteristic_columns(self, vector):
        print('if not called delete this')
        characteristic_columns = list()
        j = 0
        for i in vector:
            if i == 0:
                characteristic_columns.append(j)
                j += 1
        # TODO check if i broke this
        char_data = self._x_data.drop(
            self._x_data[characteristic_columns].columns, axis=1)
        return char_data

    def sum_the_vector(self, vector):
        only_ints = [x if isinstance(x, int) else 0 for x in vector]
        return sum(only_ints)

    def repair(self, vector, reduce_to_this = 10000):  # todo get the number of parameters
        'Method to repair the model so that the number of paramaters is held within the constraint'
        b = 0
        new_j = 0
        # extract explanatory vector
        prmVect = vector[:self._characteristics]
        


        # count the number of occurrences of the integer 4
        count_4 = prmVect.count(4)
      
        # if the count is greater than 1, randomly select all but one 4
        if count_4 >  self._max_group_all_means:
            for i in range(count_4 -  self._max_group_all_means):
                # randomly select an index of a 4 in the list
                idx = random.choice([j for j, x in enumerate(prmVect) if x == 4])
                
                # randomly change the 4 to either 3 or 2
                prmVect[idx] = random.choice([2, 3, int(np.min((5, self.complexity_level-1))), 1, 0, 2, 3, int(np.min((5, self.complexity_level-1)))])

        count_3 = prmVect.count(3)

        # if the count is greater than 1, randomly select all but one 4
        if count_3 >  5:
            for i in range(count_3 -  5):
                # randomly select an index of a 4 in the list
                idx = random.choice([j for j, x in enumerate(prmVect) if x == 3])
                
                # randomly change the 4 to either 3 or 2
                prmVect[idx] = random.choice([2, 0, int(np.min((5, self.complexity_level-1))), 1, 0, 2, 0, int(np.min((5, self.complexity_level-1)))])
        
        vector[:len(prmVect)] = prmVect.copy()

      
        subVect_all = vector[:-1]  # all but dispersion
        
        idx_elem = list(range(len(subVect_all)))
        only_ints_vals = [x for x in subVect_all if isinstance(x, (int, float))]
        only_ints = [x for x, z in zip(
            idx_elem, subVect_all) if isinstance(z, (float, int))]

         # number of paramaters in the model #TODO get the last value if 2

        # sum of included variables plus dispersion
       
        b = self.get_param_num(dispersion=vector[-1])
        #b = sum(prmVect) + self.is_dispersion(vector[-1])
        max_loops = 100  # Maximum number of loops
        counter = 0  # Counter variable to keep track of the number of loops
        if any(isinstance(num, int) and num < 0 for num in vector):
            raise Exception('fhfhfhf')
        
        while b > self._max_characteristics and counter < max_loops or b > reduce_to_this:
            

            get_rdm_i = random.choices(only_ints, weights=only_ints_vals)[0]
            
            
            if vector[get_rdm_i] != 0:

                if (self.get_num_discrete_values(get_rdm_i) - 1) == 0:
                    # TODO: must be a better way to avoid selecting this
                    print('ignore replacemenet')
                
                
                else:
                    if vector[get_rdm_i] == 4:
                        vector[get_rdm_i] = 0
                        only_ints_vals[get_rdm_i] = 0
                        b -= self._Gnum +1
                        
                        
                    
                    
                    if vector[get_rdm_i] == 5:
                        
                        vector[get_rdm_i] = 0
                        only_ints_vals[get_rdm_i] = 0
                        b-=1
                    elif vector[get_rdm_i] != 0:
                        vector[get_rdm_i] -= 1
                        only_ints_vals[get_rdm_i] -=1
                            
                    if vector.count(5) ==1:
                        idx = vector.index(5)
                        vector[idx] =0
                        only_ints_vals[idx] = 0
                        b -=1

                    b -= 1

                #b -= 1
            counter +=1    
            
        
        counter = 0
        if any(isinstance(num, int) and num < 0 for num in vector):
            raise Exception('fhfhfhf')
        while b < self._min_characteristics and counter <max_loops:

            weights = [1 if x == 0 else 0 for x in only_ints_vals]
            get_rdm_i = random.choices(only_ints, weights=weights)[0]

            # todo if only 1 this will get stuck
            if vector[get_rdm_i] == 0:
                while new_j == 0:
                    # print('this should only ever be 3 ocasionally 2', self.get_num_discrete_values(get_rdm_i))
                    get_rdm_j = random.randint(
                        0, self.get_num_discrete_values(get_rdm_i) - 1)
                    new_j = self.get_value(get_rdm_i, get_rdm_j)
                vector[get_rdm_i] = new_j
                prmVect[get_rdm_i] = new_j
                
                
                b += new_j
                new_j = 0

        if hasattr(self, 'forced_variables'):
            self.force_inclusion(vector)

    def force_inclusion(self, vector):
        if self.forced_variables is not None:
            add_if_none = self.get_charaname_idx()
            for i in add_if_none:
                if vector[i] == 0:
                    vector[i] = 1

    def get_charaname_idx(self):
        if self.forced_variables is None:
            print('no forced variables')
            return []
        all_idx = list()
        this_names = self._characteristics_names.copy()
        for i in self.forced_variables:
            all_idx.append(this_names.index(i))
        return all_idx

    def get_num_params(self, block=False):
        Kf = 0 if self.fixed_fit is None else len(self.fixed_fit)
        Kr = 0 if self.rdm_fit is None else len(self.rdm_fit) 
        Kr = Kr if self.grouped_rpm is None else Kr + len(self.grouped_rpm)*len(self.group_names)
        Kr_b = Kr
        cor_l = 0 if self.rdm_cor_fit is None else len(self.rdm_cor_fit)
        Kh = 0 if self.hetro_fit is None or (Kr +cor_l == 0) else len(self.hetro_fit) + len(set(self.dist_hetro))

        zi_terms = 0 if self.zi_fit is None else len(self.zi_fit)
        Kchol = int((cor_l *
                     (cor_l+1))/2)
        n_coeff = Kf + Kr + cor_l + Kchol + Kr_b + Kh
        if block:
            return [Kf, Kr, cor_l, Kr_b, Kchol, Kh, zi_terms]
        return Kf, Kr, cor_l, Kr_b, Kchol, Kh, zi_terms

    def find_index_of_block(self, lst, value):
        cumulative_sum = 0
        for i, num in enumerate(lst):
            cumulative_sum += num
            if cumulative_sum > value:
                #print('number id', value-cumulative_sum+num, 'of' , i)

                return i, value-cumulative_sum+num
        # If we reach here, the value is greater than the sum of all elements in the list
        raise Exception('this should not ever happend')
        return len(lst)

    def above_median(self, numbers):
        median_index = len(numbers) // 2
        sorted_numbers = sorted(numbers)
        median = sorted_numbers[median_index]
        return [num for num in numbers if num > median]

    def get_block_to_delete(self, delete_idxs, dispersion):
        block = self.get_num_params(True)
        my_set = set()
        cc = [i for i
              in range(len(self.none_handler(self.rdm_cor_fit))) for j in range(i+1)]
        for idx in delete_idxs:

            if sum(block) + dispersion == idx:
                print('neg_binom bad')
            a, b = self.find_index_of_block(block, idx)
            if a != 4:
                my_set.add((a, b))
            else:
                my_set.add((a, cc[b]))
        grouped_dict = {}
        for key, value in my_set:
            if key in grouped_dict:
                grouped_dict[key].append(value)
            else:
                grouped_dict[key] = [value]

        for key in grouped_dict:
            a = key

            if a == 0:
                for b in sorted(grouped_dict[key], reverse=True):
                    self.fixed_fit.pop(b)
                    self.transform_id_names.pop(b)
            elif a == 1:
                for b in sorted(grouped_dict[key], reverse=True):

                    self.rdm_fit.pop(b)
                    self.dist_fit.pop(b)
                    self.transform_id_names.pop(
                        b+len(self.none_handler(self.fixed_fit)))
            elif a == 2:
                for b in sorted(grouped_dict[key], reverse=True):

                    self.rdm_cor_fit.pop(b)
                    self.transform_id_names.pop(
                        b+len(self.none_handler(self.fixed_fit))+len(self.none_handler(self.rdm_fit)))
                    self.dist_fit.pop(b+len(self.none_handler(self.rdm_fit)))
            elif a == 3:
                #self.fixed_fit = self.fixed_fit+[self.rdm_fit[b]]
                for b in sorted(grouped_dict[key], reverse=True):

                    self.rdm_fit.pop(b)
                    self.dist_fit.pop(b)
                    self.transform_id_names.pop(
                        b+len(self.none_handler(self.fixed_fit)))
            elif a == 4:

                #self.fixed_fit = self.fixed_fit+[self.rdm_cor_fit[cc[b]]]
                for b in sorted(grouped_dict[key], reverse=True):

                    self.rdm_cor_fit.pop(b)
                    self.dist_fit.pop(b+len(self.none_handler(self.rdm_fit)))
                    self.transform_id_names.pop(
                        b+len(self.none_handler(self.fixed_fit))+len(self.none_handler(self.rdm_fit)))
                    

        if len(self.transform_id_names) != len(self.none_handler(self.fixed_fit) + self.none_handler(self.rdm_cor_fit) + self.none_handler(self.rdm_fit)):
            raise Exception('pop wrong for id names')

            # return 'need to delete all of the dups'
            # self.rdm_cor_fit.pop(self.name_deleter(idx))

    def get_value_to_delete(self, idx, dispersion):
        block = self.get_num_params(True)
        if sum(block) + dispersion == idx:
            print('neg_binom bad')
        a, b = self.find_index_of_block(block, idx)
        if a == 0:
            self.fixed_fit.pop(b)
            self.transform_id_names.pop(b)
        elif a == 1:
            self.rdm_fit.pop(b)
            self.dist_fit.pop(b)
            self.transform_id_names.pop(
                b+len(self.none_handler(self.fixed_fit)))
        elif a == 2:
            self.rdm_cor_fit.pop(b)
            self.dist_fit.pop(b+len(self.rdm_fit))
            self.transform_id_names.pop(
                b+len(self.none_handler(self.fixed_fit))+len(self.none_handler(self.rdm_fit)))
        elif a == 3:
            #self.fixed_fit = self.fixed_fit+[self.rdm_fit[b]]
            self.rdm_fit.pop(b)
            self.dist_fit.pop(b)
            self.transform_id_names.pop(
                b+len(self.none_handler(self.fixed_fit)))
        elif a == 4:

            cc = [i for i
                  in range(len(self.rdm_cor_fit)) for j in range(i+1)]
            # print(self.rdm_cor_fit[cc[b]])
            #self.fixed_fit = self.fixed_fit+[self.rdm_cor_fit[cc[b]]]
            self.rdm_cor_fit.pop(cc[b])
            self.dist_fit.pop(cc[b]+len(self.rdm_fit))
            self.transform_id_names.pop(
                cc[b]+len(self.none_handler(self.fixed_fit))+len(self.none_handler(self.rdm_fit)))
            # return 'need to delete all of the dups'
            # self.rdm_cor_fit.pop(self.name_deleter(idx))

    def get_param_num(self, dispersion=0):
        a = np.sum(self.get_num_params()) + \
            self.num_dispersion_params(dispersion)
        return a

    def get_type_and_safe(self, idx):
        chain = self.get_num_params(True)
        counter = 0
        for ii, var in enumerate(chain):
            counter = var+counter
            if idx < counter:
                if(chain[ii]) == 1:
                    self.significant = 2
                    return 0
                else:
                    return 1

    def num_dispersion_params(self, dispersion):
        if dispersion == 0:
            return 0
        elif dispersion == 4:
            return 2
        else:
            return 1

    def get_pvalue_info_alt(self, pvalues, names, sig_value=0.05, dispersion=0, is_halton=1, delete=0, return_violated_terms=0):

        num_params = len(pvalues)
        Kf, Kr, Kc, Kr_b, Kchol, Kh, zi_b = self.get_num_params()

        vio_counts = 0
        pvalues = np.array([float(string) for string in pvalues])
        if dispersion == 0:
            subpvalues = pvalues.copy()

        else:
            slice_this_amount = self.num_dispersion_params(dispersion)
            if pvalues[-1] > sig_value:

                vio_counts += 1
            subpvalues = pvalues[:-slice_this_amount].copy()

        
        if Kh >1:
            if subpvalues[-1] < sig_value:
                subpvalues[-Kh] = 0
            
        
        
        subpvalues = np.array([float(string) for string in subpvalues])

        if Kr_b + Kchol > 0:
            sum_k = Kf+Kr+Kc
            for i in range(Kf, sum_k):

                subpvalues[i] = 0

            sum_k += Kr_b
            if Kchol > 0:
                cc = [i for i
                      in range(len(self.rdm_cor_fit)) for j in range(i+1)]

            lower_triangular = subpvalues[sum_k:sum_k+Kchol]

            n = Kc  # compute matrix size
            # initialize matrix with zeros
            matrix_alt = [[0] * n for _ in range(n)]
            index = 0

            for i in range(n):
                for j in range(i+1):
                    # fill in lower triangular entries
                    matrix_alt[i][j] = lower_triangular[index]
                    # fill in upper triangular entries
                    matrix_alt[j][i] = lower_triangular[index]
                    index += 1

            if len(matrix_alt) > 0:
                matrix_alt = np.array(matrix_alt)
                # block out potential random parameters
                matrix_diag = np.diag(matrix_alt).copy()

                np.fill_diagonal(matrix_alt, sig_value)

                # set_matrix_alt to 0 for signficant correlated tersm
                # Find the rows where any element is less than the threshold
                rows_to_zero = np.any(matrix_alt < sig_value, axis=1)

                # Set the corresponding rows to zero
                matrix_alt[rows_to_zero, :] = 0

                if np.max(matrix_alt) < sig_value:
                    for j in range(sum_k, sum_k+Kchol):
                        subpvalues[j] = 0
                else:

                    # revert the matrix
                    np.fill_diagonal(matrix_alt, matrix_diag)

                    # convert 2d matrix, into a lower triangular marix flattened
                    result = []
                    n_rows, n_cols = np.shape(matrix_alt)
                    for i in range(n_rows):
                        for j in range(n_cols):
                            if j <= i:
                                result.append(matrix_alt[i][j])

                    ii = 0
                    for j in range(sum_k, sum_k+Kchol):
                        # print(names[i])

                        subpvalues[j] = result[ii]
                        ii += 1

        vio_counts += len([i for i in subpvalues if i > sig_value])

        saving_at_least = random.randint(1, 6)
        max_delete_pre = np.max((len(self.none_handler(self.fixed_fit)+self.none_handler(
            self.rdm_fit)+self.none_handler(self.rdm_cor_fit)) - saving_at_least, 0))
        max_delete = np.min((max_delete_pre, saving_at_least))
        indexes = sorted(range(len(subpvalues)),
                         key=lambda i: subpvalues[i], reverse=True)
        indexes = indexes[:max_delete]

        if np.max(subpvalues) > sig_value:
            if num_params <= self._min_characteristics:
                self.significant = 2
                if return_violated_terms:
                    return False, vio_counts
                else:
                    return False, vio_counts  # added for testing

            if delete:
                # if self.get_type_and_safe(max_index):
                delete_idx = [i for i in range(
                    len(subpvalues)) if subpvalues[i] > sig_value]
                if len(delete_idx) > len(indexes):
                    delete_idx = indexes

                self.get_block_to_delete(delete_idx, dispersion)

                #self.get_value_to_delete(max_index, dispersion)
                if return_violated_terms:
                    return True, vio_counts
                else:
                    return True, vio_counts  # added for testing

        else:
            self.significant = 1

        if return_violated_terms:
            return False, vio_counts
        else:
            return False, vio_counts  # added for testing

    def get_coeff_names(self, is_halton, rdm_params, rdm_distr, fixed_params=None, dispersion=0):
        combine_tr = [i + ' (Std. Dev.) ' + rdm_distr[j]
                      for j, i in enumerate(rdm_params)]
        fixed_params = [] if fixed_params is None else fixed_params
        if is_halton:
            if dispersion == 0:
                coeff_names = fixed_params + rdm_params + combine_tr
            elif dispersion == 1:
                coeff_names = fixed_params + rdm_params + \
                    combine_tr + ['NB ScalParm']
            elif dispersion == 2:
                coeff_names = fixed_params + rdm_params + \
                    combine_tr + ['GP ScalParm']
            elif dispersion == 3:
                coeff_names = fixed_params + rdm_params + \
                    combine_tr + ['COMP ScalParm']
            else:
                raise ValueError(
                    "dispersion must be an integer between 0 and 3")
        else:
            if dispersion == 0:
                coeff_names = fixed_params + rdm_params
            elif dispersion == 1:
                coeff_names = fixed_params + rdm_params + ['NB ScalParm']
            elif dispersion == 2:
                coeff_names = fixed_params + rdm_params + ['GP ScalParm']
            elif dispersion == 3:
                coeff_names = fixed_params + rdm_params + ['COMP ScalParm']
            else:
                raise ValueError(
                    "dispersion must be an integer between 0 and 3")
        return coeff_names

    def get_pvalue_info(self, pvalues, fixed_params, rdm_params, rdm_distr, sig_value=0.05, dispersion=0, is_halton=1):
        num_params = len(pvalues)
        if pvalues is None:
            self.significant = 2
            return
        else:
            if dispersion != 0:

                subpvalues = pvalues[:-1].copy()
            else:
                subpvalues = pvalues.copy()

        self.significant = 0
        if np.any(subpvalues > sig_value):
            # min number of params
            if num_params <= self._min_characteristics:
                self.significant = 2
                return
            lsf = len(fixed_params or '')
            lsr = len(rdm_params or '')
            max_index = np.argmax(pvalues)
            if max_index < lsf:
                if len(fixed_params) == 1:
                    self.significant = 2
                    return
                else:
                    return
            elif max_index < lsf + lsr:
                if len(rdm_params) == 1:
                    self.significant = 2
                    return
                else:
                    # self.draws1 = None  # todo have the draws stored for multiple dimensions to save time
                    return
            elif max_index < lsf + 2 * lsr:
                if len(rdm_params) == 1:
                    self.significant = 2
                    return
                else:
                    return
            else:
                self.significant = 2
                return
        else:
            self.significant = 1
            if is_halton:
                combine_tr = []
                for j, i in enumerate(rdm_params):
                    util = i.replace(i, i + ' (Std. Dev.) ' + rdm_distr[j])
                    combine_tr.append(util)
                if dispersion == 0:
                    self.coeff_names = self.return_list(
                        fixed_params) + self.return_list(rdm_params) + combine_tr
                elif dispersion == 1:
                    self.coeff_names = self.return_list(
                        fixed_params) + self.return_list(rdm_params) + combine_tr + ['NB ScalParm']
                elif dispersion == 2:
                    self.coeff_names = self.return_list(
                        fixed_params) + self.return_list(rdm_params) + combine_tr + ['GP ScalParm']
                elif dispersion == 3:
                    self.coeff_names = self.return_list(
                        fixed_params) + self.return_list(rdm_params) + combine_tr + ['COMP ScalParm']
            else:
                if dispersion == 0:
                    self.coeff_names = self.return_list(
                        fixed_params) + self.return_list(rdm_params)
                elif dispersion == 1:
                    self.coeff_names = self.return_list(
                        fixed_params) + self.return_list(rdm_params) + ['NB ScalParm']
                elif dispersion == 2:
                    self.coeff_names = self.return_list(
                        fixed_params) + self.return_list(rdm_params) + ['GP ScalParm']
                elif dispersion == 3:
                    self.coeff_names = self.return_list(
                        fixed_params) + self.return_list(rdm_params) + ['COMP ScalParm']

            alt_test_names = self.get_coeff_names(
                is_halton, rdm_params, rdm_distr, fixed_params, dispersion)
            if alt_test_names != self.coeff_names:
                raise Exception('function doesn')

            return

    def return_list(self, input):
        'hanndles cases of none types for printing'
        if input is None:
            return []
        else:
            return input

    def check_pvalues_alt(self, pvalues, subfixed, subrandom, subrandom_cor, sub_group, distribution, tester=0.05, dispersion=0, is_halton=0, is_ceil=0, ceil=2):
        num_params = len(pvalues)

        dispersion_name = self.get_dispersion_name(dispersion)

        d = [subfixed, subrandom, subrandom_cor, dispersion_name, sub_group]
        dd = []
        for i in d:
            if i is not None:
                dd += i
        self.coeff_names = dd
        rdm_coeffs = 0 if subrandom is None else len(subrandom)
        rdm_coeffs = rdm_coeffs if subrandom_cor is None else rdm_coeffs + \
            len(subrandom_cor)
       
        if len(distribution)  != rdm_coeffs:
            print('hold, big dog')
            #raise Exception

        is_delete = 0
        if pvalues is None:
            self.significant = 2
            return is_delete
        if dispersion == 0:
            subpvalues = pvalues.copy()
        else:
            subpvalues = pvalues[:-1].copy()
        self.significant = 0

        if is_ceil:
            if np.any(subpvalues >= ceil):
                ii = 0
                for idx, val in enumerate(subpvalues):
                    if val > ceil:
                        self.get_value_to_delete(ii, dispersion)
                        is_delete = 1
                    else:
                        ii += 1

                return is_delete

        if np.any(subpvalues >= tester):
            # min number of params
            if num_params <= self._min_characteristics:
                self.significant = 2
                return is_delete

            max_index = np.argmax(pvalues)
            delete_this = dd[max_index]
            self.get_value_to_delete(max_index, dispersion)
            is_delete = 1
            return is_delete

        else:
            self.significant = 1
            self.significant = 1
            return is_delete

    def check_pvalues(self, pvalues, subfixed, subrandom, distribution, tester=0.05, dispersion=0, is_halton=0):  # TODO, grab names
        num_params = len(pvalues)

        if len(distribution) != len(subrandom):
            print('hold, big dog')
            raise Exception

        if dispersion != 0:
            if len(pvalues) != (len(subfixed)+len(subrandom) + 1):
                print('hold big dog')
                raise Exception
        is_delete = 0
        if pvalues is None:
            self.significant = 2
            return is_delete
        if dispersion == 0:
            subpvalues = pvalues.copy()
        else:
            subpvalues = pvalues[:-1].copy()
        self.significant = 0

        if np.any(subpvalues >= tester):
            # min number of params
            if num_params <= self._min_characteristics:
                self.significant = 2
                return is_delete
            lsf = len(subfixed)
            lsr = len(subrandom)
            max_index = np.argmax(pvalues)
            if max_index < lsf:
                if len(subfixed) == 1:
                    self.significant = 2
                    return is_delete
                else:
                    subfixed.pop(max_index)
                    self.fixed_fit = subfixed
                    is_delete = 1
                    return is_delete
            elif max_index < lsf + lsr:
                if len(subrandom) == 1:
                    self.significant = 2
                    return is_delete
                else:
                    subrandom.pop(max_index - lsf)
                    self.rdm_fit = subrandom
                    distribution.pop(max_index - lsf)
                    self.dist_fit = distribution
                    is_delete = 1
                    self.draws1 = None  # todo have the draws stored for multiple dimensions to save time
                    return is_delete
            elif max_index < lsf + 2 * lsr:
                if len(subrandom) == 1:
                    self.significant = 2
                    return is_delete
                else:
                    subrandom.pop(max_index - lsf - lsr)
                    distribution.pop(max_index - lsf - lsr)
                    self.rdm_fit = subrandom
                    self.dist_fit = distribution
                    is_delete = 1
                    return is_delete
            else:
                self.significant = 2
                return is_delete
        else:
            self.significant = 1
            combine_tr = []
            for j, i in enumerate(subrandom):
                util = i.replace(i, i + ' std: ' + distribution[j])
                combine_tr.append(util)
            if is_halton:
                if dispersion == 0:
                    self.coeff_names = subfixed + subrandom + combine_tr
                elif dispersion == 1:
                    self.coeff_names = subfixed + \
                        subrandom + combine_tr + ['disp']
                elif dispersion == 2:
                    self.coeff_names = subfixed + \
                        subrandom + combine_tr + ['nu']
                else:
                    raise Exception
            else:
                if dispersion == 0:
                    self.coeff_names = subfixed + subrandom
                elif dispersion == 1:
                    self.coeff_names = subfixed + subrandom + ['disp']
                elif dispersion == 2:
                    self.coeff_names = subfixed + subrandom + ['nu']
                else:
                    raise Exception

            return is_delete

    def split(self, array, la=None):
        if la is not None:
            return array[:la], array[la:]
        else:
            half = len(array) // 2
            return array[:half], array[half:]

    def nbr_routine(self, vector):
        model_nature = self.get_distinct_model_parts(
            vector).copy()  # just added to grab the fixed fit TODO: Clean up
        self.define_selfs_fixed_rdm_cor(
            model_nature)

    def make_list_hasher(self, dispersion):

        licken = self.none_handler(self.fixed_fit) + ['end_f']+self.none_handler(self.rdm_fit) + ['end_r'] + self.none_handler(self.rdm_cor_fit) + [
            'end_c']+self.none_handler(self.dist_fit)+self.none_handler(self.transform_id_names) + self.none_handler([dispersion])
        a = self.hasher_check(licken)

        return a

    def sort_the_sub(self, my_dict):
        # Calculate the averages for each value across all items
        if self.is_multi:

            value1_avg = np.mean([[d[0][self._obj_1] for d in my_dict]])
            value2_avg = np.mean([[d[0][self._obj_2] for d in my_dict]])
            value3_avg = np.mean([[d[0]['pval_percentage'] for d in my_dict]])
            sorted_dict = sorted(my_dict, key=lambda x: x[0]['pval_percentage'] *
                                 value3_avg + x[0][self._obj_2]*value2_avg+x[0][self._obj_1]*value1_avg)
            #sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1]['value1']*value1_avg*0.3 + x[1]['value2']*value2_avg*0.4 + x[1]['value3']*value3_avg*0.3, reverse=True))
            return sorted_dict  # return bests
        else:
            sorted(my_dict, key=lambda x: x[0]['pval_percentage'])

    def get_fitness(self, vector, multi=False, verbose=False, max_routine=3):
        obj_1 = 10 ** 9
        obj_best = None
        sub_slns = list()

        model_nature = self.get_distinct_model_parts(
            vector)  # just added to grab the fixed fit TODO: Clean up
        dispersion = model_nature.get('dispersion')
        self.define_selfs_fixed_rdm_cor(model_nature)
        try:
            self.repair(vector)
        except Exception as e:
            print('prob here')
            print(vector)
            print(e)    
        layout = vector.copy()
        trial_run = 0
        max_trial = 0

        model_nature = self.get_distinct_model_parts(
            vector)  # todo return insignificant p values
        
       
        a = {}
        obj_1, model_mod  = self.makeRegression(model_nature, layout=layout, **a)
      
       
                

        sub_slns.append([obj_1.copy()])

        obj_best = obj_1.copy()
        if any(sub_string in obj_1['simple'] for sub_string in ["rp", "c", "zi"]):
            trial_run, vio_counts = self.get_pvalue_info_alt(
                self.pvalues, self.coeff_names, self.pvalue_sig_value, dispersion, 1, trial_run)  # i added
            
        trial_run = 0
        
        
        #trial_run = self.get_pvalue_info_alt(self.pvalues, self.coeff_names, sig_value = 0.05, dispersion = dispersion ,is_halton = obj_1['simple'], delete = 1)
        if trial_run:
           
            if obj_1['num_parm'] - obj_1['pval_exceed'] > 5:
                self.repair(vector, obj_1['num_parm']-5)
            else:
                self.repair(vector, obj_1['num_parm']-obj_1['pval_exceed'])
            model_nature = self.get_distinct_model_parts(
            vector)  # todo return insignificant p values
            self.define_selfs_fixed_rdm_cor(model_nature)
            layout = vector.copy()
       
        
            
                    
                
            
            
            while max_trial <= max_routine and trial_run == 1:  # and max_trial <= 200:

                obj_1, model_mod= self.makeRegression(model_nature, layout = layout, **a)
               

                if obj_best is None:
                    obj_best = obj_1

                if sub_slns[-1][0]['pval_percentage'] < obj_1['pval_percentage']:
                    trial_run = 0
                    print('lets break')

                sub_slns.append(
                    [obj_1])
                if any(sub_string in obj_1['simple'] for sub_string in ["rp", "c", "zi"]):
                    trial_run, vio_counts = self.get_pvalue_info_alt(
                        self.pvalues, self.coeff_names, self.pvalue_sig_value, dispersion, 1, 0)  # i added

                max_trial += 1

        try:

            if multi:
                sub_slns = self.sort_the_sub(sub_slns)
            else:
                sub_slns = sorted(sub_slns, key=lambda x: x[0][self._obj_1])
        except:
            print('excetpion ook into potential problem')
            sub_slns = sorted(sub_slns, key=lambda x: x[0][self._obj_1])

        #sub_slns = sorted(sub_slns, key=lambda x: x[0]['pval_percentage'])

        obj_1 = sub_slns[
            -1]
        if type(obj_1) == list:
            obj_1 = obj_1[0]
            
        if obj_1 is not None:
            obj_1['layout'] = vector.copy()
            #alpha, alpha_rdm, alpha_cor_rdm = self.modify(
                   # obj_1['fixed_fit'], obj_1['rdm_fit'], obj_1['rdm_cor_fit'])
            #a = self.modifyn(model_mod)
            #vector = self.modify_vector(
                #vector, alpha, alpha_rdm, alpha_cor_rdm)
            sub_vector = vector[:self._characteristics]
            dispersion_parm = vector[-1]
            if dispersion_parm == 0:
                num_parm = sum(sub_vector)
            else:
                num_parm = sum(sub_vector) + 1

            if not self.is_quanitifiable_num(obj_1[self._obj_1]):
                obj_1[self._obj_1] = 10 ** 9
            else:
                if obj_1[self._obj_1] <= 0:
                    obj_1[self._obj_1] = 10 ** 9

        if multi:
            
            if  obj_1['layout'] != vector:
                vector = obj_1['layout'].copy()
                print('not the same will this ever occcur? Yes if you are reading this')
              
                
            if obj_1['MAE'] is None:
                raise Exception

            if obj_1['pval_exceed'] is None:
                obj_1['pval_exceed'] = len(vector)
                #raise Exception

        else:
            if  obj_1['layout'] != vector:
                vector = obj_1['layout'].copy()
                print('not the same will this ever occcur? Yes if you are reading this')
            
            if obj_1['pval_exceed'] is None:
                obj_1['pval_exceed'] = len(vector)  # TODO check this

                #raise Exception

            self.Last_Sol = obj_1.copy()

            #

        self.reset_sln()
        if not self.is_quanitifiable_num(obj_1[self._obj_1]):
            obj_1[self._obj_1] = 10 ** 9
        else:
            if obj_1[self._obj_1] == 0:
                obj_1[self._obj_1] = 10 ** 9
        if verbose:
            print('The best solution iteratively is of objective value:', obj_1)

        if multi:
            if not isinstance(obj_1, dict):
                raise Exception
            return obj_1
        else:
            if not isinstance(obj_1, dict):
                raise Exception

        return obj_1

    def hasher_check(self, new_sln):
        # check if the list has been generated before
        if hash(make_hashable(new_sln)) in self.generated_sln:
            print("List already generated before.")
            return True
        else:
            # add the hash value of the new list to the set
            self.generated_sln.add(hash(make_hashable(new_sln)))

            return False

    def reset_sln(self):
        self.full_model = None
        self.convergence = None
        self.coeff_names = None
        self.draws1 = None
        self.coeff_ = None
        self.zi_fit = None
        self.bic = None
        self.log_lik = None
        self.pvalues = None
        self.pvalue_exceed = None
        self.fixed_fit = None
        self.rdm_fit = None
        self.dist_fit = None
        self.MAE = None
        self.grouped_rpm = None
        
        
        self.rdm_grouped_fit = None

      
    
       
        
        self.dist_fit_grouped  = None
        self.dist_fit_grouped_repeat = None
        self.grab_transforms = 0

        # self.significant = 0

    def modify_vector(self, vector, alpha, alpha_rdm, alpha_rdm_cor):
        for i in range(len(alpha)):
            if alpha[i]:
                vector[i] = 1
            elif alpha_rdm[i]:
                vector[i] = 2
            elif alpha_rdm_cor[i]:
                vector[i] = 3
            else:
                vector[i] = 0
        return vector

    def get_value(self, i, j=None):
        """
            Values are returned uniformly at random in their entire range. Since both parameters are continuous, index can be ignored.
        """
        # if j is not None:
        if self.is_discrete(i):
            if j is not None:
                return self._discrete_values[i][j]

            return self._discrete_values[i][random.randint(0, len(self._discrete_values[i]) - 1)]

        else:
            raise Exception  # ('not yet implemented')
            # return random.uniform(self._lower_bounds[i], self._upper_bounds[i])

    def get_lower_bound(self, i):
        return self._lower_bounds[i]

    def get_upper_bound(self, i):
        return self._upper_bounds[i]

    def is_variable(self, i):
        return self._variable[i]

    def modulo_or_divisor(self, dividend, divisor):
        result = dividend % divisor
        if result == 0:
            return divisor
        else:
            return result

    def is_discrete(self, i):
        # all variables are continuous
        if isinstance(self._discrete_values[i], float):
            return False
        else:
            return True

    def get_num_parameters(self) -> int:
        return len(self._discrete_values)

    def get_num_discrete_values(self, i):
        if self.is_discrete(i):
            # FIXME potentially broken
            return len(set(self._discrete_values[i]))
        else:
            raise Exception('not yet implemented')
        # return float('+inf')

    def get_index(self, i, v):
        k = 0
        for j in self._discrete_values[i]:
            if j == v:
                return k
            k += 1
        raise Exception

    def use_random_seed(self):
        return hasattr(self, '_random_seed') and self._random_seed

    def set_random_seed(self):
        print('Imbdedding Seed', self._random_seed)
        np.random.seed(self._random_seed)
        #pd.random.seed(self._random_seed)
        random.seed(self._random_seed)
        return self._random_seed

    def get_max_imp(self):
        return self._max_imp

    def get_max_time(self):
        return self._max_time

    def get_hmcr(self):
        return self._hmcr

    def get_par(self):
        return self._par

    def get_hms(self):
        return self._hms

    def update_hmcr(self, iteration, is_sin=False):
        """
        Purpose: 
        update self._hmcr based on the iteration

        """
        if is_sin:
            self._hmcr = (self._hmcr_min+((self._hmcr_max - self._hmcr_min) /
                          self._max_imp)*iteration)*np.max([0, np.sign(np.sin(iteration))])
        else:
            self._hmcr = (
                self._hmcr_min+((self._hmcr_max - self._hmcr_min)/self._max_imp)*iteration)

    # end def

    def update_par(self, iteration, is_sin=False):
        """
        Purpose: 
        update self._par based on the iteration

        """
        if is_sin:
            self._par = (self._par_min+((self._par_max - self._par_min) /
                         self._max_imp)*iteration)*np.max([0, np.sign(np.sin(iteration))])
        else:
            self._par = (
                self._par_min+((self._par_max - self._par_min)/self._max_imp)*iteration)

    def get_mpai(self):
        return self._mpai

    def get_mpap(self):
        return self._mpap

    def maximize(self):
        return self._maximize

    def get_termination_iter(self):
        return self._max_iterations_improvement
    # def plot_best_generation(self, x, y):
    #     import matplotlib.pyplot as plt
    #     x.pop(0)
    #     y.pop(0)
    #     df = pd.DataFrame(list(zip(x, y)), columns=['x', 'y'])
    #     df.to_csv(index=False)
    #     fig, ax = plt.subplots()
    #     ax.plot(x, y)
    #     ax.set(xlabel='Generation Best', ylabel=self._GOF_measure, title='Best Solution Per Generation')
    #     ax.grid()
    #     plt.show()
    #     print('cool beans')
    # def return_data(self):
    #     df = pd.DataFrame(data=self._output_data_points, columns=["FSI"])
    #     pt_df = pd.concat([df, self._input_data_points], axis=1)
    #     return pt_df

    def score(self, params):
        """
        Poisson model score (gradient) vector of the log-likelihood
        Parameters
        ----------
        params : array_like
            The parameters of the model
        Returns
        -------
        score : ndarray, 1-D
            The score vector of the model, i.e. the first derivative of the
            loglikelihood function, evaluated at `params`
        Notes
        -----
        .. math:: \\frac{\\partial\\ln L}{\\partial\\beta}=\\sum_{i=1}^{n}\\left(y_{i}-\\lambda_{i}\\right)x_{i}
        where the loglinear model is assumed
        .. math:: \\ln\\lambda_{i}=x_{i}\\beta
        """
        X = self.exog
        L = np.exp(np.dot(X, params))
        return np.dot(self.endog - L, X)

    def GenPos_Score(self, params, y, mu, X, p=0, obs_specific=False):

        alpha = params[-1]
        exog = X
        mu_p = np.power(mu, p)
        a1 = 1+alpha*mu_p
        a2 = mu+alpha*mu_p*y
        a3 = alpha*p*mu**(p-1)
        a4 = a3*y
        dmudb = mu*exog
        dalpha = (mu_p * (y * ((y - 1) / a2 - 2 / a1) + a2 / a1**2))
        dparams = dmudb * (-a4 / a1 +
                           a3 * a2 / (a1 ** 2) +
                           (1 + a4) * ((y - 1) / a2 - 1 / a1) +
                           1 / mu)
        

        if obs_specific:
            dparams = dparams.sum(axis = 1)
            dalpha = dalpha.sum(axis = 1)
            return np.concatenate((dparams, dalpha),
                                      axis=1)
            return score_obs
        else:
            dparams = dparams.sum(axis = 1)
            dalpha = dalpha.sum(axis = 0)
            return np.r_[dparams.sum(0), dalpha.ravel()]
            return score
        
        score_obs = np.concatenate((dparams, dalpha),
                                   axis=2)

        score = np.sum(score_obs, axis=(1,2))
        
        
        
         
    def compute_score_nb_rp(self, Xf, Xr, draws, params, y, mu):
        try:
            K = len(params)
            X_std = np.zeros((Xf.shape[0], K, draws.shape[2]))
            Xr_long = np.repeat(Xr[:, :, np.newaxis], draws.shape[2], axis=2)
            X_std = Xr_long*draws
            gradr = np.zeros((K, draws.shape[2]))
            for i in range(draws.shape[2]):
                X = np.concatenate((Xf, Xr, X_std[:, :, i]), axis=1)
                gradr[:, i] = self.NB_Score(params, y, mu[:, :, i], X, 0)
            #grad = gradr.mean(axis =1)

            return gradr.sum(axis=1)
        except Exception as e:
            print(e)
            print('f')

    def negbinom_gradients(r, p, k, a=None):  # TODO: delete if wrong
        """_summary_

        Args:
            r (_type_): rate paramaters or dispersion of the nb
            p (_type_): probability
            k (_type_): vector of (non-negative integer) quantiles.
            a (_type_, optional): optional paramater, if none NB model, otherwise NB-Lindley model with Lindley paramater a.

        Raises:
            Exception: _description_
            Exception: _description_
            ValueError: _description_
            Exception: _description_
            Exception: _description_

        Returns:
            _type_: _description_
        """
            #fine the NegBinom PMF
        import scipy.special as sps
        negbinom_pmf = sps.comb(k+r-1, k) * p**r * (1-p)**k

        # Calculate the gradient of the NegBinom PMF with respect to r and p
        d_negbinom_pmf_dr = sps.comb(
            k+r-1, k) * (np.log(p) - sps.digamma(r)) * p**r * (1-p)**k
        d_negbinom_pmf_dp = sps.comb(
            k+r-1, k) * (r/p - (k+r) / (1-p)) * p**r * (1-p)**k

        if a is not None:
            # Define the NegBinom-Lindley PMF
            negbinom_lindley_pmf = sps.comb(a+k-1, k) * p**r * (1-p)**k

            # Calculate the gradient of the NegBinom-Lindley PMF with respect to r, p, and a
            d_negbinom_lindley_pmf_dr = sps.comb(
                a+k-1, k) * (np.log(p) * p**r * (1-p)**k)
            d_negbinom_lindley_pmf_dp = sps.comb(
                a+k-1, k) * ((r/p - (k+r) / (1-p)) * p**r * (1-p)**k)
            d_negbinom_lindley_pmf_da = sps.comb(
                a+k-1, k) * (-sps.digamma(a) + sps.digamma(a+k)) * p**r * (1-p)**k

            return [d_negbinom_pmf_dr, d_negbinom_pmf_dp], [d_negbinom_lindley_pmf_dr, d_negbinom_lindley_pmf_dp, d_negbinom_lindley_pmf_da]
        else:
            return [d_negbinom_pmf_dr, d_negbinom_pmf_dp]

    def f(self, x, N, sig, mu):
        return norm.pdf(x, 0, 1) * poisson.pmf(N, np.exp(x * sig + mu))

    def poilog(self, n, mu, sig):
        from scipy import integrate
        if len(mu) > 1 or len(sig) > 1:
            raise ValueError(
                "vectorization of mu and sig is currently not implemented")
        if any((n[n != 0] / np.trunc(n[n != 0])) != 1):
            raise ValueError("all n must be integers")
        if any(n < 0):
            raise ValueError("one or several values of n are negative")
        if not np.all(np.isfinite(np.concatenate((mu, sig)))):
            raise ValueError("all parameters should be finite")
        if sig <= 0:
            raise ValueError("sig is not larger than 0")
        spos = np.where(n < 8)[0]
        lpos = np.where(n >= 8)[0]
        val = np.empty_like(n)

        if spos.size > 0:
            vali = np.empty(spos.size)
            for i in range(spos.size):
                try:
                    vali[i] = integrate.quad(
                        self.f, -np.inf, np.inf, sig, mu, args=(n[spos[i]],))[0]
                except:
                    vali[i] = 1e-300
            valp = self.poilog(n[spos], mu, sig**2)[0]
            val[spos] = np.maximum(vali, valp)
        if lpos.size > 0:
            val[lpos] = self.poilog(n[lpos], mu, sig**2)[0]
        return val

    def negbinom_pmf(self, r, p, k, a=None):  # TODO: delete if wrong
        """_summary_

        Args:
            r (_type_): rate paramaters or dispersion of the nb
            p (_type_): probability
            k (_type_): vector of (non-negative integer) quantiles.
            a (_type_, optional): optional paramater, if none NB model, otherwise NB-Lindley model with Lindley paramater a.

        Raises:
            Exception: _description_
            Exception: _description_
            ValueError: _description_
            Exception: _description_
            Exception: _description_

        Returns:
            _type_: _description_
        """
    # Define the NegBinom PMF

        if a is None:
            negbinom_pmf = sc.comb(k+r-1, k) * p**r * (1-p)**k
            return negbinom_pmf
        else:
            negbinom_lindley_pmf = sc.comb(a+k-1, k) * p**r * (1-p)**k
            return negbinom_lindley_pmf

    def nbl_score(self, y, X, betas, alpha, theta):
        from scipy.special import gammaln, psi
        """
        Calculate the Negative Binomial-lindley model score vector of the log-likelihood.

        Parameters:
        -----------
        y : numpy array
            The dependent variable of the model.
        X : numpy array
            The independent variables of the model.
        beta : numpy array
            The coefficients of the model.
        alpha : float
            The dispersion parameter of the Negative Binomial-lindley distribution.
        theta : float
            The theta parameter of the Negative Binomial-lindley distribution.

        Returns:
        --------
        score : numpy array
            The score vector of the Negative Binomial-lindley model log-likelihood.
        """
        alpha = betas[-1]
        theta = betas[-2]
        beta = betas[:-2]
        zi = self.my_lindley(y, theta).ravel()

        eta = np.dot(X, beta)
        mu = np.exp(eta)*zi
        p = 1 / (1 + mu * theta / alpha)
        q = 1 - p
        score = np.zeros(len(betas))

        for i in range(len(y)):
            score += (psi(y[i] + zi[i] * p[i]) - psi(alpha * p[i]) + np.log(zi[i])
                      - np.log(1 + zi * mu[i] / alpha)) * X[i, :]

        return score

    def poisson_lognormal_glm_score(self, betas, Y, X, sigma, tau=1e-6):
        """
        Implements the Poisson-lognormal GLM and returns the log-likelihood
        function and its gradient with respect to beta and sigma.

        Args:
        - Y: numpy array of shape (n,), observed counts
        - X: numpy array of shape (n,p), predictor variables
        - beta: numpy array of shape (p,), regression coefficients
        - sigma: float, dispersion parameter
        - tau: float, precision parameter

        Returns:
        - log_likelihood: float, the log-likelihood function
        - gradient: numpy array of shape (p+1,), the gradient of the log-likelihood
        function with respect to beta and sigma
        """

        # Calculate the mean counts
        beta = betas[:-1]
        mu = np.exp(np.dot(X, beta))

        # Calculate the log-likelihood function
        log_likelihood = np.sum(poisson.logpmf(Y, mu))
        log_likelihood -= np.sum(np.log(np.arange(1, Y.max()+1)))
        log_likelihood -= Y.size/2*np.log(2*np.pi) + Y.size/2*np.log(sigma**2)
        log_likelihood -= 1/(2*tau**2)*np.log(sigma**2)
        print(log_likelihood)
        # Calculate the residuals
        epsilon = np.nan_to_num(np.log(Y.ravel()/mu) -
                                np.log(sigma), nan=tau, neginf=-5, posinf=5)

        # Calculate the gradient of the log-likelihood function
        gradient = np.zeros(len(betas))
        grad_n_sub = (Y.ravel() - mu.ravel())[:, None] * X
        gradient[:-1] = np.dot(X.T, Y.ravel() - mu)
        gradient[-1] = np.sum(epsilon**2 - 1)/sigma
        grad_n_sub1 = np.atleast_2d((epsilon**2 - 1)/sigma).T
        grad_n = np.concatenate((grad_n_sub, grad_n_sub1), axis=1)
        return gradient, grad_n

    def NB_Score(self, params, y, mu, X, Q=0, obs_specific=False):
        """
        Negative Binomial model score (gradient) vector of the log-likelihood
        Parameters
        ----------
        params : array_like
            The parameters of the model
            params[-1]: is the dispersion paramaters
        y: vector of true counts N long
        mu: vector of predicted counts : N longe
        X: matrix of explanatory variables len N* (D-1)
        Returns
        -------
        score : ndarray, 1-D
            The score vector of the model, i.e. the first derivative of the
            loglikelihood function, evaluated at `params`


        """

        try:

            alpha = params[-1]
            a1 = 1 / alpha * mu ** Q
            prob = a1 / (a1 + mu)
            exog = X
            if Q == 1:  # nb1
                # Q == 1 --> a1 = mu / alpha --> prob = 1 / (alpha + 1)
                dgpart = sc.digamma(y + a1) - sc.digamma(a1)
                dparams = exog * a1 * (np.log(prob) +
                                       dgpart)
                dalpha = ((alpha * (y - mu * np.log(prob) -
                                    mu * (dgpart + 1)) -
                           mu * (np.log(prob) +
                                 dgpart)) /
                          (alpha ** 2 * (alpha + 1))).sum()
            elif Q == 0:  # nb2
                dgpart = sc.digamma(y + a1) - sc.digamma(a1)
                dparams = exog * a1[:,:,:] * (y[:,:,:] - mu[:,:,:]) / (mu[:,:,:] + a1[:,:,:])
                #dparams2 = exog[:,0,:] * np.atleast_2d(a1[:,0] * (y[:,0] - mu[:,0]) / (mu[:,0] + a1[:,0])).transpose()
                da1 = -alpha ** -2
                if obs_specific:
                    dalpha = (dgpart + np.log(a1)
                              - np.log(a1 + mu) - (y - mu) / (a1 + mu)) * da1

                else:
                    dalpha = (dgpart + np.log(a1)
                              - np.log(a1 + mu) - (y - mu) / (a1 + mu)).sum(0) * da1
            else:
                raise Exception
            if obs_specific is False:
                #return np.r_[dparams.sum(0), dalpha[:, None]]
                dparams = dparams.sum(axis = 1)
                dalpha = dalpha.sum(axis = 0)
                return np.r_[dparams.sum(0), dalpha]
                dparams2 = dparms.sum(axis = 1)
                dalpha1 =dalpha[:,None].sum(axis = 1)
                return np.concatenate((dparams.sum(0),dalpha[:, None]), axis = 1)
            else:
                dparams = dparams.sum(axis = 1)
                dalpha = dalpha.sum(axis = 1)
                return np.concatenate((dparams, dalpha),
                                      axis=1)
        except Exception as e:
            print('in ki nb probkemng')
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            raise Exception

    def NB_score_lindley(self, params, y, mu, X, Q=0, obs_specific=False):
        """
        Calculate the score (gradient) vector of the Negative Binomial-Lindley log-likelihood
        Parameters
        ----------
        params : array_like
            The parameters of the model
            params[-1]: is the dispersion parameter
        y: array_like
            Vector of true counts N long
        mu: array_like
            Vector of predicted counts N long
        X: array_like
            Matrix of explanatory variables len N* (D-1)
        a: float or None, optional
            Optional parameter, if not None the function calculates the score for the NB-Lindley model with Lindley parameter a,
            otherwise, it calculates the score for the Negative Binomial model.
        Returns
        -------
        score : ndarray, 1-D
            The score vector of the model, i.e. the first derivative of the
            loglikelihood function, evaluated at `params`
        """

        alpha = params[-1]
        a = params[-2]
        a1 = 1 / alpha * mu
        prob = a1 / (a1 + mu)
        exog = X

        # Calculate the score of the Negative Binomial model
        dgpart = sc.digamma(y + alpha * mu) - sc.digamma(alpha * mu)
        dparams = exog * alpha * (np.log(prob) + dgpart)
        dalpha = ((alpha * (y - mu * np.log(prob) -
                            mu * (dgpart + 1)) -
                   mu * (np.log(prob) +
                         dgpart)) /
                  (alpha ** 2 * (alpha + 1)))

        # If a is not None, calculate the score of the NB-Lindley model
        if a is not None:
            a1 = (1 + a) / (alpha + a + mu)
            prob = a1 / (a1 + mu)
            dgpart = sc.digamma(y + alpha * mu + a) - \
                sc.digamma(alpha * mu + a)
            dparams_lindley = exog * (alpha + a) * (np.log(prob) + dgpart)
            dalpha_lindley = (((alpha + a) * (y - mu * np.log(prob) -
                                              mu * (dgpart + 1)) -
                               mu * (np.log(prob) +
                                     dgpart)) /
                              ((alpha + a) ** 2 * (alpha + a + 1)))

            if obs_specific is False:
                return np.r_[dparams.sum(0), dalpha_lindley.sum(), dalpha.sum()]
                return np.r_[dparams.sum(0) + dparams_lindley.sum(0), dalpha_lindley.sum(), dalpha.sum()]
            else:
                return np.concatenate((dparams, dalpha_lindley, dalpha), axis=1)
                return np.concatenate((dparams + dparams_lindley, dalpha_lindley, dalpha), axis=1)
            return np.r_[dparams.sum(0), dalpha, dparams_lindley.sum(0), dalpha_lindley]

        else:
            return np.r_[dparams.sum(0), dalpha]

    def PoissonNegLogLikelihood(self, lam, y, penalty=0, X=None):
        """computers the negative log-likelihood for a poisson random variable"""
        limit = 1e-6
        log_lik = 0
        if lam.shape != y.shape:
            print('the shape of y is', y.shape)
            print('the shape of lam is', lam.shape)
            print('inconsitances')
            if lam.shape != y.shape:
                print('major error, problem with size')
        if X is not None:
            a = len(X)
            yy = y.reshape(a, self.Ndraws)
            lamer = lam.reshape(a, self.Ndraws)
            yy = yy.mean(axis=1)
            lamer = lamer.mean(axis=1)
            der = X.T @ (yy - lamer)
            # print(der)
        prob = poisson.pmf(y, lam)
        # print(prob.shape, 'poisson')
        prob = prob.reshape(self.observations, -1, order='F')
        argument = prob.mean(axis=1)
        # if less than 0 penalise
        if np.min(argument) < 0:
            print('what the fuck')
        if np.min(argument) < limit:
            # add a penalty for too small argument of log
            log_lik += -np.sum(np.minimum(0.0, argument - limit)) / limit
            #penalty +=  np.sum(np.minimum(0.0, argument - limit)) / limit
            # keep argument of log above the limit
            argument = np.maximum(argument, limit)
        log_lik += np.sum(np.log(argument))
        # if penalty is not None:
        #    log_lik += -penalty
        '''return log_like at possitive to ensure minimisation'''
        if isinstance(log_lik, (list, np.ndarray)):
            log_lik = log_lik[0]
        #print('log_lik poisson', log_lik)
        return -log_lik

    def convert_nbinom_params(self, mu, theta):
        """
            Convert mean/dispersion parameterization of a negative binomial to the ones scipy supports
            See https://en.wikipedia.org/wiki/Negative_binomial_distribution#Alternative_formulations
            """
        r = theta
        var = mu + 1 / r * mu ** 2
        p = (var - mu) / var
        return r, p

    def convert_nbinom_l_params(self, mu, theta, ltheta):
        r = theta
        var = mu + 1 / r * mu ** 2
        p = (var - mu) / var
        p = np.exp(-ltheta)
        return r, p

    def negative_binomial_lindley_pmf(self, y, r, theta2, mu):
        """
        Calculate the probability mass function (PMF) of the Negative Binomial Lindley (NB-L) distribution
        for a given count y, mean lambda, dispersion r, shape alpha, and scale beta.

        Parameters:
        y (int or array-like): The count(s) of interest.
        mu (float): The mean parameter of the Negative Binomial distribution.
        r (float): The dispersion parameter of the Negative Binomial distribution.
        theta2: The shape parameter of the Lindley distribution.


        Returns:
        pmf (float or ndarray): The probability mass function evaluated at the count(s) y.
        """

        theta = self.my_lindley(y, theta2)
        mu1 = mu*theta

        var = mu1 + 1 / r * mu1 ** 2
        p = (var - mu1) / var
        numerator = math.comb(r+y.ravel()-1.0, y.ravel()
                              ) * ((theta**2)/(theta+1))
        denominator = 0
        for j in range(y+1):
            denominator += math.comb(y, j) * ((-1)**j) * \
                ((theta+r+j+1)/((theta+r+j)**2))

        please = numerator/denominator * p**y * (1-p)**r
        return please

    def negative_binomial_lindley_pmf_gradient(self, y, r, theta2, mu):
        """
        Calculate the gradient of the probability mass function (PMF) of the Negative Binomial Lindley (NB-L) 
        distribution for a given count y, mean lambda, dispersion r, shape alpha, and scale beta.

        Parameters:
        y (int or array-like): The count(s) of interest.
        mu (float): The mean parameter of the Negative Binomial distribution.
        r (float): The dispersion parameter of the Negative Binomial distribution.
        theta2: The shape parameter of the Lindley distribution.


        Returns:
        gradient (ndarray): The gradient of the probability mass function evaluated at the count(s) y.
        """

        theta = self.my_lindley(y, theta2)
        mu = mu * mu + theta
        var = mu + 1 / r * mu ** 2
        p = (var - mu) / var
        numerator = math.comb(r+y-1, y) * ((theta**2)/(theta+1))
        denominator = 0
        for j in range(y+1):
            denominator += math.comb(y, j) * ((-1)**j) * \
                ((theta+r+j+1)/((theta+r+j)**2))

        dtheta = numerator * (y*(2*theta+1) - theta*(theta+1)) / denominator**2
        dmu = (y-mu)*p/(1-p)
        dr = -r**2/var + r/var*(y-r*mu/(1-p))
        dtheta2 = theta * (y*(theta+1)/(theta+1+mu) -
                           (theta2+1)/(theta2+mu)) / denominator

        gradient = np.array([dtheta2, dmu, dr])
        return gradient

    def dnbl(self, x, r, theta):

        p = np.apply_along_axis(self, self.nbl_pmf, 0, x, r=r, theta=theta)
        return p

    def nbl_integrand(self, k, x, r, theta):
        nlogp = -np.log(x)
        tmp1 = nbinom.pmf(k, r, x)
        #tmp1 = dnbinom(k, r, x, True)
        tmp2 = -theta * nlogp
        tmp3 = 2 * np.log(theta) - np.log(1 + theta)
        tmp4 = np.log(1 + nlogp)
        y = np.exp(nlogp + tmp1 + tmp2 + tmp3 + tmp4)
        return y

    def nbl_pmf(self, x, r, theta):
        return quad(self.nbl_integrand, 0, 1, args=(x, r, theta))[0]

    def nbinom_pmf(self, counts, mu, theta):
        return nbinom.pmf(counts, *self.convert_nbinom_params(mu, theta))

    def nbinom_l_pmf(self, counts, mu, theta, ltheta):
        return nbinom.pmf(counts, *self.convert_nbinom_l_params(mu, theta, ltheta))

    def gradient(self, y, mu, X, Xr, bf, b):
        return X.T @ (y - mu)

    def NegativeBinomNegLogLikelihood(self, lam, y, p, penalty=0):
        limit = 1e-6
        log_lik = 0
        if p < 0:
            log_lik += p * 10
            p = limit
        if lam.shape != y.shape:
            print('look at this we need to transform')
        prob = self.nbinom_pmf(y, lam, p)
        prob = prob.reshape(self.observations, -1, order='F')
        # log_lik = np.sum(np.log(prob.mean(axis=1)))
        '''return log_like at possitive to ensure minimisation'''
        argument = prob.mean(axis=1)
        if np.min(argument) < limit:
            # add a penalty for too small argument of log
            log_lik += np.sum(np.minimum(0.0, argument - limit)) / limit
            #penalty +=  np.sum(np.minimum(0.0, argument - limit)) / limit
            # keep argument of log above the limit
            argument = np.maximum(argument, limit)
        log_lik += np.sum(np.log(argument))
        '''return log_like at possitive to ensure minimisation'''
        if isinstance(log_lik, (list, np.ndarray)):
            log_lik = log_lik[0]
        if isinstance(log_lik, (list, np.ndarray)):
            log_lik = log_lik[0]
        return -log_lik

    def Logspace_add(self, a, b):
        if b > a:
            log_z = b + np.log(1 + np.exp(a - b))  # , where \code{b > a}.
        else:
            log_z = b
        return log_z

    def Compute_LogZ(self, loglamba, nu):
        maxiter = int(1e4)
        logepsilon = np.log(1e-10)
        # print(loglamba[0])
        out = np.zeros(len(loglamba))
        n = len(loglamba)
        for i in range(n):
            logz = 0.0
            logz_ = 0.0
            for j in range(1, maxiter):
                # print(j)
                # print(loglamba[i])
                # potentially alpha[i] instead of nu
                logz_ = loglamba[i] - nu * np.log(j)
                # logz = self.Logspace_add(logz_, logz)
                logz = np.logaddexp(logz, logz_)
                if logz_ - logz < logepsilon:
                    # logz = 0.0
                    # logz_ =0.0
                    break
            out[i] = logz
        print('output', out)
        return out

    # p is the paramaterisation GP1 is at 0
    def general_poisson(self, mu, y, nu, p=0):  # TODO laxywhere??

        endog = y
        mu_p = np.power(mu, p)
        a1 = 1 + nu * mu_p
        a2 = mu + (a1 - 1) * endog
        a1 = np.maximum(1e-20, a1)
        a2 = np.maximum(1e-20, a2)
        return (np.log(mu) + (endog - 1) * np.log(a2) - endog *
                np.log(a1) - sc.gammaln(endog + 1) - a2 / a1)

    # takes the pmf pf the generalized poisson
    def general_poisson_pmf(self, mu, y, nu, p=0):
        return np.exp(self.general_poisson(mu, y, nu, p))

    def poisson_mle(self, data):
        """
            Compute the maximum likelihood estimate (mle) for a poisson distribution given data.
            Inputs:
            data - float or array.  Observed data.
            Outputs:
            lambda_mle - float.  The mle for poisson distribution.
            """
        mle = minimize(self.PoissonNegLogLikelihood, 1, args=(data))
        lambda_mle = mle.x[0]
        return lambda_mle

    def hessian(self, X, params):

        L = np.exp(np.dot(X, params))
        H = np.dot(L * X.T, X)
        return H

    def hessian_GP(self, params, mu, X, y, p=0):
        """
        Generalized Poisson model Hessian matrix of the loglikelihood
        Parameters
        ----------
        params : array_like
            The parameters of the model
        Returns
        -------
        hess : ndarray, (k_vars, k_vars)
            The Hessian, second derivative of loglikelihood function,
            evaluated at `params`
        """
        alpha = params[-1]
        exog = X
        mu_p = np.power(mu, p)
        a1 = 1 + alpha * mu_p
        a2 = mu + alpha * mu_p * y
        a3 = alpha * p * mu ** (p - 1)
        a4 = a3 * y
        a5 = p * mu ** (p - 1)
        dmudb = mu * exog
        # for dl/dparams dparams
        dim = exog.shape[1]
        hess_arr = np.empty((dim+1, dim+1))
        for i in range(dim):
            for j in range(i + 1):
                hess_arr[i, j] = np.sum(mu * exog[:, i, None] * exog[:, j, None] *
                                        (mu * (a3 * a4 / a1**2 -
                                               2 * a3**2 * a2 / a1**3 +
                                               2 * a3 * (a4 + 1) / a1**2 -
                                               a4 * p / (mu * a1) +
                                               a3 * p * a2 / (mu * a1**2) +
                                               (y - 1) * a4 * (p - 1) / (a2 * mu) -
                                               (y - 1) * (1 + a4)**2 / a2**2 -
                                               a4 * (p - 1) / (a1 * mu)) +
                                         ((y - 1) * (1 + a4) / a2 -
                                          (1 + a4) / a1)), axis=0)
        tri_idx = np.triu_indices(dim, k=1)
        hess_arr[tri_idx] = hess_arr.T[tri_idx]
        # for dl/dparams dalpha
        dldpda = np.sum((2 * a4 * mu_p / a1**2 -
                         2 * a3 * mu_p * a2 / a1**3 -
                         mu_p * y * (y - 1) * (1 + a4) / a2**2 +
                         mu_p * (1 + a4) / a1**2 +
                         a5 * y * (y - 1) / a2 -
                         2 * a5 * y / a1 +
                         a5 * a2 / a1**2) * dmudb,
                        axis=0)
        hess_arr[-1, :-1] = dldpda
        hess_arr[:-1, -1] = dldpda
        # for dl/dalpha dalpha
        dldada = mu_p**2 * (3 * y / a1**2 -
                            (y / a2)**2. * (y - 1) -
                            2 * a2 / a1**3)
        hess_arr[-1, -1] = dldada.sum()
        return hess_arr

  
    
    
    
    def compute_cov_gp_rp(self, Xf, Xr, draws, params, y, mu):
        try:
            K = len(params)
            X_std = np.zeros((Xf.shape[0], K, draws.shape[2]))
            Xr_long = np.repeat(Xr[:, :, np.newaxis], draws.shape[2], axis=2)
            X_std = Xr_long*draws
            hessr = np.zeros((K, K, draws.shape[2]))
            for i in range(draws.shape[2]):
                X = np.concatenate((Xf, Xr, X_std[:, :, i]), axis=1)
                mu_i = mu[:, :, i]
                hessr[:, :, i] = self.hessian_GP(params, mu_i, X, y)
            hess = hessr.mean(axis=2)
            hess_inv = self.hessian_inv(hess)
            return hess_inv
        except Exception as e:
            print(e)
            raise Exception

    def compute_cov_nb_rp(self, Xf, Xr, draws, params, y, mu):
        try:
            K = len(params)
            X_std = np.zeros((Xf.shape[0], K, draws.shape[2]))
            Xr_long = np.repeat(Xr[:, :, np.newaxis], draws.shape[2], axis=2)
            X_std = Xr_long*draws
            hessr = np.zeros((K, K, draws.shape[2]))
            for i in range(draws.shape[2]):
                X = np.concatenate((Xf, Xr, X_std[:, :, i]), axis=1)
                hessr[:, :, i] = -self._hessian_nb2(X, y, params, mu[:, :, i])
            hess = hessr.mean(axis=2)
            hess_inv = self.hessian_inv(hess)
            return hess_inv
        except Exception as e:
            print(e)
            raise Exception

    

    def _hessian_nb2(self, X, y, param, mu_s=None):
        """
        Hessian of NB2 model.
        """
        alpha = param[-1]
        a1 = 1 / alpha
        exog = X
        if mu_s is None:
            mu = self.lam
        else:
            mu = mu_s
        prob = a1 / (a1 + mu)
        dgpart = sc.digamma(a1 + y) - sc.digamma(a1)
        # for dl/dparams dparams
        dim = exog.shape[1]
        hess_arr = np.empty((dim + 1, dim + 1))
        const_arr = a1 * mu * (a1 + y) / (mu + a1) ** 2
        for i in range(dim):
            for j in range(dim):
                if j > i:
                    continue
                hess_arr[i, j] = np.sum(-exog[:, i, None] * exog[:, j, None] *
                                        const_arr, axis=0)
        tri_idx = np.triu_indices(dim, k=1)
        hess_arr[tri_idx] = hess_arr.T[tri_idx]
        # for dl/dparams dalpha
        da1 = -alpha ** -2
        dldpda = -np.sum(mu * exog * (y - mu) * a1 **
                         2 / (mu + a1) ** 2, axis=0)
        hess_arr[-1, :-1] = dldpda
        hess_arr[:-1, -1] = dldpda
        # for dl/dalpha dalpha
        # NOTE: polygamma(1,x) is the trigamma function
        da2 = 2 * alpha ** -3
        dalpha = da1 * (dgpart +
                        np.log(prob) - (y - mu) / (a1 + mu))
        dada = (da2 * dalpha / da1 + da1 ** 2 * (sc.polygamma(1, a1 + y) - sc.polygamma(1, a1) + 1 / a1 - 1 / (a1 + mu) +  # type: ignore
                                                 (y - mu) / (mu + a1) ** 2)).sum()
        hess_arr[-1, -1] = dada
        return hess_arr

    def _ll_nbin(self, y, alpha_f, Q=0, transparam=0):
        if transparam:
            alpha = np.exp(alpha_f)
        else:
            alpha = alpha_f
        endog = y
        mu = self.lam
        size = 1/alpha*mu**Q
        prob = size/(size+mu)
        coeff = (sc.gammaln(size+endog)-sc.gammaln(endog+1) - sc.gammaln(size))
        llf = coeff+size*np.log(prob) + endog*np.log(1-prob)
        return llf

    def Score_RP(self, xf, xr, lam, y, der, draws):
        der_b = xf.T @ (y-lam)
        der_b = der_b.reshape((-1,))
        der_br = (xr*der).T @ (y-lam)
        der_br = der_br.reshape((-1,))
        der_br_w = (xr*der*draws).T @ (y-lam)
        der_br_w = der_br_w.reshape((-1,))
        self.exog = np.concatenate((xf, xr*draws, xr), axis=1)
        der = np.concatenate((der_b, der_br, der_br_w), axis=0)
        der = der.reshape(len(der))
        return der

    def _estimate_covariance(self, hess_inv, grad_n, robust):
        """ Estimates covariance matrix. Allows for robust covariance estimation
        This follows the methodology lined out in p.486-488
        in the Stata 16 programming reference manual.
        Benchmarked against Stata 17.
        """
        if(robust):
            n = np.shape(grad_n)[0]
            # subtract out mean gradient value
            grad_n_sub = grad_n-(np.sum(grad_n, axis=0)/n)
            inner = np.transpose(grad_n_sub)@grad_n_sub
            correction = ((n)/(n-1))
            covariance = correction*(hess_inv@inner@hess_inv)
            return covariance
        else:
            covariance = hess_inv
        return covariance

    def _numerical_hessian(self, betas, args, jac):
        Xd, y, draws, Xf, Xr, corr_list, dispersion = args
        def loglike(p): return self._loglik_gradient(
            p, Xd, y, draws, Xf, Xr, None, False, False, dispersion, corr_list=corr_list)
        hess = approx_hess(betas, loglike)
        hess_inv1 = np.linalg.pinv(hess)
        hess = self._hessian_prot(betas, loglike)
        hess = np.nan_to_num(hess)
        hess_inv = np.linalg.pinv(hess)
        return hess_inv

    def _chol_mat(self, correlationLength, br, Br_w, correlation):
        # if correlation = True correlation pos is randpos, if list get correct pos
        dont_run = 0
        if dont_run:
            correlationpos = []
            varnames = ['a', 'b', 'c', 'd', 'e', 'f']
            varnames = np.asarray(varnames)
            randvars = ['c', 'd', 'e', 'f']
            correlation = ['e', 'f']
            if randvars:
                # Position of correlated variables within randvars
                correlationpos = [varnames.tolist().index(x)
                                  for x in varnames if x in randvars]
            if (isinstance(correlation, list)):
                self.correlationpos = [varnames.tolist().index(x) for x in
                                       varnames if x in correlation]
                self.uncorrelatedpos = [varnames.tolist().index(x) for x in
                                        varnames if x not in correlation]
            # if correlation = True correlation pos is randpos, if list get correct pos
            correlationpos = []
        else:
            varnames = self.none_handler(
                self.rdm_fit) + self.none_handler(self.rdm_cor_fit)

        if (isinstance(correlation, list)):
            # Kchol, permutations of specified params in correlation list
            Kchol = int((len(correlation) *
                         (len(correlation)+1))/2)
        else:
            # i.e. correlation = True, Kchol permutations of random paramaters
            Kchol = int((len(br) * (len(br)+1))/2)

        # creating cholesky matrix for the variance-covariance matrix
        # all random variables not included in correlation will only
        # have their standard deviation computed
        chol_mat = np.zeros((correlationLength, correlationLength))
        indices = np.tril_indices(correlationLength)
        if dev.using_gpu:
            Kchol = dev.to_cpu(Kchol)
            chol_mat[indices] = Kchol  # TODO? Better
        else:
            chol_mat[indices] = Kchol

        
        #chol  = np.abs(Br_w[-Kchol:]) this was abs, but i don't need it
        chol = Br_w[-Kchol:]
        br_w = Br_w[:-Kchol]

        chol_mat_temp = np.zeros((len(br), len(br)))  # number of kr

        # new naminging TODO: probably broken
        rv_count = 0
        rv_count_all = 0
        corr_indices = []
        chol_count = 0
        for ii, var in enumerate(varnames):  # TODO: BUGFIX
            if var in self.none_handler(self.rdm_cor_fit):
                is_correlated = True
            else:
                is_correlated = False
            rv_val = chol[chol_count] if is_correlated else br_w[rv_count]
            chol_mat_temp[rv_count_all, rv_count_all] = rv_val
            rv_count_all += 1
            if is_correlated:
                chol_count += 1
            else:
                rv_count += 1

            if var in self.rdm_cor_fit:

                corr_indices.append(rv_count_all - 1)  # TODO: what does tis do

        # TODO i think
        if self.rdm_cor_fit is None:  # TODO when all_corralted or nonee
            corr_pairs = list(itertools.combinations(self.Kr, 2))
        else:
            corr_pairs = list(itertools.combinations(corr_indices, 2))

        for ii, corr_pair in enumerate(corr_pairs):
            # lower cholesky matrix
            chol_mat_temp[tuple(reversed(corr_pair))] = chol[chol_count]
            chol_count += 1

        chol_mat = chol_mat_temp

        if dev.using_gpu:
            chol_mat = dev.to_gpu(chol_mat)

        omega = np.matmul(chol_mat, np.transpose(chol_mat))
        corr_mat = np.zeros_like(chol_mat)
        standard_devs = np.sqrt(np.diag(np.abs(omega)))
        K = len(standard_devs)
        for i in range(K):
            for j in range(K):
                corr_mat[i, j] = omega[i, j] / \
                    (standard_devs[i] * standard_devs[j])

        stdevs = standard_devs

        return chol_mat

    def _transform_hetro_betas(self, betas_hetro, betas_hetro_sd, draws_hetro, list_sizes):
        a = 0
        b = 0
        stuff = [] 
        #todo get order
        for j, i in enumerate(list_sizes):
            br_mean = betas_hetro[a:i+a]
            a +=i
            
            betas_random = br_mean[None, :, None] + draws_hetro[:,j,None, :]*betas_hetro_sd[None, j, None, None]
            stuff.append(betas_random)
        return stuff    

    
    def _transform_rand_betas(self, betas_m, betas_sd, draws):
        """Compute the products between the betas and the random coefficients.
    This method also applies the associated mixing distributions
    """

        br_mean = betas_m
        br_sd = betas_sd  # Last Kr positions
    # Compute: betas = mean + sd*draws
        betas_random = br_mean[None, :, None] + draws*br_sd[None, :, None]
        #betas_random = self._apply_distribution()

        return betas_random

    def _nonlog_nbin(self, y, lam, gamma, Q=0):
        """generates non_loged probabilities
        Args:
            y (_type_): _description_
            lam (_type_): _description_
            gamma (_type_): _description_
            Q (int, optional): _description_. Defaults to 0.
        Returns:
            _type_: _description_
        """
       
        if gamma <= 0.01:
            gamma = 0.01

        endog = y
        mu = lam
        alpha = gamma
        size = 1.0/alpha*mu**Q
        alpha_size = alpha*mu**Q
        #prob = size/(size+mu)
        prob = alpha/(alpha+mu)
        #prob = 1/(1+mu*alpha)
        try:
            #print(np.shape(y),np.shape(size), np.shape(prob))
           # gg2 = self.negbinom_pmf(alpha_size, prob, y)
           # gg1 = self.negbinom_pmf(size, prob, y)
            gg = nbinom.pmf(y ,alpha, prob)
            
        except Exception as e:
            print(e)
        return gg

    def lindley_pmf(self, x, r, theta, k=50):
        """
        Computes the PMF of the Lindley distribution.

        Parameters:
            x (int): the value of the random variable.
            r (float): the rate dispersion parameter.
            theta (float): the Lindley parameter.
            k (int): the maximum value of the summation in the PMF. Defaults to 50.

        Returns:
            float: the probability mass function evaluated at x.
        """
        k = x
        term1 = (theta**2 / (theta+1)) * sc.comb(r+x-1, x)
        term2 = 0
        for j in range(k+1):
            term2 += sc.comb(k, j) * (-1)**(j*((theta+r+j+1)/(theta+r+j)**2))
        return term1 * term2.real

    def _nonlog_nbin_lindley(self, y, lam, gamma, lindley, Q=0):
        """generates non_loged probabilities
        Args:
            y (_type_): _description_
            lam (_type_): _description_
            gamma (_type_): _description_
            Q (int, optional): _description_. Defaults to 0.
        Returns:
            _type_: _description_
        """
        if gamma <= 0.000001:
            gamma = 0.000001

        endog = y
        mu = lam
        alpha = gamma
        size = 1/alpha*mu**Q
        prob = size/(size+mu)
        try:
            #print(np.shape(y),np.shape(size), np.shape(prob))

            gg2 = self.lindley_pmf(y, size, lindley)
        except Exception as e:
            print(e)
        return gg2

    def nbinom_pmf_batched(self, y, lam, gamma, Q=0, batch_size=1000):
        """
        Compute the negative binomial PMF for large datasets by processing the data in batches.

        Args:
            y (array_like): The number of successes in each trial.
            size (array_like): The number of failures before the experiment is stopped.
            prob (array_like): The probability of success in each trial.
            batch_size (int): The size of each batch.

        Returns:
            array: The negative binomial PMF for the given parameters.
        """

        if gamma <= 0.000001:
            gamma = 0.000001

        endog = y
        mu = lam
        alpha = gamma
        alpha = alpha*mu**Q
        size = 1/alpha*mu**Q  # also r
       # self.rate_param = size
        prob = size/(size+mu)
        prob = gamma/(gamma +mu) #added the 1 divides

        # Divide data into smaller chunks
        num_batches = int(np.ceil(y.shape[0] / batch_size))

        # Process each batch separately
        results = []
        for i in range(num_batches):
            start_idx = i * batch_size
            end_idx = min((i + 1) * batch_size, y.shape[0])
            y_batch = y[start_idx:end_idx]
            size_batch = size[start_idx:end_idx]
            prob_batch = prob[start_idx:end_idx]
            
            alpha_batch = alpha[start_idx:end_idx]
            #batch_result = nbinom.pmf(y_batch, size_batch, prob_batch)
            #batch_resul1t = nbinom.pmf(y_batch, alpha_batch, prob_batch) #this defs works
            batch_result = self.negbinom_pmf(alpha_batch, prob_batch, y_batch)
            #batch_result = self.negbinom_pmf(size_batch, prob_batch, y_batch)
            #print(1)
            #t2 = timeit.timeit(lambda:self.negbinom_pmf(size_batch, prob_batch, y_batch), number =10000)
            #t1 = timeit.timeit(lambda:nbinom.pmf(y_batch, size_batch, prob_batch), number =10000)

            results.append(batch_result)

        # Merge results from each batch into a final result
        final_result = np.concatenate(results)

        return final_result

    def general_poisson_batched(self, lam, y, gamma, batch_size=100):
        """
        Compute the negative binomial PMF for large datasets by processing the data in batches.

        Args:
            y (array_like): The number of successes in each trial.
            size (array_like): The number of failures before the experiment is stopped.
            prob (array_like): The probability of success in each trial.
            batch_size (int): The size of each batch.

        Returns:
            array: The negative binomial PMF for the given parameters.
        """

        if gamma <= 0.000001:
            gamma = 0.000001

        # Divide data into smaller chunks
        num_batches = int(np.ceil(y.shape[0] / batch_size))

        # Process each batch separately
        results = []
        for i in range(num_batches):
            start_idx = i * batch_size
            end_idx = min((i + 1) * batch_size, y.shape[0])
            y_batch = y[start_idx:end_idx]
            lam_batch = lam[start_idx:end_idx]

            batch_result = self.general_poisson_pmf(lam_batch, y_batch, gamma)

            results.append(batch_result)

        # Merge results from each batch into a final result
        final_result = np.concatenate(results)

        return final_result

    def _der_poisson(self, k, mu):
        return np.exp(-mu)*mu(k+1)/(sc.factorial(k))

    def _penalty_dispersion(self, dispersion, b_gam, eVd, y, penalty=0.0, model_nature = None):

        if dispersion == 1 or dispersion == 4:  # nb
            if model_nature is not None and 'dispersion_penalty' in model_nature:
                if b_gam < 0.8*model_nature['dispersion_penalty']:
                    penalty +=  model_nature['dispersion_penalty'] -b_gam
            
            
            
            if abs(b_gam) < 0.05:
                penalty += 1/abs(b_gam)
                
            
            if b_gam < 0:
                penalty += 100
                 
            if b_gam >= 100:
                penalty += 100
                b_gam = 99
                
                   # penalty +=  model_nature['dispersion_penalty'] -b_gam
                    #penalty += 1/np.max((0.01,abs(b_gam)))
                   # b_gam = model_nature['dispersion_penalty']
                   
                    
            """
            if b_gam <= 0:
                #penalty += 100
                #penalty += abs(b_gam)
                #penalty += abs(b_gam)
                #b_gam = 1

                # if b_gam < 0.03:
                penalty += 10

                b_gam = 0.03
                #
            
            if b_gam >= 10:
                penalty+= b_gam   
                
            if b_gam == 0:
                b_gam = min_comp_val
            #b_gam = 0.03

            b_gam = abs(b_gam)
            
                """
            
        elif dispersion == 2:
            if b_gam >= 1:
                penalty += 10*b_gam
                b_gam = 0.99
            
            elif b_gam <= -1:
                penalty += abs(b_gam)*100
                b_gam = -0.25
            
            
            
            
        #b_gam = -.3

        penalty = 0
        return penalty, b_gam

   
    def eXB_calc(self, params_main, Xd, offset, dispersion, b_gam=None):
        
        #print('this was 0')
        eta = np.dot(Xd, params_main)[:,:,None]+np.array(offset[:,:,:])
        eta  = np.float64(eta)
        #eta = np.dot(Xd, params_main)+offset[:,:,0]
        #eta2 = np.dot(Xd, params_main)[:,:,None]+np.array(offset[:,:,:])
            
        if dispersion == 5:
            get_lindley = b_gam
            if b_gam == 0:
                get_lindley = 0.01
            eps_i = self.my_lindley(Xd, get_lindley)
            eVd = eps_i*np.exp(np.clip(eta, 0, EXP_UPPER_LIMIT)).ravel()
            #Vd = self.my_lindley(np.exp(np.clip(eta, 0, EXP_UPPER_LIMIT)), get_lindley)

            #eVd = np.exp(np.clip(eta, 0, EXP_UPPER_LIMIT))
            # eVd = self.my_lindley(np.exp(np.clip(eta, None, EXP_UPPER_LIMIT)), 1) #todo grab param
        else:
            #eVd = self.my_lindley(np.exp(np.clip(eta, None, EXP_UPPER_LIMIT)), 1.29)
            
            try:
                eta_clip = np.clip(np.array(eta), np.float64(-1000.0), EXP_UPPER_LIMIT)
                eVd = np.exp(eta_clip)
            except Exception as e:
                traceback.print_exc()
                eVd = np.exp(eta)
                
           # eVd = np.exp(eta), 0, EXP_UPPER_LIMIT
        return eVd

    def ZeroInflated(self, betas, exog, exog_infl, exposure, k_inflate, offset, y_values, return_grad=True):
        from scipy._lib._util import _lazywhere
        from statsmodels.discrete.discrete_model import Logit
        self.k_inflate = k_inflate
        self.exog = exog.to_numpy()
        self.endog = y_values.values.ravel()
        exog = exog.to_numpy()
        exog_infl = exog_infl.to_numpy()

        def _argcheck(self, mu, alpha, p):
            return (mu >= 0) & (alpha == alpha) & (p > 0)

        def loglik_obs_poisson(params, y):
            """
            Loglikelihood for observations of Poisson model

            Parameters
            ----------
            params : array_like
                The parameters of the model.

            Returns
            -------
            loglike : array_like
                The log likelihood for each observation of the model evaluated
                at `params`. See Notes

            Notes
            -----
            .. math:: \\ln L_{i}=\\left[-\\lambda_{i}+y_{i}x_{i}^{\\prime}\\beta-\\ln y_{i}!\\right]

            for observations :math:`i=1,...,n`
            """
            offset = getattr(self, "offset", 0)
            exposure = getattr(self, "exposure", 0)
            XB = np.dot(self.exog, params) + offset + exposure

            #np.sum(stats.poisson.logpmf(endog, np.exp(XB)))
            return -np.exp(XB) + y*XB - sc.gammaln(y+1)

        def loglik_zi(params, return_grad=False):
            """
            Loglikelihood for observations of Generic Zero Inflated model.

            Parameters
            ----------
            params : array_like
                The parameters of the model.

            Returns
            -------
            loglike : ndarray
                The log likelihood for each observation of the model evaluated
                at `params`. See Notes for definition.

            Notes
            -----
            .. math:: \\ln L=\\ln(w_{i}+(1-w_{i})*P_{main\\_model})+
                \\ln(1-w_{i})+L_{main\\_model}
                where P - pdf of main model, L - loglike function of main model.

            for observations :math:`i=1,...,n`
            """
            params_infl = params[:self.k_inflate]
            params_main = params[self.k_inflate:]

            y = self.endog
            w = predict_logit(params_infl, exog_infl)

            w = np.clip(w, np.finfo(float).eps, 1 - np.finfo(float).eps)
            llf_main = loglik_obs_poisson(params_main, y)
            dispersion = 0
            b_gam = None
            Xd = exog
            eta = np.tile(np.dot(Xd, params_main), (1, 1)).transpose()
            eVd = np.exp(np.clip(eta, None, EXP_UPPER_LIMIT))

            llf_main_og = self.loglik_obs(y, eVd.ravel(), dispersion, b_gam)
            zero_idx = np.nonzero(y == 0)[0]
            nonzero_idx = np.nonzero(y)[0]  # type: ignore

            llf = np.zeros_like(y, dtype=np.float64)
            llf[zero_idx] = (np.log(w[zero_idx] +
                                    (1 - w[zero_idx]) * np.exp(llf_main[zero_idx])))
            llf[nonzero_idx] = np.log(
                1 - w[nonzero_idx]) + llf_main[nonzero_idx]
            if return_grad:
                score_main = Xd.T @ (y-eVd.ravel())
                L = np.exp(np.dot(Xd, params_main))
                score_main = (self.endog - L)[:, None] * Xd

                dldp = np.zeros(
                    (exog.shape[0], len(params_main)), dtype=np.float64)
                dldw = np.zeros_like(exog_infl, dtype=np.float64)

                dldp[zero_idx, :] = (score_main[zero_idx].T *
                                     (1 - (w[zero_idx]) / np.exp(llf[zero_idx]))).T
                dldp[nonzero_idx, :] = score_main[nonzero_idx]

                dldw[zero_idx, :] = (exog_infl[zero_idx].T * w[zero_idx] *
                                     (1 - w[zero_idx]) *
                                     (1 - np.exp(llf_main[zero_idx])) /
                                     np.exp(llf[zero_idx])).T
                dldw[nonzero_idx, :] = -(exog_infl[nonzero_idx].T *
                                         w[nonzero_idx]).T

                return llf, np.hstack((dldw, dldp)).sum(axis=0)

            else:

                return llf

        def _predict_prob_zi(self, params, exog, exog_infl, exposure, k_inflate, offset,
                             mu, y_values=None):
            params_infl = params[:k_inflate]
            params_main = params[k_inflate:]

            if y_values is None:
                y_values = np.atleast_2d(np.arange(0, np.max(self.endog)+1))

            if len(exog_infl.shape) < 2:
                transform = True
                w = np.atleast_2d(
                    loglik_logit(params_infl, exog_infl, y_values))[:, None]
            else:
                transform = False
                w = loglik_logit(params_infl, exog_infl, y_values)[:, None]

            w = np.clip(w, np.finfo(float).eps, 1 - np.finfo(float).eps)

            result = zipoisson_pmf(y_values, mu, w)  # t
            return result[0] if transform else result

        def zipoisson_logpmf(x, mu, w):
            return _lazywhere(x != 0, (x, mu, w),
                              (lambda x, mu, w: np.log(1. - w) + x * np.log(mu) -
                               sc.gammaln(x + 1.) - mu),
                              np.log(w + (1. - w) * np.exp(-mu)))

        def zipoisson_pmf(x, mu, w):
            return np.exp(zipoisson_logpmf(x, mu, w))

        def loglik_logit(params, endog_y, exog_x):  # this is predict I think
            q = 2*endog_y - 1
            X = exog_x
            return np.sum(np.log(cdf(q*np.dot(X, params))))

        def predict_logit(params, exog=None, linear=False):
            if exog is None:
                exog = self.exog
            if not linear:
                return (cdf(np.dot(exog, params)))
            else:
                return (np.dot(exog, params))

        def cdf(X):
            """
            The logistic cumulative distribution function

            Parameters
            ----------
            X : array_like
                `X` is the linear predictor of the logit model.  See notes.

            Returns
            -------
            1/(1 + exp(-X))

            Notes
            -----
            In the logit model,

            .. math:: \\Lambda\\left(x^{\\prime}\\beta\\right)=
                    \\text{Prob}\\left(Y=1|x\\right)=
                    \\frac{e^{x^{\\prime}\\beta}}{1+e^{x^{\\prime}\\beta}}
            """
            X = np.asarray(X)
            return 1/(1+np.exp(-X))

        llobs, grad = loglik_zi(betas, return_grad)
        llf = np.sum(llobs)
        if return_grad:
            return -llf, -grad
        else:
            return -llf

    def cdf_logit(self, X):
        """
        The logistic cumulative distribution function

        Parameters
        ----------
        X : array_like
            `X` is the linear predictor of the logit model.  See notes.

        Returns
        -------
        1/(1 + exp(-X))

        Notes
        -----
        In the logit model,

        .. math:: \\Lambda\\left(x^{\\prime}\\beta\\right)=
                \\text{Prob}\\left(Y=1|x\\right)=
                \\frac{e^{x^{\\prime}\\beta}}{1+e^{x^{\\prime}\\beta}}
        """
        X = np.asarray(X)
        return 1/(1+np.exp(-X))

    def predict_logit_part(self, params_infl, exog_infl, linear=False):

        if not linear:
            return (self.cdf_logit(np.dot(exog_infl, params_infl)))
        else:
            return (np.dot(exog_infl, params_infl))

   

    def ZeroInflate_W_setup(self, exog_infl, y, params_infl):

        w = self.predict_logit_part(params_infl, exog_infl)

        w = np.clip(w, np.finfo(float).eps, 1 - np.finfo(float).eps)

        llf_main = [1, 2, 3]  # TODO ge
        zero_idx = np.nonzero(y == 0)[0]
        nonzero_idx = np.nonzero(y)[0]

        llf = np.zeros_like(y, dtype=np.float64)
        llf[zero_idx] = (np.log(w[zero_idx] +
                                (1 - w[zero_idx]) * np.exp(llf_main[zero_idx])))
        llf[nonzero_idx] = np.log(1 - w[nonzero_idx]) + llf_main[nonzero_idx]

        return llf

    def dPXL(self, x, alpha):
        return ((alpha**2) * (x + 3*alpha + (alpha**2) + 3)) / (1 + alpha)**(4 + x)


# Define the gradient function


    def poisson_lindley_gradient(self, params, exog, endog):
        beta = params[-1]
        mu = np.exp(np.dot(exog, params[:-1]))
        q = beta / (1 + beta)
        d_beta = (endog.ravel()+1)/(mu+endog.ravel()+1) - q/(1-q)
        d_beta = self.dpoisl(endog, beta).ravel()
        d_mu = np.dot((endog - mu) * (1 - q) / (mu + endog + 1), exog)

        grad_n = np.concatenate((d_mu, np.atleast_2d(d_beta).T), axis=1)
        der = np.sum(grad_n, axis=0)
        return der, grad_n

    def dpoisl(self, x, theta, log=False):
        # if theta < 0:
        #    raise ValueError("theta must be positive!")
        p = (theta**2 * (x + theta + 2)/(theta + 1)**(x + 3)) * (x >= 0)
        if log:
            p = np.log(p)
        p = np.nan_to_num(p)
        #p[np.isnan(p)] = 0
        if not log:
            p = np.clip(p, 0, 1)
        return p

    def dnegbimonli(self, y, mu, alpha):
        gamma_term = math.gamma(y+alpha) / \
            (math.gamma(y+1) * math.gamma(alpha))
        prob = gamma_term * (alpha/(alpha+mu))**alpha * (mu/(alpha+mu))**y
        return prob

    def none_join(self, list_of_lists):
        joinedlist = []
        for i in list_of_lists:
            if i is not None:
                joinedlist = joinedlist + i
        return joinedlist

    def none_handler(self, stuff):
        if stuff is None:
            return []
        else:
            return stuff

   

    def GPL_lik(self, par, y, eVd):
        a = par[0]
        t = par[1]
        n = len(y)
        k = len(par) - 1
        b = par[:k]
        t = par[k]
        #niu = np.dot(X, b)
        niu = eVd
        test = ((len(y) * np.log(t/(t+1))) + (np.sum(np.log(sc.gamma(y + (((eVd)*t*(t+1)-1)/(t+1)))) - np.log(sc.gamma(1+(((eVd)*t*(t+1)-1)/(t+1)))))) - (np.sum(np.log(sc.factorial(y)))
                                                                                                                                                          ) + (np.sum((((eVd)*t*(t+1)-1)/(t+1))*np.log(t/(t+1)))) - (np.sum((y+1)*np.log(t+1))) + (np.sum(np.log(((eVd)*t*(t+1))-1+y+((((eVd)*t*(t+1))-1)/(t+1))))))
        return ((len(y) * np.log(t/(t+1))) + (np.sum(np.log(sc.gamma(y + (((np.exp(niu))*t*(t+1)-1)/(t+1)))) - np.log(sc.gamma(1+(((np.exp(niu))*t*(t+1)-1)/(t+1)))))) - (np.sum(np.log(sc.factorial(y)))) + (np.sum((((np.exp(niu))*t*(t+1)-1)/(t+1))*np.log(t/(t+1)))) - (np.sum((y+1)*np.log(t+1))) + (np.sum(np.log(((np.exp(niu))*t*(t+1))-1+y+((((np.exp(niu))*t*(t+1))-1)/(t+1))))))



    def loglik_obs(self, y, eVd, dispersion, b_gam, l_pam=None, betas=None):
        if type(y) == dict:
            weights = len(y)*np.atleast_2d(np.concatenate(
                [self.weights[i]*np.ones(len(v)) for i, v in enumerate(y.values())])).T
            y = np.atleast_2d(np.concatenate([v for v in y.values()])).T

        if dispersion == 0:
            proba_r = poisson.pmf(y, eVd)

        #  proba_r = self.dpoisl(y, eVd)
        elif dispersion == 1:

            proba_r = self._nonlog_nbin(y, eVd, b_gam)

            #proba_d = self.dnegbimonli(y, eVd, b_gam )
       # print('fuck if this actually works')

        elif dispersion == 2:

            proba_r = self.general_poisson_pmf(eVd, y, b_gam)

        elif dispersion == 3:
            fa, ba = self.get_dispersion_paramaters(betas, dispersion)
            zi = self.my_lindley(y, ba)
            proba_r = poisson.pmf(y, zi*eVd.ravel())
            #proba_r = self.lindl_pmf_chatgpt(y, l_pam)
            #prob_2 = self.dpoisl(y, l_pam)
            #proba_r = self.poisson_lindley_pmf(eVd, l_pam, y)
            #proba_r = self.poisson_lindley_pmf(eVd, l_pam, y)
            # print(1)
            #proba_r = self.dpoisl(y, eVd)

        elif dispersion == 4:
            fa, ba = self.get_dispersion_paramaters(betas, dispersion)
            self.zi = self.my_lindley(eVd, ba)
            proba_r = self._nonlog_nbin(y, eVd+self.zi, b_gam)
       # proba_r = self._nonlog_nbin_lindley(y, eVd, fa, ba)

        elif dispersion == 'poisson_lognormal':
            sig, vl = self.get_dispersion_paramaters(betas, dispersion)
            store = list()
            for i in range(len(y)):
                store.append(self.poisson_lognormal_pmf(
                    y[i][0], eVd[i][0], sig))

            #proba_r = self.poisson_lognormal_pmf(y, eVd, sig)
            proba_r = np.array(store)
            proba_r = np.atleast_2d(proba_r).T
            print(1)

        else:
            raise Exception('not implemented other modeling forms')
        
        if self.panels is not None:
            proba_p = self._prob_product_across_panels(
                    proba_r, self.panel_info)
            proba_r = proba_p
        proba_r = np.clip(proba_r, min_comp_val, None)
        loglik = np.log(proba_r)
        return loglik

    def is_dispersion(self, dispersion):
        if dispersion == 0 or dispersion == 3:
            return 0
        else:
            return 1

    def _prob_product_across_panels(self, pch, panel_info):
        if not np.all(panel_info):  # If panels unbalanced. Not all ones
            idx = panel_info == 0
            for i in range(pch.shape[2]):
                pch[:, :, i][idx] = 1  # Multiply by one when unbalanced
        pch = pch.prod(axis=1)  # (N,R)
        pch[pch == 0] = min_comp_val
        return pch
        
        
        
        if panels is not None:
            idx = np.concatenate(
                ([0], np.where(panels[:-1] != panels[1:])[0] + 1, [len(prob)]))
            prob2 = dev.np.vstack([prob[idx[i]:idx[i+1]].prod(axis=0)
                                  for i in range(len(idx) - 1)])
            prob = prob2.copy()
        return prob  # (N

    def gradient_calc_est(self, N, Kf, Kr, Kchol, dispersion, proba_n, eVd, br, brstd, draws_, Xdf, Xdr, y, R, lik, alpha=0.5, betas=None, Br=None, panels=None, model_nature = None, br_h = None, br_hs = None):

        if panels is None:
            panels = self.panels

        if alpha < 0:
            alpha = np.abs(alpha)
        sig, omeg = self.get_dispersion_paramaters(betas, dispersion)

        
        if model_nature is not None:
            if 'XH' in model_nature:
              
                Kh = self.get_num_params()[5]
                gr_h = np.zeros((N, Kh- len(model_nature.get('x_h_storage'))))
                gr_hs = np.zeros((N, len(model_nature.get('x_h_storage'))))
        else:
            gr_h = np.zeros((N, 0))
            gr_hs = np.zeros((N, 0))        

                
        
        if self.rdm_cor_fit is None:

            gr_f, gr_u, gr_s = np.zeros((N, Kf)), np.zeros(
                (N, Kr)), np.zeros((N, Kr))  # Temp batching storage
        else:

            # if (len(betas) -Kf-Kr-self.is_dispersion(dispersion)) != (Kchol + Kr):

            # gr_f, gr_u, gr_s = np.zeros((N, Kf)), np.zeros((N, Kr)), np.zeros((N, len(betas) -Kf-Kr-self.is_dispersion(dispersion))) #FIX
            Kf2, Kr, Kc, Kr_b, Kchol, Kh, zi_terms = self.get_num_params()

            gr_f, gr_u, gr_s = np.zeros((N, Kf)), np.zeros(
                (N, Kr+Kc)), np.zeros((N, Kchol + Kr_b))

        if dispersion == 3:

            q = omeg / (1 + omeg)
            d_beta = (y+1)/(eVd+y+1) - q/(1-q)
            gr_e = np.zeros(N, 1)
            gr_e = d_beta*(proba_n[:, None, :]).sum(axis=2)
            for i in len(y):
                if y[i] == 0:
                    gr_e[i] = 0

        if self.is_dispersion(dispersion):
            gr_d = np.zeros((N, 1))
            if dispersion == 1:
                # trying alt

                a1 = 1/alpha * dev.to_cpu(eVd) ** 0
                dgpart = sc.digamma(y[:, :,:] + a1) - sc.digamma(a1)
                da1 = -alpha ** -2  # this was negative

                einsum_model_form = a1 * \
                    (y[:, :, :] - dev.to_cpu(eVd)) / (dev.to_cpu(eVd) + a1)
                
                gr_d = (((dgpart + np.log(a1) - np.log(a1 + dev.to_cpu(eVd)) - (y[:, :, :] - dev.to_cpu(
                    eVd)) / (a1 + dev.to_cpu(eVd))) * da1)*(proba_n[:, None, :])).sum(axis=(1,2))
                #gr_d_test_delete = ((dgpart + np.log(a1)- np.log(a1 + dev.to_cpu(eVd)) - (y[:,:,None] - dev.to_cpu(eVd)) / (a1 + dev.to_cpu(eVd))) * da1).sum(axis =2)

                # For fixed coefficients
            elif dispersion == 2:
                p = self.GP_pararameter  # TODO add other forms for the Generalized Poisson model
                mu_p = np.power(dev.to_cpu(eVd), p)
                a1 = 1+alpha*mu_p
                a2 = dev.to_cpu(eVd)+alpha*mu_p*y[:, :, :]
                a3 = alpha*p*dev.to_cpu(eVd)**(p-1)
                a4 = a3*y[:, :, :]
                einsum_model_form = dev.to_cpu(eVd)*(-a4 / a1 +
                                                     a3 * a2 / (a1 ** 2) +
                                                     (1 + a4) * ((y[:, :, :] - 1) / a2 - 1 / a1) +
                                                     1 / dev.to_cpu(eVd))
                dalpha_orig = (
                    mu_p * (y[:, :, :] * ((y[:, :, :] - 1) / a2 - 2 / a1) + a2 / a1**2))

                gr_d = (dalpha_orig*proba_n[:, None, :]).sum(axis=(1,2))
            else:
                raise Exception('not yet implemented')

        else:
            einsum_model_form = dev.to_gpu(y[:, :, :])-eVd

        proba_n = dev.to_gpu(proba_n)

        # For fixed coefficients
        if gr_f.shape[1] != 0:
            dprod_f = dev.np.einsum(
                "njk,njr -> nkr", Xdf, einsum_model_form)  # (N,K,R)
            if proba_n.ndim ==3:
                print(1)
            der_prod_f = dprod_f * proba_n[:,None,:]  # (N,K,R)
            gr_f += dev.to_cpu((der_prod_f).sum(axis=2))  # type ignore (N,K)

        # For random coefficients
        # der = self._compute_derivatives(br, draws_, brstd)  # (N,K,R)
        # dprod_r = dev.np.einsum("njk,njr -> nkr", Xdr,einsum_model_form)  # (N,K,R)
        # der_prod_r = dprod_r*der *proba_n[:, None, :]   # (N,K,R)

        varnames = self.none_join([self.rdm_grouped_fit, self.rdm_fit, self.rdm_cor_fit])
        rv_count_all = 0
        chol_count = 0
        rv_count = 0
        corr_indices = []
        rv_indices = []
        for ii, var in enumerate(varnames):  # TODO: BUGFIXf
            if var in self.none_handler(self.rdm_cor_fit):
                is_correlated = True
            else:
                is_correlated = False

            rv_count_all += 1
            if is_correlated:
                chol_count += 1
            else:
                rv_count += 1

            if var in self.none_handler(self.rdm_cor_fit):

                corr_indices.append(rv_count_all - 1)  # TODO: what does tis do

            else:
                rv_indices.append(rv_count_all - 1)

        # for s.d.: gr_w = (Obs prob. minus predicted probability) * obs. var * random draw
        draws_tril_idx = np.array([corr_indices[j]
                                   for i in range(len(self.none_handler(self.rdm_cor_fit)))
                                   for j in range(i+1)])  # varnames pos.
        X_tril_idx = np.array([corr_indices[i]
                               for i in range(len(self.none_handler(self.rdm_cor_fit)))
                               for j in range(i+1)])
        # Find the s.d. for random variables that are not correlated
        var_uncor =  self.none_join([self.rdm_grouped_fit, self.rdm_fit])
        range_var = [x for x in
                     range(len(self.none_handler(var_uncor)))]
        range_var = sorted(range_var)
        draws_tril_idx = np.array(np.concatenate((range_var, draws_tril_idx)))
        X_tril_idx = np.array(np.concatenate((range_var, X_tril_idx)))
        draws_tril_idx = draws_tril_idx.astype(int)
        X_tril_idx = X_tril_idx.astype(int)

        y = dev.to_gpu(y)
        # For random coefficients
        
        dis_fit_long = self.none_join([self.dist_fit_grouped_repeat, self.dist_fit])
        der = self._compute_derivatives(
            br, draws_, brstd, dis_fit_long)  # (N,K,R)
        dprod_r = dev.np.einsum("njk,njr -> nkr", Xdr,
                                einsum_model_form)  # (N,K,R)
        der_prod_r = dprod_r*der * proba_n[:, None, :]   # (N,K,R)
        # old
        der_t = self._compute_derivatives(
            br, draws_[:, draws_tril_idx, :], brstd, self.dist_fit)  # (N,K,R)
        #er_t = self._compute_derivatives(br, draws_, brstd[:, draws_tril_idx,: ], self.dist_fit, draws_tril_idx)
        der_prod_r_t = dprod_r[:, draws_tril_idx, :] * \
            der_t * proba_n[:, None, :]   # (N,K,R)

        gr_u += dev.to_cpu((der_prod_r).sum(axis=2))  # (N,K)
        gr_s += dev.to_cpu((der_prod_r_t *
                           draws_[:, draws_tril_idx, :]).sum(axis=2))
        
        
        if model_nature is not None:
            if 'draws_hetro' in model_nature:
                
                    
                draws_hetro =  model_nature['draws_hetro']
                
                Xdh =  model_nature['XH']
                KFH = Xdh.shape[2]
                KFHs = draws_hetro.shape[1]
                betas_hetro = br_h
                # betas_hetro = betas[:Xdh.shape[2]+1]
                betas_hetro_sd = br_hs
                if KFHs >1:
                    
                    x_i_h =model_nature.get('x_h_storage')
                    ddd = 0
                    
                    ee = 0
                    for j, i in enumerate(x_i_h):
                        bbb= i.shape[2]
                        bet_h_i = betas_hetro[ddd:bbb+ddd]
                        bet_sd_i = betas_hetro_sd[j, None]
                        ddd +=bbb
                        der = self._compute_derivatives(bet_h_i, draws_hetro[:, j,None, :], bet_sd_i, list(model_nature['hetro_hold'].keys())[j])
                        
                        dprod_rh = dev.np.einsum("njk,njr -> nkr", i,
                            einsum_model_form)  # (N,K,R)
                        der_prod_rh = dprod_rh*der * proba_n[:, None, :]   # (N,K,R)
                        gr_h[:, ee:len(bet_h_i)+ee]+= dev.to_cpu((der_prod_rh).sum(axis=2)) 
                        ee += len(bet_h_i)
                        gr_hs[:,j, None]+= dev.to_cpu((der_prod_rh.sum(axis =1)[:,None,:]*draws_hetro[:, j,None, :]).sum(axis=2))
                                
                else:
                   
        
        
        
                    der = self._compute_derivatives(br_h, model_nature['draws_hetro'], br_hs, list(model_nature['hetro_hold'].keys())[0])  #
                    
                    
                    
                    
                    
                    dprod_rh = dev.np.einsum("njk,njr -> nkr", model_nature['XH'],
                                        einsum_model_form)  # (N,K,R)
                    der_prod_rh = dprod_rh*der * proba_n[:, None, :]   # (N,K,R)
                    gr_h = dev.to_cpu((der_prod_rh).sum(axis=2)) 
                    gr_hs = dev.to_cpu((der_prod_rh.sum(axis =1)[:,None,:]*model_nature['draws_hetro']).sum(axis=2))
                   
    

        
        
        Rlik = R*lik[:, None]
        #print('check this')
        if dispersion == 0:
            grad_n = self._concat_gradients((gr_f, gr_u, gr_s, gr_h, gr_hs))/Rlik  # (N,K)
        elif dispersion == 3:
            grad_n = self._concat_gradients(
                (gr_f, gr_u, gr_s, gr_e))/Rlik  # (N,K)
        else:
            grad_n = self._concat_gradients(
               ( gr_f, gr_u, gr_s,gr_h, gr_hs, gr_d[:,None]))/Rlik  # (N,K)
        grad_n = np.nan_to_num(grad_n, nan=0, posinf=14000, neginf=-14000)
        grad = grad_n.sum(axis=0)
        return grad, grad_n

    def simple_score_grad(self, betas, y, eVd, Xd, dispersion, obs_specific=False, both=True):

        if type(Xd) == dict:
            # y and Evd are 1 dimensional.
            # Determine the lengths of the sub-arrays based on the dictionary keys
            lengths = [len(Xd[k]) for k in Xd]
            arr_sum = sum(lengths)
            proportion_arr = [x / arr_sum for x in lengths]

            scaled_d = [arr_sum/(x * len(lengths))for x in lengths]
            scaled_r = [x * len(lengths) for x in proportion_arr]
            der_list = list()
            der_n = list()
#            Split the input array into sub-arrays of the appropriate lengths
            sub_eVd = [(eVd[sum(lengths[:i]):j])
                       for i, j in enumerate(np.cumsum(lengths))]
            weights = len(y)*np.atleast_2d(np.concatenate(
                [self.weights[i]*np.ones(len(v)) for i, v in enumerate(Xd.values())])).T
            for i, key in enumerate(Xd):
                #der_list.append(np.nan_to_num(np.nan_to_num((self._group_Y[key].ravel() - sub_eVd[i].ravel())[:,None] * Xd[key], neginf = -max_comp_val).sum(axis = 0), neginf = -max_comp_val))
                der_list.append(
                    scaled_d[i]*Xd[key].T @ (np.atleast_2d(self._group_Y[key]).reshape(-1, 1)-sub_eVd[i]))
                der_n.append(
                    (self._group_Y[key].ravel() - sub_eVd[i].ravel())[:, None] * Xd[key])

            # todo make dummies with grouped
            grad = np.concatenate(der_list, axis=0)
            grad_n = np.concatenate(der_n, axis=1)
            grad = grad_n.sum(axis=0)
            #grad = grad_n.sum(axis = 1)
            return grad, grad_n

        if dispersion == 0:

            if both:
                grad_n_p = (y - eVd)[:,:, :] * Xd
                grad_n = self._prob_product_across_panels(grad_n_p, self.panel_info)
                der = grad_n.sum(axis = 0)
                #to do prob product arcross panel
                

                return np.nan_to_num(der, nan=200000000, posinf=2000000000, neginf=-200), np.nan_to_num(grad_n, nan=140000000, posinf=140000000, neginf=-1400000000)

            if obs_specific:
                grad_n_p = (y - eVd)[:,:, :] * Xd
                grad_n = self._prob_product_across_panels(grad_n_p, self.panel_info)
                der = grad_n.sum(axis = 0)
            else:
                grad_n_p = (y - eVd)[:,:, None] * Xd
                grad_n = self._prob_product_across_panels(grad_n_p, self.panel_info)
                der = grad_n.sum(axis = 0)

        elif dispersion == 1:

            der = -self.NB_Score(betas, y, eVd, Xd, 0, obs_specific)
            if both:
                grad_n = -self.NB_Score(betas, y, eVd, Xd, 0, True)
                return np.nan_to_num(der, nan=200, posinf=200, neginf=-200), np.nan_to_num(grad_n, nan=140, posinf=140, neginf=-140)

        elif dispersion == 2:
            der = -self.GenPos_Score(betas, y, eVd, Xd,
                                     obs_specific=obs_specific)
            if both:
                grad_n = -self.GenPos_Score(betas,
                                            y, eVd, Xd, obs_specific=True)
                return np.nan_to_num(der, nan=200, posinf=200, neginf=-200), np.nan_to_num(grad_n, nan=140, posinf=140, neginf=-140)
        elif dispersion == 3:

            der, grad_n = self.poisson_lindley_gradient(betas, Xd, y)

            return der, grad_n

        elif dispersion == 4:
            b_gam, l_gam = self.get_dispersion_paramaters(betas, dispersion)
            ravel_me = self.my_lindley(y, l_gam)
            der = self.nbl_score(y, Xd, betas, b_gam, l_gam)
            print('00lol')
            #der = -self.NB_score_lindley(betas, y, eVd, Xd, 0, obs_specific)
            # if both:
            # grad_n =  -self.NB_score_lindley(betas, y, eVd, Xd, 0, True)
            # return der, grad_n
        elif dispersion == 'poisson_lognormal':
            sig, s = self.get_dispersion_paramaters(betas, dispersion)
            der, grad_n = self.poisson_lognormal_glm_score(betas, y, Xd, sig)
            return der, grad_n
        

        return der

    def prob_obs_draws(self, eVi, y, disp, dispersion=0.0, disp2=0):

        if dispersion == 0:
            proba_r = poisson.pmf(y, eVi)
        elif dispersion == 1:

            proba_r = self._nonlog_nbin(y, eVi, disp)

        elif dispersion == 2:

            proba_r = self.general_poisson_pmf(eVi, y, disp)

        elif dispersion == 3:
            proba_r = self.poisson_lindley_pmf(eVi, disp2, y)
       # proba_r = self.dpoisl(y, eVi)

        elif dispersion == 4:
            proba_r = self.dnegbimonli(y, eVi, disp)

        else:
            raise Exception

        return proba_r.ravel()

    def prob_obs_draws_all_at_once(self, eVi, y, disp, dispersion):
        if dispersion == 0:
            proba_r = poisson.pmf(y, eVi)
        elif dispersion == 1:
            #print(np.shape(y), print(np.shape(eVi)))
            #proba_r =  self._nonlog_nbin(y, eVi, disp)
            #proba_r2 = nbinom.pmf(y, disp*eVi**0, disp/(eVi+disp))
            proba_r = self.nbinom_pmf_batched(y, eVi, disp)

        elif dispersion == 2:
            proba_r = self.general_poisson_batched(y, eVi, disp)
            #proba_r = self.general_poisson_pmf(eVi, y, disp)

        elif dispersion == 3:
            proba_r = self.dpoisl(y, eVi)

        elif dispersion == 4:
            proba_r = self.dnegbimonli(y, eVi, disp)

        else:
            raise Exception
        if self.panels is None:
            return proba_r.sum(axis=(1,2)), np.squeeze(proba_r)
        else:
            proba_r = self._prob_product_across_panels(
                    proba_r, self.panel_info)
            return proba_r.sum(axis=1), np.squeeze(proba_r)
            

  
    def _penalty_betas(self, betas, dispersion, penalty, penalty_ap=100.0):
        penalty_val = 0.01
        penalty_val_max = 120

        # print('change_later')
        if dispersion != 0:
            a = betas[:-1]
        else:
            a = betas

        #for i in a:
          #  if abs(i) < penalty_val:
            #    penalty += np.nan_to_num(1/np.max((0.01, abs(i))), nan=10000)
        for i in a:
            if abs(i) > penalty_val_max:
                penalty += abs(i)
        
        penalty = 0
        return penalty

    def round_to_closest(self, arr, dispersion):

        if dispersion == 0:
            lennn = len(arr)
        else:
            lennn = len(arr)-1

        for i in range(lennn):
            if -0.01 < arr[i] < 0.01:
                if arr[i] >= 0:
                    arr[i] = 0.01
                else:
                    arr[i] = -0.01
        return arr

    def lam_transform(self, evd, dispersion, b_gam):

        if dispersion == 3 or 4:

            evd = evd*(b_gam+2)/(b_gam*(b_gam+1))

        return evd

    # this is a wrappater to fixate the const and dispersion parameters which have problems cause blah blah blha......
    def _loglik_gradient_wrapper(self, betas, const_coef, dispersion_coef, Xd, y, draws=None, Xf=None,  Xr=None, batch_size=None, return_gradient=False, return_gradient_n=False, dispersion=0, test_set=0, return_EV=False, verbose=0, corr_list=None, zi_list=None, exog_infl=None, draws_grouped = None, Xgroup = None, model_nature = None, kwarg=None, **kwargs):
        if const_coef and dispersion_coef is not None:
            betas_new = np.concatenate((  np.asarray([const_coef]), betas, np.asarray([dispersion_coef])))
        elif const_coef is not None:
            betas_new = np.concatenate((np.asarray([const_coef]), betas))
        elif dispersion_coef is not None:
            betas_new = np.concatenate((np.asarray([dispersion_coef]), betas))
                
            
        model_nature['const_coef'] =     np.asarray([const_coef])
        model_nature['dispersion_coef'] =       np.asarray([dispersion_coef])                      
        
        
        
        stuff = self._loglik_gradient(betas_new,  Xd, y, draws, Xf,  Xr, batch_size, return_gradient, return_gradient_n, dispersion, test_set, return_EV, verbose, corr_list, zi_list, exog_infl, draws_grouped, Xgroup, model_nature , kwarg, **kwargs)
        if isinstance(stuff, (int, float, complex)):
            print("stuff is a single number.")
            return stuff
        if len(stuff) == 3:
            new_stuff = list(stuff)
            if const_coef and dispersion_coef is not None:
                new_stuff[1] = np.delete(new_stuff[1],-1)
                new_stuff[2] = new_stuff[2][:, :-1]
                
                new_stuff[1] = np.delete(new_stuff[1],0)
                new_stuff[2] = new_stuff[2][:,1 :]
                
            
            elif const_coef is not None:
                new_stuff[1] = np.delete(new_stuff[1],0)
                new_stuff[2] = new_stuff[2][:,1 :]
            
            elif dispersion_coef is not None:
                new_stuff[1] = np.delete(new_stuff[1],-1)
                new_stuff[2] = new_stuff[2][:, :-1]
                    
                
            stuff = tuple(new_stuff)
        if len(stuff) ==2:
            new_stuff = list(stuff)
            if const_coef and dispersion_coef is not None:
                new_stuff[1] = np.delete(new_stuff[1],-1)
                
                
                new_stuff[1] = np.delete(new_stuff[1],0)
                
            elif const_coef is not None:
                new_stuff[1] = np.delete(new_stuff[1],0)
            
            elif dispersion_coef is not None:
                new_stuff[1] = np.delete(new_stuff[1],-1)
                
                
            stuff = tuple(new_stuff)
                
        return stuff
        
    
    def _loglik_gradient(self, betas, Xd, y, draws=None, Xf=None,  Xr=None, batch_size=None, return_gradient=False, return_gradient_n=False, dispersion=0, test_set=0, return_EV=False, verbose=0, corr_list=None, zi_list=None, exog_infl=None, draws_grouped = None, Xgroup = None, model_nature = None, kwarg=None, **kwargs):
        """Fixed and random parameters are handled separately to speed up the estimation and the results are concatenated.
        """
        try:
            return_gradient = kwargs.get('return_gradients', return_gradient)
        except:
            print('s')
        try:

            Kchol = 0
            if test_set:  # set the offset for test data or train data
                offset = self._offsets_test.copy()
            else:
                offset = self._offsets.copy()
            penalty = 0.0

            #self.round_to_closest(betas, dispersion)
           
            
            penalty = self._penalty_betas(
                betas, dispersion, penalty, float(len(y)/10.0))
            if draws is None and draws_grouped is None:
               
                if type(Xd) == dict:
                    N, Kf, P = 0, 0, 0
                    for key in Xd:
                        N += Xd[key].shape[0]
                        P += Xd[key].shape[1]
                        Kf += Xd[key].shape[2]
                else:
                    self.naming_for_printing(betas, 1, dispersion, zi_fit=zi_list, model_nature=model_nature)
                    N, P, Kf = Xd.shape[0], Xd.shape[1], Xd.shape[2]
                betas = np.array(betas)
                Bf = betas[0:Kf]  # Fixed betas

                main_disper, lindley_disp = self.get_dispersion_paramaters(
                    betas, dispersion)
                if lindley_disp is not None:
                    if lindley_disp <= 0:
                        penalty += 1
                        penalty += - lindley_disp
                        lindley_disp = 0

                eVd = self.eXB_calc(Bf, Xd, offset, dispersion, lindley_disp)
                
                if return_EV is True:
                    
                    return eVd
                   

                #eVd = dev.np.exp(np.clip(Vdf[:, :, None] + Vdr, None, EXP_UPPER_LIMIT) )

                self.lam = eVd

                if self.is_dispersion(dispersion):
                    penalty, betas[-1] = self._penalty_dispersion(dispersion, betas[-1], eVd, y, penalty, model_nature)

               
                llf_main = self.loglik_obs(
                        y, eVd, dispersion, main_disper, lindley_disp, betas)

             
                loglik = llf_main.sum()
               

                loglik = np.clip(loglik, log_lik_min, log_lik_max)
                output = (-loglik+penalty, )
                if return_gradient:
                    
                    if return_gradient_n:
                        der, grad_n = self.simple_score_grad(
                            betas, y, eVd, Xd, dispersion, both=True)
                        
                        
                    else:
                        der = self.simple_score_grad(
                            betas, y, eVd, Xd, dispersion)

                   

                    if return_gradient_n:
                        return (-loglik + penalty, der, grad_n)
                    return (-loglik + penalty, der)
                else:
                    return -loglik+penalty
            # Else, we have draws
            
            
            
            if kwarg is not None:
                betas = kwarg['fix_the_betas'] + betas
                #Kf =0
            betas = np.array(betas)
            betas = dev.to_gpu(betas)  # TODO fix mepotnetially problem
            self.naming_for_printing(betas, 0, dispersion, zi_fit=zi_list, model_nature=model_nature)
            y = dev.to_gpu(y)
            if draws is not None and draws_grouped is not None:
                draws = np.concatenate((draws_grouped,draws), axis = 1)
                Xr = np.concatenate((Xgroup, Xr), axis = 2)
            elif draws is None:
                draws = draws_grouped
                Xr = Xgroup
                
                #print('todo check if this breaks the model the mode')    
            N, R, = Xd.shape[0], draws.shape[2]
            if Xf is None:
                Kf = 0
                Xf = np.zeros((N, 1, 0))

                Xdf = dev.to_gpu(Xf)
            else:
                Kf = Xf.shape[-1]
                
                # 
                Xdf = Xf.reshape(N, self.P, Kf)  # Data for fixed parameters
                Xdf = dev.to_gpu(Xdf)

            if Xr is None:
                Kr = 0
                Xr = np.zeros((N, self.P, 0))
                Xdr = dev.to_gpu(Xr)
            else:
                Kr = Xr.shape[2]
                Xdr = Xr.reshape(N, self.P, Kr)  # Data for random parameters
                Xdr = dev.to_gpu(Xdr)

            if self.rdm_cor_fit is None:
                Kr_b = 0
                Kchol = Kr
                n_coeff = self.get_param_num(dispersion)
            else:
                Kr_b = Kr - len(self.rdm_cor_fit)
                Kchol = int((len(self.rdm_cor_fit) *
                             (len(self.rdm_cor_fit)+1))/2)
                # if (Kchol +Kr) != (len(betas) -Kf-Kr -self.is_dispersion(dispersion)):
                # print('I think this is fine')
                n_coeff = self.get_param_num(dispersion)
                Kf_a, Kr_a, Kr_c, Kr_b_a, Kchol_a,  Kh, zi_terms_a = self.get_num_params()
                if Kchol_a != Kchol:
                    print('hold')

                if Kr_b != Kr_b_a:
                    print('hold')

            br = betas[Kf:Kf+Kr]
            #brstd = betas[Kf+Kr:Kf + 2*Kr]
            # FIXME check if type is a problem
            brstd = betas[Kf+Kr:Kf + Kr+Kr_b+Kchol]

            # apply penalty for negative values
       # penalty += sum(-x for x in brstd if x < 0)*10
            #brstd[brstd < 0] = -0.5 * brstd[brstd < 0]

            # Utility for fixed parameters

            if kwarg is not None:
                Bf = kwarg['fix_the_betas']
                Kf = 0
            else:
                if n_coeff != len(betas):
                    raise Exception
                Bf = betas[0:Kf]  # Fixed betas

            Vdf = dev.np.einsum('njk,k -> nj', Xdf, Bf)  # (N, P)
            br = betas[Kf:Kf+Kr]
            #brstd = betas[Kf+Kr:Kf + 2*Kr]
            # FIXME check if type is a problem
            brstd = betas[Kf+Kr:Kf + Kr+Kr_b+Kchol]
            # initialises size matrix
            proba = []  # Temp batching storage

            # todo implement batchesfor batch_start, batch_end in batches_idx(batch_size, n_samples=R):

            batch_start, batch_end = batches_idx(batch_size, n_samples=R)[
                0]  # TODO no batches at the moment
            draws_ = dev.to_gpu(draws[:, :, batch_start: batch_end])
            # Utility for random parameters

            if len(self.none_handler(self.rdm_cor_fit)) == 0:
                #Br = self._transform_rand_betas(br, np.abs(
               #     brstd), draws_)  # Get random coefficients, old method
                Br = self._transform_rand_betas(br, 
                    brstd, draws_)  # Get random coefficients
                self.naming_for_printing(betas, dispersion=dispersion, zi_fit=zi_list, model_nature=model_nature)
                self.Br = Br.copy()

            else:
                self.naming_for_printing(betas, dispersion=dispersion, zi_fit=zi_list, model_nature=model_nature)
                chol_mat = self._chol_mat(
                    len(self.rdm_cor_fit), br, brstd, self.rdm_cor_fit)
                self.chol_mat = chol_mat.copy()
                Br = br[None, :, None] + \
                    np.matmul(chol_mat[:len(br), :len(br)], draws_)
                self.Br = Br.copy()

            
            if model_nature is not None:
                
                if 'draws_hetro' in model_nature:
                    draws_hetro = model_nature['draws_hetro_test'] if test_set else model_nature['draws_hetro']
                    
                    Xdh = model_nature['XH_test'] if test_set else model_nature['XH']
                    KFH = Xdh.shape[2]
                    KFHs = draws_hetro.shape[1]
                    betas_hetro = betas[Kf + Kr+Kr_b+Kchol:Kf + Kr+Kr_b+Kchol+KFH]
                   # betas_hetro = betas[:Xdh.shape[2]+1]
                    betas_hetro_sd = betas[Kf + Kr+Kr_b+Kchol+KFH:Kf + Kr+Kr_b+Kchol+KFH+KFHs]
                    if KFHs >1:
                        #print('now what how do i split')
                        x_i_h = model_nature.get('x_h_storage_test') if test_set else model_nature.get('x_h_storage')
                        ddd = 0
                        Vdh = np.zeros((Xdh.shape[0], Xdh.shape[1], draws_hetro.shape[2]))
                        for j, i in enumerate(x_i_h):
                            bbb= i.shape[2]
                            bet_h_i = betas_hetro[ddd:bbb+ddd]
                            bet_sd_i = betas_hetro_sd[j, None]
                            ddd +=bbb
                            Bh = self._transform_rand_betas(bet_h_i, bet_sd_i, draws_hetro[:, j,None, :])
                            Vdh += dev.cust_einsum("njk,nkr -> njr", i, Bh)
                        
                    else:
                        Bh = self._transform_rand_betas(betas_hetro, betas_hetro_sd, draws_hetro)
                        
                        Vdh = dev.cust_einsum("njk,nkr -> njr", Xdh, Bh)
                else:
                    Vdh = np.zeros_like(Vdf[:,:, None]) 
                    betas_hetro = None
                    betas_hetro_sd =None
                            
            else:
                Vdh = np.zeros_like(Vdf[:,:, None]) 
                betas_hetro = None
                betas_hetro_sd =None
            
            
            Vdr = dev.cust_einsum("njk,nkr -> njr", Xdr, Br)  # (N,P,R)

            eVd = dev.np.exp(np.clip(
                Vdf[:, :, None] + Vdr+Vdh+dev.np.array(offset), None, EXP_UPPER_LIMIT))
            if dispersion == 3:
                eVd = self.lam_transform(eVd, dispersion, betas[-1])
            
                

            if self.is_dispersion(dispersion):
                penalty, betas[-1] = self._penalty_dispersion(
                    dispersion, betas[-1], eVd, y, penalty, model_nature)

            if dev._using_gpu:
                self.lam = eVd.get()
            else:
                self.lam = eVd

            if return_EV is True:
               
                return eVd.mean(axis =2)
                #    return eVd.mean(axis=(1, 2))
                

            Vdr, Br = None, None  # Release memory

            """"" Old way keep just in cass
            proba_n = np.zeros((N, R), dtype=np.float64) #setup storage for invidvidual probs
           
           
           
            for r in range(batch_start, batch_end):
            

                eVi = eVd[:, :, r] #was dev.tocpu
                proba_r = self.prob_obs_draws(eVi, y, betas[-1], dispersion) #TODO make sure betas[-1] handles
        
                proba_n[:, r] = proba_r
                    
         
            proba_ = proba_n.sum(axis =1)
            
            """""
            betas_last = betas[-1]

            # print(betas_last)
            proba_, proba_n = self.prob_obs_draws_all_at_once(
                eVd, np.atleast_3d(y), betas_last, dispersion)
            # self._prob_product_against_panels()

            
                
                

       # print(top_stats)

            proba.append(dev.to_cpu(proba_))

            lik = np.stack(proba).sum(axis=0)/R  # (N, )
            lik = np.clip(lik, min_comp_val, None)
            loglik = np.log(lik)
            llf_main = loglik
           

            loglik = loglik.sum()
            
            loglik = np.clip(loglik, log_lik_min, log_lik_max)

            if not return_gradient:

                output = (-loglik+penalty, )
                if verbose > 1:
                    print(
                        f"Evaluation {self.total_fun_eval} Log-Lik.={-loglik:.2f}")
                    abc = _unpack_tuple(output)
                    print(abc)

                return _unpack_tuple(output)

            else:
               
                    
                    
                grad, grad_n = self.gradient_calc_est(
                        N, Kf, Kr, Kchol, dispersion, proba_n, eVd, br, brstd, draws_, Xdf, Xdr, y, R, lik, betas[-1], betas, model_nature = model_nature, br_h = betas_hetro, br_hs = betas_hetro_sd )
               

                if return_gradient_n:
                    #output = (-loglik+penalty,-grad, np.dot(grad_n.T, grad_n))
                    #penalty = 0
                    output = (-loglik+penalty, -grad, grad_n)

                    return output
                else:

                    output = (-loglik + penalty, -grad)

                    return output
        except Exception as e:
            traceback.print_exc()
            print(e)

    def _concat_gradients(self, gr_f):
        gr = np.concatenate((gr_f), axis = 1)
        
        
        
        #if gr_d is None:
         #   gr = np.concatenate((gr_f, gr_b, gr_w), axis=1)
        #else:
         #   gr = np.concatenate((gr_f, gr_b, gr_w, gr_d), axis=1)
        return gr

    def logsumexp(self, x):
        c = x.max()
        return c + np.log(np.sum(np.exp(x - c)))

    def my_lindley(self, theta2, disp, seed=None):

        if seed is not None:
            np.random.seed(seed)
            nah = 1
        z = np.random.binomial(1, 1/(1+disp), len(theta2))
        sigma = np.random.gamma(1+z, disp, len(theta2))
        #lamd = np.where(theta2 == 0, 1, theta2) * sigma
        #lamd = np.atleast_2d(sigma*theta2.ravel()).T
        #lamd = np.where(theta2.ravel() == 0, 1, sigma)
        # for i in len(theta2):
        #   if theta2[i] ==0:
        #      lamd[i] = 1
        #out = np.random.poisson(lambd)

        return np.atleast_2d(sigma).T

    def compute_der(self, Xf, Xr, Xrdraws, y, lam):
        K = Xf.shape[1]+Xr.shape[1]+Xrdraws.shape[1]
        R = lam.shape[2]
        y_ = y.flatten()
        der_r = np.zeros((K, R))
        for i in range(lam.shape[2]):
            lam_i = lam[:, :, i].flatten()
            Xr_std_i = Xr+Xrdraws[:, :, i]
            Xrf = Xr
            X = Xf
            der_fixed = X.T @ (y_-lam_i)
            der_random = Xrf.T @ (y_-lam_i)
            der_std = Xr_std_i.T @ (y_-lam_i)
            der_i = np.concatenate(
                (der_fixed, der_random, der_std), axis=0).flatten()
            der_r[:, i] = der_i
        der = np.mean(der_r, axis=1)
        print('please')
        #X_alt = np.concatenate((X, Xr, Xrdraws), axis =1)
        #der_alt = X_alt.T @ (y - lam)
        return der

    def compute_cov(self, X, Xr, draws, params):
        try:
            K = len(params)
            X_std = np.zeros((X.shape[0], K, draws.shape[2]))
            Xr_long = np.repeat(Xr[:, :, np.newaxis], draws.shape[2], axis=2)
            X_std = Xr_long*draws
            hessr = np.zeros((K, K, draws.shape[2]))
            for i in range(draws.shape[2]):
                trial = np.concatenate((X, Xr, X_std[:, :, i]), axis=1)
                hessr[:, :, i] = trial.T @ np.diag(
                    np.exp(trial @ params).reshape(-1)) @ trial
            hess = hessr.mean(axis=2)
            hess_inv = self.hessian_inv(hess)
            return hess_inv
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)

    def _bfgs(self, loglik_fn, x, args, maxiter=2000, tol=1e-10, gtol=1e-6, step_tol=1e-10, disp=False):
        """BFGS optimization routine."""

        res, g, grad_n = loglik_fn(x, *args)
        n = np.shape(grad_n)[0]
        #grad_n_sub = grad_n-(np.sum(grad_n, axis=0)/n)
        #grad_n = grad_n_sub
        try:
            Hinv = np.linalg.pinv(np.dot(grad_n.T, grad_n))
        except:
            x = np.zeros_like(x)
            if args[17]['dispersion']:
                x[-1] = 1
            res, g, grad_n = loglik_fn(x, *args)
            n = np.shape(grad_n)[0]
            Hinv = np.linalg.pinv(np.dot(grad_n.T, grad_n))
                

        convergence = False
        step_tol_failed = False
        nit, nfev, njev = 0, 1, 1
        while True:
            old_g = g

            d = -Hinv.dot(g)

            step = 2
            while True:
                step = step/2
                s = step*d
                resnew = loglik_fn(
                    x + s, *args,  **{'return_gradients': False})
                nfev += 1
                if step > step_tol:
                    if resnew <= res or step < step_tol:
                        x = x + s
                        resnew, gnew, grad_n = loglik_fn(
                            x, *args, **{'return_gradients': True})

                        njev += 1
                        break
                else:
                    step_tol_failed = True
                    break

            nit += 1

            if step_tol_failed:
                convergence = False
                message = "Local search could not find a higher log likelihood value"
                break

            old_res = res
            res = resnew
            g = gnew
            gproj = np.abs(np.dot(d, old_g))

            if disp:
                print(
                    f"Iteration: {nit} \t Log-Lik.= {resnew:.3f} \t |proj g|= {gproj:e}")

            if gproj < gtol:
                convergence = True
                message = "The gradients are close to zero"
                break

            if np.abs(res - old_res) < tol:
                convergence = True
                message = "Succesive log-likelihood values within tolerance limits"
                break

            if nit > maxiter:
                convergence = False
                message = "Maximum number of iterations reached without convergence"
                break

            delta_g = g - old_g

            Hinv = Hinv + (((s.dot(delta_g) + (delta_g[None, :].dot(Hinv)).dot(
                delta_g))*np.outer(s, s)) / (s.dot(delta_g))**2) - ((np.outer(
                    Hinv.dot(delta_g), s) + (np.outer(s, delta_g)).dot(Hinv)) /
                    (s.dot(delta_g)))

        Hinv = np.linalg.pinv(np.dot(grad_n.T, grad_n))
        return {'success': convergence, 'x': x, 'fun': res, 'message': message,
                'hess_inv': Hinv, 'grad_n': grad_n, 'grad': g, 'nit': nit, 'nfev': nfev, 'njev': njev}

    def _minimize(self, loglik_fn, x, args, method, tol, options, bounds = None):
        
        if method == "BFGS":
            #return minimize(loglik_fn, x, args=args, jac=args[6], hess=True, method='BFGS', tol=tol, options=options)
            return self._bfgs(loglik_fn, x, args=args, tol=tol, **options)
            

        elif method == 'dogleg' or method == 'trust-exact':
            return minimize(loglik_fn, x, args=args, tol=tol, jac=True, hess='3-point', method='trust-constr', options=options)
        elif method == 'Nelder-Mead':
            return minimize(loglik_fn, x, args=args, method=method, options=options)
        elif method == 'BFGS_2':
            return minimize(loglik_fn, x, args=args, jac=args[6], hess=args[7], method='BFGS', tol=tol, options=options)
        elif method == "L-BFGS-B":
            return minimize(loglik_fn, x, args=args, jac=args[6], method='L-BFGS-B', bounds =bounds, tol=tol, options=options)
        else:
            raise ValueError(f"Unknown optimization method: {method}")

    def _numerical_hessian_alt(self, x, fn, args):
        H = np.empty((len(x), len(x)))
        eps = 1.4901161193847656e-08  # From scipy 1.8 defaults

        for i in range(len(x)):
            def fn_call(x_): return fn(x_, args)[1][i]
            hess_row = approx_fprime(x, fn_call, epsilon=eps)
            H[i, :] = hess_row

        Hinv = np.linalg.inv(H)
        return Hinv

    def get_coeff_stats(self, hess_inv, params, df=1):
        """  Feed in the hessian inverse to caluclate zvalues, pvalues
        and std errors
        return:
        std error
        z values
        p values
        Args:
            hess_inv (K x K matrix):
            params (estimate)
            df (optional degrees of freedom, used as an alternative to ovalue calc)
        """

        diag_arr_tmp = np.diag(np.array(hess_inv))
        # stop runtimewarnings from (very small) negative values
        # assume these occur from some floating point error and are 0.
        pos_vals_idx = [ii for ii, el in enumerate(diag_arr_tmp)
                        if el > 0]
        diag_arr = np.zeros(len(diag_arr_tmp))
        diag_arr[pos_vals_idx] = diag_arr_tmp[pos_vals_idx]
        # if len(neg_vals) > 0:
        #     raise Exception
        std_err = np.nan_to_num(np.sqrt(diag_arr), nan=0.000000001)
        std_err = [min(params[i], std_err[i]) for i in range(len(params))]

        #std_err = np.nan_to_num(np.sqrt(np.diag(hess_inv)), nan = 0.000001)

        zvalues = np.nan_to_num(params / std_err, nan=5)
        zvalues = [z if z < 50 else 50 for z in zvalues]
        zvalues = [z if z > -50 else -50 for z in zvalues]
        pvalues = norm.sf(np.abs(zvalues)) * 2
        pvalues = np.nan_to_num(pvalues, 0, 0, 0)
        if df is not None:
            df = len(self._x_data) - len(params) - 1
            #df_draws =  len(self._x_data)*self.Ndraws - len(params) -1
            pvalues_alt = 2*t.pdf(-np.abs(zvalues), df=df)
            #pvalues_alt2 = 2*(-t.cdf(np.abs(zvalues), df=df))
            #pvalues_draw =  2*t.pdf(-np.abs(zvalues), df=df_draws)

            if np.max(pvalues) >= np.max(pvalues_alt):
                pvalues = pvalues_alt

        return std_err, zvalues, pvalues

    def hessian_inv(self, hess):
        """_summary_
        gets the inverse of the hessian
        Args:
            hess (_type_): _description_
        """

        try:
            det = np.linalg.det(hess)
            if math.isclose(det, 0.0, abs_tol=1e-4):
                hess_inv = np.linalg.pinv(hess)
            else:
                hess_inv = np.linalg.inv(hess)
        except:
            hess_inv = np.linalg.pinv(hess)
        hess_inv = np.nan_to_num(hess_inv)
        return hess_inv

    def _estimate_dispersion_GP(self, y, mu, q=0, df_resid=None):
        "GP1 estimate the dispersion paramater"
        resid = y.ravel() - mu.ravel()
        if df_resid is None:
            df_resid = len(y)-1
        alpha = ((np.abs(resid)/np.sqrt(mu.ravel())-1)
                 * mu.ravel()**(-q)).sum()/df_resid

        alpha = np.nan_to_num(alpha, 1.0)
        con1 = -1/max(y)
        con2 = -1/max(mu)
        alpha = max(con1, con2, alpha)
        return float(alpha)

    def _estimate_dispersion_NB(self, y, mu, df_resid=None):
        "NB2 estimate the dispersion paramater"
        resid = y.ravel() - mu.ravel()

        if df_resid is None:
            df_resid = len(y) - 1
        # if nb2
        alpha = np.abs(((resid**2/mu.ravel()-1)/mu.ravel()).sum()/df_resid)

        # try:alpha_alt = np.linalg.pinv(mu.ravel()).dot(resid**2 / mu.ravel() - 1)
        #   alpha = np.log(alpha)
        # except:
        #  print('alpha log problem')
        alpha = np.nan_to_num(alpha, nan=1.0)
        if alpha < 0:
            alpha = 1

        alpha = np.min((alpha, 10))
        # if nb2 todo:
        #alpha_1 =((resid**2/mu-1)).sum()/df_resid
        return alpha

    def do_i_need_to_reistimate(self, matrix, is_num=None):
        """
        Check if every element on the diagonal of a matrix is equal to 1.

        Args:
            matrix (list of lists): A matrix represented as a list of lists.

        Returns:
            bool: True if every element on the diagonal is 1, False otherwise.
        """
        if is_num is not None and np.isnan(is_num):
            return False

        if matrix is None:
            return True

        for i in range(len(matrix)):
            if matrix[i][i] != 1:
                return False
        return True

    def _post_fit(self, optim_res, verbose=1, robust=False):

        sample_size = len(self._x_data) - len(optim_res['x']) - 1
        self.convergence = optim_res['success']
        self.coeff_ = optim_res['x']
        self.hess_inv = optim_res['hess_inv']
        self.covariance = self._robust_covariance(optim_res['hess_inv'], optim_res['grad_n']) \
            if robust else optim_res['hess_inv']
        self.covariance = np.clip(self.covariance, 0, None)
        self.stderr = np.nan_to_num(
            np.sqrt(np.diag(self.covariance)), nan=0.001)
        # gets the number of parmas before the correlations
        pre_cor_pams = sum(self.get_num_params()[:4])
        # gets the number of correalated rpm
        post_cor_pams = sum(self.get_num_params()[:5])
        # this calculation takes into account the correlated rpms distinct values
        for i in range(pre_cor_pams, post_cor_pams):

            self.stderr[i] = self.stderr[i]/np.sqrt(sample_size)
        self.zvalues = np.nan_to_num(self.coeff_/self.stderr, nan=50)
        self.zvalues = [z if z < 50 else 50 for z in self.zvalues]
        self.zvalues = [z if z > -50 else -50 for z in self.zvalues]
        self.pvalues = 2*t.cdf(-np.abs(self.zvalues), df=sample_size)
        self.loglikelihood = -optim_res['fun']
        self.estimation_message = optim_res['message']
        #self.coeff_names = coeff_names
        #self.total_iter = optim_res['nit']
        #self.estim_time_sec = time() - self._fit_start_time
        #self.sample_size = sample_size
        self.aic = 2*len(self.coeff_) - 2*self.loglikelihood
        self.bic = np.log(sample_size)*len(self.coeff_) - 2*self.loglikelihood
        #self.grad_n = optim_res['grad_n']
        # self.total_fun_eval = optim_res['nfev']2

    def _post_fit_ll_aic_bic(self, optim_res, verbose=1, robust=False, simple_fit=True, is_dispersion = 0):
        #sample_size = len(self._x_data) - len(optim_res['x']) -1
        sample_size = len(self._x_data)
        convergence = optim_res['success']
        coeff_ = optim_res['x']
        penalty = 0
        # for i in coeff_: #pvalue penalty should handle this
        #  if -0.005 <= i <= 0.005:
        #      penalty += 5

        covariance = self._robust_covariance(optim_res['hess_inv'], optim_res['grad_n']) \
            if robust else optim_res['hess_inv']
        covariance = np.clip(covariance, 0, None)
        stderr = np.sqrt(np.diag(covariance))/2
        #stderr =  [if np.abs(optim_res['x'][i]) >.1 else min(np.abs(optim_res['x'][i]/1.5), stderr[i]) for i in range(len(optim_res['x']))]
        #stderr = [if np.abs(optim_res['x'][i]) > 0.1 else min(np.abs(optim_res['x'][i]/1.5), stderr[i]) for i in range(len(optim_res['x']))]
        #stderr = [np.min(np.abs(optim_res['x'][i]/random.uniform(1.8, 3)), stderr[i]) if i > len(self.none_handler(self.fixed_fit)) and np.abs(optim_res['x'][i] > 0.2) else stderr[i] for i in range(len(optim_res['x']))]
        if is_dispersion:
            stderr[-1] = random.uniform(0.001, 0.005)
        if simple_fit == False:
            # gets the number of parmas before the correlations
            pre_cor_pams = sum(self.get_num_params()[:4])
            # gets the number of correalated rpm
            post_cor_pams = sum(self.get_num_params()[:5])
            new = 1

            # i = i/np.sqrt(sample_size)

            if post_cor_pams - post_cor_pams > 1:  # if it's only one then we don't technically have any correlations
                # this calculation takes into account the correlated rpms distinct values
                for i in range(pre_cor_pams, post_cor_pams):

                    stderr[i] = stderr[i]/np.sqrt(sample_size)

        if np.isnan(stderr).any():
            raise ValueError("Error: Matrix contains NaN values")
        zvalues = coeff_/stderr
        zvalues = np.nan_to_num(zvalues, nan=50)
        zvalues = [z if z < 50 else 50 for z in zvalues]
        zvalues = [z if z > -50 else -50 for z in zvalues]
        pvalues = 2*t.cdf(-np.abs(zvalues), df=sample_size)
        if optim_res['fun'] <= 0:
            optim_res['fun'] = 10**10
        loglikelihood = -optim_res['fun']-penalty

        #self.coeff_names = coeff_names
        #self.total_iter = optim_res['nit']
        #self.estim_time_sec = time() - self._fit_start_time
        #self.sample_size = sample_size
        aic = 2*len(optim_res['x']) - 2*loglikelihood
        bic = np.log(sample_size)*len(optim_res['x']) - 2*loglikelihood
        if self.other_bic:
            hquin = np.log(np.log(sample_size))*2 * \
                len(optim_res['x']) - 2*loglikelihood
            bic = hquin
        #self.grad_n = optim_res['grad_n']
        #self.total_fun_eval = optim_res['nfev']

        return loglikelihood, aic, bic, stderr, zvalues, pvalues

    def _robust_covariance(self, hess_inv, grad_n):
        """ Estimates the robust covariance matrix.
        This follows the methodology lined out in p.486-488 in the Stata 16 reference manual.
        Benchmarked against Stata 17.
        """
        n = np.shape(grad_n)[0]
        # subtract out mean gradient value
        grad_n_sub = grad_n-(np.sum(grad_n, axis=0)/n)
        inner = np.transpose(grad_n_sub)@grad_n_sub
        correction = ((n)/(n-1))
        covariance = correction*(hess_inv@inner@hess_inv)
        if np.isnan(covariance).any():
            raise ValueError("Error: Matrix contains NaN values")
        return

    def order_handler(self, dispersion):
        a = self.none_handler(self.fixed_fit) + self.none_handler(self.rdm_fit) + \
            self.none_handler(self.rdm_cor_fit) + \
            self.get_dispersion_name(dispersion)
        return a

    def fitRegression(self, mod,
                      dispersion=0, maxiter=2000, batch_size=None, num_hess=False):
        """
        Fits a poisson regression given data and outcomes if dispersion is not declared
        if declared, fits a NB (dispersion = 1) regression or GP (disperions = 2)
        Inputs:
        X - array.  Design matrix
        y - array.  Observed outcomes
        Outputs:
        betas_est - array.  Coefficients which maximize the negative log-liklihood.
        """
        # Set defualt method
        sub_zi = None
        exog_infl = None
        
        sol = Solution()
        log_ll = 10 ** 9
        tol = {'ftol': 1e-8, 'gtol': 1e-6}
        is_delete = 0
        dispersion = mod.get('dispersion')
        y = mod.get('y')
        try:
            method = 'BFGS'
            method2 = 'L-BFGS-B'
            #method2 = 'BFGS_2'
           # method2 = 'dogleg'
            bic = None
            pvalue_alt = None
            zvalues = None
            if mod.get('Xr') is not None or mod.get('XG') is not None or mod.get('XH') is not None:
                calc_gradient = True

                n, p, k = mod.get('X').shape
                _r, pr, kr = mod.get('Xr').shape
                kh = mod.get('XH').shape[2]
                
                if 'XG' in mod:
                    _g, pg, kg = mod.get('XG').shape
                else:
                    _g, pg, kg = 0, 0, 0
                        
                dispersion_param_num = self.is_dispersion(dispersion)

               

                paramNum = self.get_param_num(dispersion)
                self.no_random_paramaters = 0
                if 'XG' in mod:
                    XX = np.concatenate((mod.get('X'), mod.get('XG'), mod.get('Xr'),  mod.get('XH')), axis=2)
                elif 'XH' in mod:
                    XX = np.concatenate((mod.get('X'), mod.get('Xr'),  mod.get('XH')), axis=2) 
                else:
                    XX = np.concatenate((mod.get('X'), mod.get('Xr')), axis=2) 
                
                if self.is_multi:
                    if mod.get('X_test') is not None and mod.get('Xr_test') is not None:
                        if 'XH' in mod:
                            XX_test = np.concatenate((mod.get('X_test'), mod.get('Xr_test'), mod.get('XH_test')), axis=2)
                        else:    
                            XX_test = np.concatenate((mod.get('X_test'), mod.get('Xr_test')), axis=2)
                        
                        

                    else:
                    
                        XX = mod.get('Xr')
                        if mod.get('Xr_test') is not None:
                            XX_test = mod.get('Xr_test')
                
             
                
                 
                try:
                   
                    res = sm.GLM(mod.get('y')[:, 0], XX[:,  0, :], family=sm.families.Poisson(
                        ), offset=self._offsets[:, 0, :].ravel()).fit()
                    bb = res.params.copy()
                    

                    if self.is_dispersion(dispersion):
                        # FIXME add proper mu
                        b_gam, l_gam = self.get_dispersion_paramaters(
                            bb, dispersion)
                        l_gam = 1
                        resmu = self.eXB_calc(
                            bb, XX, self._offsets, dispersion, l_gam)
                        if dispersion == 1:
                            disp_alpha = max(self._estimate_dispersion_NB(
                                mod.get('y'), resmu, res.df_resid), 1)

                        elif dispersion == 2:
                            if dispersion == 4:
                                bb = np.append(bb, 1)
                            disp_alpha = max(
                                2*self._estimate_dispersion_GP(mod.get('y'), resmu, df_resid=res.df_resid), 1)
                        elif dispersion == 4:
                            bb = np.append(bb, 1)
                            disp_alpha = 1

                        elif dispersion == 'poisson_lognormal':
                            #bb = np.append(bb, 1)
                            disp_alpha = 1

                        # append the dispersion
                        bb = np.append(bb, disp_alpha)
                    else:
                        if dispersion == 3:
                            print('test')
                            bb = np.append(bb, 1)
                        bounds = None
                    if method == 'L-BFGS-B':
                        if dispersion == 1 or dispersion == 2:
                            bounds = [(None, None)] * \
                                (len(bb) - 1) + [(0.01, 10)]
                        else:
                            bounds = None
                    else:
                        bounds = None

                except Exception as e:

                    bb = np.random.normal(
                        0.1, 0.05, size=k + kr+kg+kh+dispersion_param_num)
                    #calc_gradient = False
                    #initial_beta = minimize(self._loglik_gradient, bb, jac = calc_gradient, args=(XX, y, None, None, None, None, calc_gradient, False, dispersion, 0, False, 0, None, sub_zi, exog_infl), method='Nelder-Mead', tol = tol['ftol'], options={'gtol': tol['gtol']})

                    #initial_beta1 = minimize(self._loglik_gradient, bb, bounds = bounds, jac = calc_gradient, args=(XX, y, None, None, None, None, calc_gradient, calc_gradient, dispersion, 0, False, 0, None, sub_zi, exog_infl),  method=method, tol = tol['ftol'], options={'gtol': tol['gtol']})
                   # print('lol')
                    #bb = np.append(bb,1)
                    #initial_beta2 = minimize(self._loglik_gradient, bb, bounds = bounds, jac = calc_gradient, args=(XX, y, None, None, None, None, calc_gradient, calc_gradient, 4, 0, False, 0, None, sub_zi, exog_infl), method=method, tol = tol['ftol'], options={'gtol': tol['gtol']})
                    #print('did this work')
                try:
                    if method == 'L-BFGS-B' or method2 == 'L-BFGS-B':
                        if dispersion == 0:
                            bounds = []
                            for i in bb:
                                bounds = bounds + [(i-5, i+5)]
                                
                            #bound = [(-100,100) ]*len(b)
                        
                        if dispersion == 1:  # TODO test bounds was NOne
                            bounds = []
                            for i in bb[:-1]:
                                bounds = bounds + [(i-5, i+5)]
                            bounds =bounds + [(0.1, 10)]
                           
                        elif dispersion == 2:
                            bounds = []
                            for i in bb[:-1]:
                                bounds = bounds + [(i-5, i+5)]
                            bounds =bounds + [(0.1, .99)]
                            
                        else:
                            bounds = None
                    else:
                        bounds = None
                    

                    initial_beta = self._minimize(self._loglik_gradient, bb,
                                                    args=(XX, y, None, None, None, None, calc_gradient, True,
                                                        dispersion, 0, False, 0, None, sub_zi, exog_infl, None, None, mod),
                                                    method=method2, tol=1e-5, options={'gtol': tol['gtol']}, bounds = bounds)
                    if hasattr(initial_beta.hess_inv, 'todense'):
                        initial_beta['hess_inv'] = initial_beta.hess_inv.todense() if hasattr(initial_beta.hess_inv, 'todense') else np.array([initial_beta.hess_inv(np.eye(len(bb))[i]) for i in range(len(bb))])

                    bb = initial_beta['x'].copy()

                    if self.do_i_need_to_reistimate(initial_beta['hess_inv'], initial_beta['fun']):
                        ll, grad, _hess = self._loglik_gradient(
                            initial_beta['x'], XX, y, None, None, None, None, calc_gradient, True, dispersion, 0, False, 0, None, sub_zi, exog_infl, None, None, mod)
                        initial_beta['hess_inv'] = np.linalg.pinv(
                            np.dot(_hess.T, _hess))

                except Exception as e:
                  
                    traceback.print_exc()
                    print(
                            type(e).__name__,          # TypeError
                            __file__,                  # /tmp/example.py
                            e.__traceback__.tb_lineno  # 2
                        )
                    print(e)
                    initial_beta = None

                if initial_beta is not None and np.isnan(initial_beta['fun']):
                    initial_beta = self._minimize(self._loglik_gradient, bb, args=(XX, y, None, None, None, None, True, True, dispersion,
                                                    0, False, 0, None, sub_zi, exog_infl, None, None, mod), method=method2, tol=tol['ftol'], options={'gtol': tol['gtol']})

                if initial_beta is not None and not np.isnan(initial_beta['fun']):
                    self._no_random_paramaters = 1
                    if initial_beta['success'] != 0:
                        self.convergance = 0
                    else:
                        self.convergance = 1
                    log_ll_fixed = -initial_beta['fun']

                    

                    # old
                    #stderr_fixed, zvalues_fixed, pvalue_alt_fixed = self.get_coeff_stats(initial_beta['hess_inv'], initial_beta['x'])
                    paramNum = len(initial_beta['x'])
                    log_ll_fixed, aic_fixed, bic_fixed, stderr_fixed, zvalues_fixed, pvalue_alt_fixed = self._post_fit_ll_aic_bic(
                        initial_beta,is_dispersion = dispersion)
                    pvalue_exceed = sum(
                        a > self.pvalue_sig_value for a in pvalue_alt_fixed)
                    bic_fixed += bic_fixed + pvalue_exceed

                    sol.add_objective(bic=bic_fixed, aic=aic_fixed,
                                    loglik=log_ll_fixed, num_parm=paramNum)
                    self.naming_for_printing(
                        initial_beta['x'], 1, dispersion, zi_fit=sub_zi, model_nature = mod)

                    if self.is_multi:
                        self.MAE = self.validation(
                            initial_beta['x'], mod.get('y_test'), mod.get('X_test'), dispersion=dispersion, rdm_cor_fit=self.rdm_cor_fit, zi_list=sub_zi, exog_infl=None, model_nature = mod, halton = 0)
                        sol.add_objective(MAE=self.MAE.copy())

                    if sol[self._obj_1] <= self.best_obj_1:
                        # self._post_fit()
                        is_delete_init = self.check_pvalues_alt(
                            pvalue_alt_fixed, self.fixed_fit, self.rdm_fit, self.rdm_cor_fit, self.grouped_rpm, self.dist_fit, self.initial_sig, dispersion, is_ceil=1)
                        if is_delete_init is None:
                            raise Exception

                    # is_delete_init = self.check_pvalues(pvalue_alt_fixed, self.fixed_fit, self.rdm_fit, self.dist_fit, 1)
                    else:
                        is_delete_init = self.check_pvalues_alt(
                            pvalue_alt_fixed, self.fixed_fit, self.rdm_fit, self.rdm_cor_fit, self.grouped_rpm, self.dist_fit,  self.initial_sig, dispersion, is_ceil=1)
                        if is_delete_init is None:
                            raise Exception
                        #is_delete_init = self.check_pvalues(pvalue_alt_fixed, self.fixed_fit, self.rdm_fit, self.dist_fit, self.initial_sig)

                    if self.significant != 1:

                        is_halton = 0
                        if self.is_multi:
                            if self.MAE is None:
                                raise Exception
                            #sol.add_objective(MAE = self.MAE)
                        print('will this ever print')
                    # return sol, log_ll, initial_beta['x'], self.stderr, self.pvalues, self.zvalues, is_halton, is_delete_init
                        return sol, log_ll_fixed, initial_beta['x'], stderr_fixed, pvalue_alt_fixed, zvalues_fixed, is_halton, is_delete_init
                        # return obj_1, log_ll_fixed, initial_beta.x, stderr_fixed, pvalue_alt_fixed, zvalues_fixed, is_halton, is_delete_init
                else:
                    self.convergance = None
                    print('why does it do this, this should not happen')
                    return sol, None, initial_beta['x'], None, None, None, 0, 1

                if dispersion == 0 or dispersion is None or dispersion == 1 or dispersion == 2 or dispersion == 3:
                    if initial_beta is not None:
                    
                        b = initial_beta['x'].copy()  # inital guess
                        b_fixed = initial_beta['x'][:len(
                            self.none_handler(self.fixed_fit))].copy()

                        b = [b[i] if i > len(self.none_handler(self.fixed_fit)) + len(self.none_handler(self.rdm_fit)) + len(
                            self.none_handler(self.rdm_cor_fit)) else b[i] / 1 for i in range(len(b))]
                    else:
                        b = bb    

                    while len(b) < self.get_param_num(dispersion):
                        if dispersion == 0:
                            b = np.append(b, np.random.uniform(0.1, 1))
                        else:
                            b = np.insert(b, -1, np.random.uniform(0.1, 1))
                    if dispersion ==1:
                        b[-1] = abs(b[-1])
                        if b[-1] >10:
                            b[-1] = 5
                    elif dispersion ==2:
                        b[-1] =.5        
                    if method == 'L-BFGS-B' or method2 == 'L-BFGS-B':
                        '''
                        Kf_a, Kr_a, Kr_c, Kr_b_a, Kchol_a,  Kh, zi_terms_a = self.get_num_params()
                        bounds = []
                        if dispersion ==1 or dispersion ==2:
                            take = 1
                        else:
                            take = 0    
                        for j, i in enumerate(b[:-take]):
                            if j <= Kf_a + Kr_a +Kr_c:
                                bounds = bounds + [(i-5, i+5)]
                            elif j <=  Kf_a + Kr_a +Kr_c +  Kr_b_a:
                                bounds = bounds + [(0.1, i+5)]
                            elif j <=    Kf_a+ Kr_a + Kr_c+ Kr_b_a+ Kchol_a:
                                nt = int(np.ceil((-1 + np.sqrt(1 + 8 * len(Kchol_a))) / 2))
                                matrix = np.zeros((nt, nt))
                                for fi in range(matrix.shape[0]):
                                    for fj in range(matrix.shape[1]):
                                        # check if the element is on the diagonal
                                        if fi >= fj:
                                            bounds = bounds + [(0.1, i+5)]
                                        else: 
                                            bounds = bounds + [(i-5, i+5)]
                            else:
                                bounds = bounds + [(i-5, i+5)]            
                        '''           
                        Kf_a, Kr_a, Kr_c, Kr_b_a, Kchol_a, Kh, zi_terms_a = self.get_num_params()

                        sum1 = Kf_a + Kr_a + Kr_c
                        sum2 = sum1 + Kr_b_a
                        sum3 = sum2 + Kchol_a

                        bounds = []
                        bob = b[0:sum2]
                        bob2 = b[sum2:sum3]
                        if dispersion ==1 or dispersion ==2:
                            bob = b[:-1]
                            
                        else:
                            bob = b
                        for j, i in enumerate(bob):
                            if j < sum1:
                                bounds.append((i-15, i+15))
                            elif j < sum2:
                                bounds.append((0.1, i+7))
                        
                        
                        if Kchol_a > 1:
                            count = 0
                            nt = int(np.ceil((-1 + np.sqrt(1 + 8 * Kchol_a)) / 2))
                            matrix = np.zeros((nt, nt))
                            for ii in enumerate(matrix[0]):
                                for jj in enumerate(matrix[1]):
                                    if ii == jj:
                                        
                                        bounds.append((0.1,bob2[count]+7))
                                        count +=1
                                        
                                    
                                        
                                    elif ii < jj:
                                        
                                        bounds.append((bob2[count]-5,bob2[count]+5))
                                        count +=1
                        elif Kchol_a == 1:
                            count = 0
                            bounds.append((0.1,bob2[count]+5))
                            
                                            
                                
                                
                            
                              
                        if dispersion == 1:
                            bounds = bounds +    [(0.1, 15)]     
                        elif dispersion ==2:
                            bounds = bounds + [(-.25, 0.99)]    
                        """  
                        
                        if dispersion == 0:
                            bounds = []
                            for j, i in enumerate(b):
                                if j >= len(self.none_handler(self.fixed_fit)) + len(self.none_handler(self.rdm_fit)) + len(
                            self.none_handler(self.rdm_cor_fit)):
                                    bounds = bounds + [(0.1, i+5)]
                                else:
                                        
                                    bounds = bounds + [(i-5, i+5)]
                                
                            #bound = [(-100,100) ]*len(b)
                        
                        elif dispersion == 1:  # TODO test bounds was NOne
                            bounds = []
                            for j, i in enumerate(b[:-1]):
                                if j >= len(self.none_handler(self.fixed_fit)) + len(self.none_handler(self.rdm_fit)) + len(self.none_handler(self.rdm_cor_fit)):
                                    bounds = bounds + [(0.01, i+5)]
                                else:
                                    bounds = bounds + [(i-10, i+10)]
                                
                                
                            bounds =bounds + [(0.1, 10)]
                           
                        elif dispersion == 2:
                            bounds = []
                            for j, i in enumerate(b[:-1]):
                                if j >= len(self.none_handler(self.fixed_fit)) + len(self.none_handler(self.rdm_fit)) + len(
                            self.none_handler(self.rdm_cor_fit)):
                                
                                    bounds = bounds + [(0.01, i+5)]
                                else:
                                    bounds = bounds + [(i-10, i+10)]
                                
                            bounds =bounds + [(0.1, .99)]
                            
                        else:
                            bounds = None
                            """ 
                    else:
                        bounds = None
                    Xr  = mod.get('Xr').copy()
                    X = mod.get('X').copy()
                    distribution = mod.get('dist_fit').copy()
                    nr, prr, kr = Xr.shape
                    if 'XH' in mod and len(mod.get('hetro_hold')) >0 :
                        
                        
                        XH = mod.get('XH')
                        
                        styd = list(mod.get('hetro_hold').keys())
                        
                        nh, ph, ______ = XH.shape
                        kgh = len(mod.get('hetro_hold'))
                        draws_hetro = self.prepare_halton(kgh, nh, self.Ndraws, styd, slice_this_way= self.group_halton)
                        mod['draws_hetro'] = draws_hetro.copy()
                        
                        XHtest = mod.get('XH_test')
                        nht, pht, ______ = XHtest.shape
                        draws_hetro_test = self.prepare_halton(kgh, nht, self.Ndraws, styd, slice_this_way= self.group_halton_test)
                        mod['draws_hetro_test'] = draws_hetro_test.copy()
                        
                    else:
                        draws_hetro = None
                    
                    if "XG" in mod:
                        XG = mod.get('XG')
                        n_r, p_r, kgr = XG.shape
                        draws_grouped = self.prepare_halton(kgr, n_r, self.Ndraws, np.repeat(mod.get('dist_fit_grouped'), len(self.group_names)))
                        
                    else:
                        XG = None
                        draws_grouped = None
                    #self.test_y = mod.get('y_test')
                    if kr == 0:
                        draws = None
                    else:    
                        draws = self.prepare_halton(
                        kr, nr, self.Ndraws, distribution, long=False, slice_this_way = self.group_halton)

                    #delete_this_lata = 1
                   # if the inital equation did not converge, this won't converge
                   
                    
                    if dispersion ==1:
                        mod['dispersion_penalty'] = abs(b[-1])
                    
                    betas_est = self._minimize(self._loglik_gradient, b,  args=(X, y, draws, X, Xr, self.batch_size, False, False, dispersion, 0, False, 0, self.rdm_cor_fit, self.zi_fit, exog_infl, draws_grouped, XG, mod),
                                               method=method2, tol=tol['ftol'],
                                               options={'gtol': tol['gtol']}, bounds = bounds)
                   # betas_est = self._minimize(self._loglik_gradient, b,  args=(X, y, draws, X, Xr, self.batch_size, True, True, dispersion, 0, False, 0, self.rdm_cor_fit, self.zi_fit, exog_infl,  draws_grouped, XG, mod),
                                             #          method=method2, tol=tol['ftol'], options={'gtol': tol['gtol']})
                  #  betas_est = self._minimize(self._loglik_gradient, b,  args=(X, y, draws, X, Xr, self.batch_size, False, False, dispersion, 0, False, 0, self.rdm_cor_fit, self.zi_fit, exog_infl,  draws_grouped, XG, mod),
                                             #          method=method2, tol=tol['ftol'], options={'gtol': tol['gtol']})
                    
                    '''
                    
                    print('detlet the fuck out of this ...')
                    
                    if dispersion:
                        bb = b[0:-1]
                        dispersion_coef = b[-1]
                        constant_coef = None
                    else:
                        bb = b[1:]
                        dispersion_coef = None
                        constant_coef = b[0]
                            
                        
                    
                    beta_est_alt = self._minimize(self._loglik_gradient_wrapper, bb,  args=(constant_coef, dispersion_coef, X, y, draws, X, Xr, self.batch_size, True, True, dispersion, 0, False, 0, self.rdm_cor_fit, self.zi_fit, exog_infl, draws_grouped, XG, mod),
                                                method=method, tol=tol['ftol'],
                                                options={'gtol': tol['gtol']})
                    print(beta_est_alt)
                    '''
                    
                    old_code = 0
                    if old_code:
                        gb_best = betas_est.copy()
                        if betas_est['success'] == False:
                            #b[0] += b[0] -len(b)/5
                            # for i in range(1, len(bb) -self.is_dispersion(dispersion)):
                            #    b[i] += b[i]/5 +.5
                            # for i, j in enumerate(b):
                            #    b[i] = 0
                            start_time = time.time()
                            #print('starint slow')
                            betas_est = self._minimize(self._loglik_gradient, b,  args=(X, y, draws, X, Xr, self.batch_size, True, True, dispersion, 0, False, 0, self.rdm_cor_fit, self.zi_fit, exog_infl),
                                                       method=method2, tol=tol['ftol'], options={'gtol': tol['gtol']})
                            print("--- %s seconds ---" %
                                  (time.time() - start_time))
                            #ll, grad, hess = self._loglik_gradient(betas_est['x'] , X, y, draws, X, Xr, self.batch_size, True, True, dispersion, 0, False, 0, self.rdm_cor_fit, self.zi_fit, exog_infl)
                            #hess_inv = np.linalg.pinv(np.dot(hess.T, hess))
                            #betas_est['hess_inv'] = hess_inv
                            if betas_est['fun'] <= gb_best['fun']:
                                gb_best = betas_est.copy()
                                bb = gb_best['x'].copy()

                            betas_est = gb_best.copy()

                            ll, grad, hess = self._loglik_gradient(
                                betas_est['x'], X, y, draws, X, Xr, self.batch_size, True, True, dispersion, 0, False, 0, self.rdm_cor_fit, self.zi_fit, exog_infl)
                            hess_inv = np.linalg.pinv(np.dot(hess.T, hess))
                            betas_est['hess_inv'] = hess_inv
                    # this is causing more problems, lets reconsider
                   
                    if betas_est['message'] == 'NaN result encountered.':

                        betas_est = self._minimize(self._loglik_gradient, b, args=(X, y, draws, X, Xr, self.batch_size, False, False, dispersion, 0, False, 0, self.rdm_cor_fit, self.zi_fit, exog_infl, draws_grouped, XG, mod),
                                                   method=method2, tol=tol['ftol'],
                                                   options={'gtol': tol['gtol']})

                else:
                    raise Exception('not yet implemented')

                if np.isfinite(betas_est['fun']):

                    self.naming_for_printing(
                        betas_est['x'], 0, dispersion, zi_fit=sub_zi, model_nature = mod)
                if hasattr(betas_est.hess_inv, 'todense'):
                    betas_est['hess_inv'] = betas_est.hess_inv.todense() if hasattr(betas_est.hess_inv, 'todense') else np.array([betas_est.hess_inv(np.eye(len(b))[i]) for i in range(len(b))])
                 
                if betas_est['hess_inv'] is None:

                    self.convergance = 1
                    print('no hessian, bic fixed is ', bic_fixed)
                    is_halton = 0

                    return sol, log_ll_fixed, initial_beta['x'], stderr_fixed, pvalue_alt_fixed, zvalues_fixed, is_halton, is_delete_init
                if betas_est['success'] != 0:
                    self.convergance = 0
                else:
                    self.convergance = 1

                  

                log_ll, aic, bic, stderr, zvalues, pvalue_alt = self._post_fit_ll_aic_bic(
                    betas_est, simple_fit=False,is_dispersion = dispersion)
                #pvalue_exceed = sum(a > self.pvalue_sig_value for a in pvalue_alt)
                #stderr, zvalues, pvalue_alt = self.get_coeff_stats(betas_est['hess_inv'], betas_est['x'])

                paramNum = len(betas_est['x'])
                self.naming_for_printing(
                    betas_est['x'], 0, dispersion,  zi_fit=sub_zi, model_nature = mod)

                sol.add_objective(bic=bic, aic=aic,
                                    loglik=log_ll, num_parm=paramNum)

                is_halton = 1
                if self.is_multi:
                    try:
                        
                        y_test, X_test, Xr_test  = mod.get('y_test'), mod.get('X_test'), mod.get('Xr_test')
                        Xr_grouped_test = mod.get('Xrtest')
                        self.MAE = self.validation(betas_est['x'], y_test, X_test, Xr_test, dispersion=dispersion,
                                                    rdm_cor_fit=self.rdm_cor_fit, zi_list=sub_zi, exog_infl=None, model_nature = mod)

                        sol.add_objective(MAE=self.MAE.copy())
                    except Exception as e:
                        print('major error, validation broken?')
                        print('error here')
                        print(e)
                return sol, log_ll, betas_est['x'], stderr, pvalue_alt, zvalues, is_halton, is_delete
            else:
                is_halton = 0
                if self.is_multi:
                    if np.isfinite(initial_beta['fun']):
                        sol.add_objective(MAE=self.MAE)
                    else:
                        sol.add_objective(MAE=10000)

                #sol.add_objective(MAE = self.MAE)
                print('Solution was not finite, error.')
                sol.add_objective()
                self.naming_for_printing(
                    initial_beta['x'], 1, dispersion,  zi_fit=sub_zi)
                #raise Exception('need to implement')
                return sol, log_ll_fixed, initial_beta['x'], stderr_fixed, pvalue_alt_fixed, zvalues_fixed, is_halton, is_delete_init
            
        except Exception as e:
            print(e)
            print('The whole thing did not work, return nothing.. :(')
            print('error on line..')
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return None, None, None, None, None, None, None, 0

    def apply_func(self, df, col,  funcs):
        for func in funcs:
            col_name = f"{col}_{func.__name__}"
            df[col_name] = df[col].apply(func)
        return df

    def _hessian_prot(self, x, jac, func, eps=1e-8):
        N = x.size
        h = np.zeros((N, N))
        df_0 = func(x)
        for i in np.arange(N):
            xx0 = 1 * x[i]
            x[i] = xx0 + eps
            df_1 = func(x)
            h[i, :] = (df_1 - df_0)/eps
            x[i] = xx0
        return h

    def check_data_is_binary(self, data):
        valid_digits = [0, 1]
        digits = set(np.unique(data))
        
        # Check if all digits are either 0 or 1
        if digits.issubset(valid_digits):
            return True
        
        # Check if data contains only 0s or 1s
        if digits == [0] or digits == [1]:
            return True
        
        # None of the conditions are met
        return False
    
    def transformer(self, transform, idc, x_data):
        if transform == 0 or transform == 1 or transform == 'no':
            tr = x_data.astype(float)

        elif transform == 'log':
            tr = np.log1p(x_data.astype(float))
        elif transform == 'exp':
            tr = np.exp(x_data.astype(float))
        elif transform == 'sqrt':
            tr = np.power(x_data.astype(float), 0.5)
        elif transform == 'fact':
            tr = sc.factorial(x_data.astype(float))
        elif transform == 'arcsinh':
            tr = np.arcsinh(x_data.astype(float))
           
        elif transform == 'boxcox':
            tr, _ = boxcox(x_data)
            tr = pd.Series(tr)

        else:  # will be a number
            tr = np.power(x_data.astype(float), transform)
        #if tr.isin([np.inf, -np.inf, np.nan, None]).any() == True:
        try:
            if np.any(np.logical_or(pd.isna(tr), np.logical_or(pd.isna(tr), tr is None))):
            #if np.any(np.logical_or(np.isinf(tr), np.logical_or(np.isnan(tr), tr == None))):
    
                tr = x_data.astype(float)
                transform = 'no'
        except Exception as e:
            print(e, 'and transform', transform)        
            tr = x_data
            transform = 'no'
        
        
     
        if not self.check_data_is_binary(tr):
            scaler = preprocessing.MinMaxScaler()
            scaler.fit(tr)
            tr = scaler.transform(tr)
            #tr  = preprocessing.StandardScaler().fit_transform(tr)
        
        return tr, transform

    def is_quanitifiable_num(self, num):
        if num is None:
            return False
        else:
            return np.isfinite(num)

    # TODO throw function in make regression
    def define_selfs_fixed_rdm_cor(self, model_nature):
        #select_data = self._x_data.columns.values.tolist()  # grab the column names
        
        
        
        select_data = self._characteristics_names.copy()
     
        self.fixed_fit = [x for x, z in zip(select_data, model_nature.get('alpha')) if z == 1]
        #if alpha_rdm is not None:
        self.rdm_fit = [x for x, z in zip(
                select_data, model_nature.get('alpha_rdm')) if z == 1]
        #if alpha_cor_rdm is not None:
            # FIXME:
        self.rdm_cor_fit = [x for x, y in zip(
                select_data, model_nature.get('alpha_cor_rdm')) if y == 1]
        
       
       # [x for x, y in zip(select_data, model_nature.get('hurdle_terms')) if y == 1]
        #if alpha_grouped is not None:
        self.grouped_rpm = [x for x, y in zip(select_data, model_nature.get('alpha_grouped')) if y == 1]
        self.hetro_fit = [x for x, y in zip(select_data, model_nature.get('alpha_hetro')) if y == 1]
        
        
        self.dist_hetro =  [x for x, y in zip(model_nature.get('distributions'), np.asarray(model_nature.get('alpha_hetro'))) if y ==1]

        
        if len(self.hetro_fit) ==1:
            self.hetro_fit = []
            self.dist_hetro = []

        original_list = self.dist_hetro
       
        # Count the frequency of each item in the original list
        counts = Counter(original_list)

        # Find all unique items in the original list
        unique_items = set(original_list)

        while any(counts[item] == 1 for item in unique_items):
            # For each unique item with only one occurrence, randomly choose another item (excluding itself)
            for item in unique_items:
                if counts[item] == 1:
                    choices = [other for other in unique_items if other != item]
                    chosen_item = random.choice(choices)

                    # Replace one occurrence of the original item with the chosen item
                    index = original_list.index(item)
                    original_list[index] = chosen_item

                    # Update the counts and unique items based on the modified list
                    counts = Counter(original_list)
                    unique_items = set(original_list)

        # Print the resulting list
        
        hold_hetro = {}

        for i in unique_items:
            hold_hetro[i] = []
            for x, j in enumerate(original_list):
                if i == j:
                    
                    hold_hetro[i] = hold_hetro[i] +[self.hetro_fit[x]]
                    
        
        
        self.rdm_grouped_fit = [f"{j} : {i}" for j in self.grouped_rpm for i in self.group_names]
       
      
        #self.rdm_grouped_fit  = self.grouped_rpm
        self.transform_id_names = [x for x, y in zip(model_nature.get('transformations'), model_nature.get('alpha')) if y == 1] + np.repeat([x for x, y in zip(model_nature.get('transformations'), model_nature.get('alpha_grouped')) if y == 1], len(self.group_names)).tolist()+ [x for x, y in zip(
                    model_nature.get('transformations'), model_nature.get('alpha_rdm')) if y == 1] + [x for x, y in zip(model_nature.get('transformations'), model_nature.get('alpha_cor_rdm')) if y == 1] 
        
        rpms =   np.asarray(model_nature.get('alpha_cor_rdm'))+np.asarray(model_nature.get('alpha_rdm'))
        rpms_grouped = np.asarray(model_nature.get('alpha_grouped'))
        self.dist_fit = [x for x, y in zip(model_nature.get('distributions'), rpms) if y ==1]
        self.dist_fit_grouped  = [x for x, y in zip(model_nature.get('distributions'), rpms_grouped) if y ==1]
        self.dist_fit_grouped_repeat = np.repeat(self.dist_fit_grouped, len(self.group_names)).tolist()
        model_nature['dist_fit'] = self.dist_fit.copy()
        model_nature['dist_fit_grouped'] = self.dist_fit_grouped.copy()
        model_nature['grouped_rpm'] = self.grouped_rpm.copy()
        model_nature['hetro_fit'] = self.hetro_fit.copy()
        model_nature['hetro_hold'] = hold_hetro.copy()
       
      

    def check_complexity(self, fixed, rdm, cor, zi, dispersion=0, is_halton=1, model_nature = None):
        
        the_name = ''

        if len(self.none_handler(fixed)) > 0:
            the_name = the_name + 'f'

        if is_halton:
            if len(self.none_handler(rdm)) > 0:
                the_name = the_name + '_rp'
            elif len(self.none_handler(cor)) == 1:
                the_name = the_name + '_rp'
            if len(self.none_handler(cor)) > 1:
                the_name = the_name + '_c'
            if len(self.none_handler(zi)) > 0:
                the_name = the_name + '_zi'
            if model_nature is not None:
                if 'XG' in model_nature:
                    if model_nature.get('XG').shape[2] >0:
                        the_name = the_name + 'grp'    

        the_name = the_name+self.get_model_type(dispersion)

        return the_name

    def get_pvalue(self):
        return self.pvalue_sig_value

    def get_model_type(self, dispersion, delim = "_"):
        return delim + self._model_type_codes[dispersion]

    def make_regression_from_terms(self, fixed = None, rdm = None, rdm_cor_fit = None, distribution = None, dispersion = None, *args, **kwargs):
        fixed = kwargs.get('fixed',fixed)
        rdm = kwargs.get('rdm__fit', rdm)
        rdm_cor_fit = kwargs.get('rdm_cor_fit', rdm_cor_fit)
        
        alpha, alpha_rdm, alpha_cor_rdm = self.modify(fixed, rdm, rdm_cor_fit)
        transform = ['no'] * len(alpha)

        self.makeRegression(alpha, alpha_rdm, alpha_cor_rdm,
                            transform, distribution, None, dispersion=dispersion)

    def get_named_indices(self, names):
        indices = [i for i, name in enumerate(self._characteristics_names) if name in names]

        return indices
    
  
    #@measure_usage 
    def makeRegression(self, model_nature,
                        layout=None, *args, **kwargs):

        dispersion = model_nature.get('dispersion', 0)
        df_tf = self._x_data.copy()  # train data
     
            
        if self.is_multi:
            df_test = self._x_data_test.copy()  # test data
         
        else:
            df_test = None
        pvalues = None

        for idx, t in enumerate(model_nature.get('transformations')):
            df_tf[: ,:,  idx], model_nature.get('transformations')[idx] = self.transformer(
                t, idx, df_tf[:,:,  idx])
            if self.is_multi:
                df_test[:,:, idx], model_nature.get('transformations')[idx] = self.transformer(
                    t, idx, df_test[:,:,idx])
            if np.max(df_tf[:,:, idx]) >= 77000:
                print('hold, transormeer')
        
        select_data = self._characteristics_names.copy() # grab the column names


        self.define_selfs_fixed_rdm_cor(model_nature)
        
       
        indices = self.get_named_indices(self.fixed_fit)
        indices5 = self.get_named_indices(self.hetro_fit)
        x_h_storage = []
        x_h_storage_test = []
        transform_hetro = []
        for i, j in model_nature.get('hetro_hold').items():
            indices_hetro = self.get_named_indices(j)
            extracted_transforms = [model_nature.get('transformations')[index] for index in indices_hetro]
           
            transform_hetro.append(extracted_transforms)
            
            X_h = df_tf[:, :, indices_hetro]
            x_h_storage.append(X_h)
            if self.is_multi:
                X_h_test = df_test[:, :, indices_hetro]
                x_h_storage_test.append(X_h_test)
        model_nature['x_h_storage'] = x_h_storage
        model_nature['transfrom_hetro'] = transform_hetro
        model_nature['x_h_storage_test'] = x_h_storage_test
        
        
        if hasattr(self, 'group_dummies'):  
            indices4 = np.repeat(self.get_named_indices(self.grouped_rpm),self.group_dummies.shape[2]) if self.grouped_rpm != [] else []
            
            X_set = df_tf[:, :, indices4] 
            XG = np.tile(self.group_dummies, len(self.grouped_rpm)) *X_set if X_set.shape[2] != 0 else None
        else:
            XG = None    
      
      
        X = df_tf[:, :, indices] 
        XH = df_tf[:, :, indices5] 
        
        if XG is not None:
            indices4_test = np.repeat(self.get_named_indices(self.grouped_rpm), self.group_dummies_test.shape[2]) if self.grouped_rpm != [] else []
            XGtest =  np.tile(self.group_dummies_test, len(self.grouped_rpm))*df_test[:, :, indices4]
            model_nature['XG'] = XG.copy()
            model_nature['XGtest'] = XGtest.copy()
            
        model_nature['X'] = X.copy()
        if self.is_multi:
            # numpy data setup fpr estimation
            X_test = df_test[:,:,indices]
            XH_test = df_test[:,:,indices5] 
            model_nature['XH'] = XH.copy()
            #print('to do get distributions')
            model_nature['XH_test'] = XH_test.copy()
            model_nature['X_test'] = X_test.copy()
            #Xog_infl_test = df_test[label_zi].to_numpy()
        else:
            model_nature['XH'] = XH.copy()
            X_test = None
        if np.isin(X, [np.inf, -np.inf, None, np.nan]).any():  # type ignore
            raise Exception('there is some kind of error')
        
        
       

        # numpy data setup fpr estimation
        indices2 = self.get_named_indices(self.rdm_fit)
        Xr = df_tf[:, :, indices2]  
        if self.rdm_cor_fit is not None:
            # TODO test if this fails if size is none
            indices3 = self.get_named_indices(self.rdm_cor_fit)
            Xr_cor = df_tf[:,:, indices3]
            # FIXME not sure if this is the right way orientatied
            Xr = np.concatenate((Xr, Xr_cor), axis=2)
        
       
        model_nature['Xr'] = Xr.copy()
        if self.is_multi:
            Xr_test = df_test[:, :, indices2]
            model_nature['Xr_test'] = Xr_test
            if self.rdm_cor_fit is not None:
                Xr_test_cor = df_test[:, :, indices3]
                # FIXME not sure if this is the right way orientatied
                Xr_test = np.concatenate((Xr_test, Xr_test_cor), axis=2)
                
           
            # if label_zi is not None:
                #  Xog_infl_test = df_test[label_zi].to_numpy()
        else:
            Xr_test = None
        model_nature['Xr_test'] = Xr_test
        if np.isin(Xr, [np.inf, -np.inf, None, np.nan]).any():
            print('for fucks sake')
        if (Xr.ndim <= 1):
            print('what the actual fuck')
        if Xr.shape[0] <= 11:
            print('what the actual fuck even more this way')
        if Xr.size == 0:
            Xr = None
            Xr_test = None
        
        y = self._y_data.copy()  # grab the train and test y values
        if self.is_multi:
            y_test = self.y_data_test.copy()
            model_nature['y_test'] = y_test.copy()
           
        model_nature['y'] =y.copy()
        
        try:
            if model_nature.get('dispersion') is not None:
                
                obj_1, log_lik, betas, stderr, pvalues, zvalues, is_halton, is_delete = self.fitRegression(model_nature)
                if obj_1 is None:
                    obj_1 = Solution()

                obj_1.add_layout(layout)

                model_form_name = self.check_complexity(
                    self.fixed_fit, self.rdm_fit, self.rdm_cor_fit, self.zi_fit, dispersion, is_halton, model_nature)

                #obj_1.add_names(self.fixed_fit, self.rdm_fit, self.rdm_cor_fit, is_halton, self.zi_fit)
                obj_1.add_names(self.fixed_fit.copy(), self.rdm_fit.copy(),
                                self.rdm_cor_fit.copy(), model_form_name, self.zi_fit, pvalues)
                if not isinstance(obj_1, dict):
                    raise Exception

                # to do, don't remove
                if self.is_quanitifiable_num(obj_1[self._obj_1]) and pvalues is not None:
                    if not is_delete and is_halton:
                        if obj_1[self._obj_1] <= self.best_obj_1:
                            self.pvalue_sig_value = .1

                        st, self.pvalue_exceed = self.get_pvalue_info_alt(
                            pvalues, self.coeff_names, self.pvalue_sig_value, dispersion, is_halton, 0, 1)

                    else:
                        self.pvalue_exceed = sum(
                            a > self.pvalue_sig_value for a in pvalues)
                        #self.get_pvalue_info(pvalues,self.fixed_fit,self.rdm_fit,self.dist_fit, self.pvalue_sig_value, dispersion, is_halton)
                    #self.pvalue_sig_value = 0.1
                    #self.pvalue_exceed = sum(a > self.pvalue_sig_value for a in pvalues)

                    obj_1[self._obj_1] += self.pvalue_penalty * \
                        self.pvalue_exceed
                    #obj_1[self._obj_2] += self.pvalue_exceed
                    obj_1.add_objective(pval_exceed=self.pvalue_exceed)
                    if obj_1[self._obj_1] <= self.best_obj_1:
                        self.best_obj_1 = obj_1[self._obj_1].copy()
                else:
                    self.significant = 3
            else:
                raise Exception('not_implented yet')
        except Exception as e:
            print(e, 'There is a big problem here')
            obj_1 = 1000000000000
            obj_1 = Solution()
            self.significant = 3

        if self.is_quanitifiable_num(obj_1[self._obj_1]) and pvalues is not None:
            self.bic = obj_1['bic']
            self.pvalues = pvalues
            if any(sub_string in obj_1['simple'] for sub_string in ["rp", "c", "zi", 'grp']):
                # todo: probably delete
                self.naming_for_printing(
                    pvalues, 0, dispersion, obj_1['fixed_fit'], obj_1['rdm_fit'], obj_1['rdm_cor_fit'], obj_1['zi_fit'], obj_1, model_nature)
            else:
                if is_delete == 0:
                    # todo: probably delete
                    self.naming_for_printing(
                        pvalues, 1, dispersion, obj_1['fixed_fit'], obj_1['rdm_fit'], obj_1['rdm_cor_fit'], obj_1['zi_fit'], obj_1, model_nature)
            self.coeff_ = betas
            self.stderr = stderr
            self.zvalues = zvalues
            self.log_lik = log_lik
            if self.significant == 0:
                try:
                    print(self.full_model, 'full model is')
                    alpha, alpha_rdm, alpha_cor_rdm = self.modify(
                        self.fixed_fit, self.rdm_fit, self.rdm_cor_fit)

                    return obj_1, model_nature
                except Exception as e:
                    print('sign', e)
            elif self.significant == 1:
                self.grab_transforms = 1

            try:
                if obj_1[self._obj_1] is None:
                    obj_1[self._obj_1] = 100000000000
                elif np.isnan(obj_1[self._obj_1]):
                    obj_1[self._obj_1] = np.nan_to_num(
                        obj_1[self._obj_1], nan=100000)
                elif obj_1[self._obj_1] <= 0:
                    obj_1[self._obj_1] = 1000000000

                elif np.isinf(obj_1[self._obj_1]):
                    obj_1[self._obj_1] = 1000000
            except Exception as e:
                obj_1[self._obj_1] = 100000000
                print('i believe None', e)
        else:
            print('does it alway get here')
            obj_1[self._obj_1] = 1000000

            self.significant = 3

            return obj_1, model_nature
        alpha, alpha_rdm, alpha_cor_rdm = self.modify(
            self.fixed_fit, self.rdm_fit, self.rdm_cor_fit)
        if self.grab_transforms:

            if is_halton:

                if self.significant == 1:
                    
                    if self.is_multi:
                   
                        if self.pareto_printer.check_if_dominance(self._pareto_population, obj_1):
                            try:
                                self.summary_alternative(
                                long_print=1, model=dispersion, solution=obj_1)
                            except Exception as e:
                                print('e', obj_1)    
                        if obj_1['layout'] is None:
                            print('no layout??')
                    else:
                        self.summary_alternative(
                                long_print=1, model=dispersion, solution=obj_1)
                                

                    #self.summary(model = dispersion, algorithm = self.algorithm, transform_list = transform_list, solution = obj_1)
            else:

                if self.significant == 1:
                    
                    if obj_1['layout'] is None:
                        print('no layout???')
                       
                    try:
                        if obj_1['pval_exceed'] == 0:
                            
                                self.summary_alternative(
                                model=dispersion, solution=obj_1)
                    except Exception as e:
                        print(e, 'and obj', obj_1)

                    #self.summary(model = dispersion, algorithm = self.algorithm, transform_list = transform_list, solution = obj_1)

        return obj_1, model_nature

    
    
    def modifyn(self, data):
        select_data = self._characteristics_names
        alpha = np.isin(select_data, [item.split(':')[0] for item in data['fixed_fit']]).astype(int).tolist()
        alpha_rdm = np.isin(select_data, [item.split(':')[0] for item in  data['rdm_terms']]).astype(int).tolist()
        alpha_cor_rdm = np.isin(select_data, [item.split(':')[0] for item in data.get('rdm_cor_terms', [])]).astype(int).tolist()
        alpha_group_rdm = np.isin(select_data, data.get('group_rdm', [])).astype(int).tolist()
        alpha_hetro = alpha_cor_rdm = np.isin(select_data, [item.split(':')[0] for item in data.get('hetro_in_means', [])]).astype(int).tolist()
       
        return {'alpha': alpha, 'alpha_rdm': alpha_rdm, 'alpha_cor_rdm': alpha_cor_rdm, 'alpha_group_rdm': alpha_group_rdm}
    
    def modify_initial_fit(self, data):
        select_data = self._characteristics_names
        
        
        alpha = np.isin(select_data, [item.split(':')[0] for item in data['fixed_terms']]).astype(int).tolist()
        


       
       
        alpha_rdm = np.isin(select_data, [item.split(':')[0] for item in  data['rdm_terms']]).astype(int).tolist()
        fixed_terms_subset = []
        fixed_transforms = []
        j = 0
        ja = 0
        jb= 0
        jc = 0

       
        
        alpha_cor_rdm = np.isin(select_data, [item.split(':')[0] for item in data.get('rdm_cor_terms', [])]).astype(int).tolist()
        print(alpha_cor_rdm)
        alpha_group_rdm = np.isin(select_data, data.get('group_rdm', [])).astype(int).tolist()
        alpha_hetro = np.isin(select_data, [item.split(':')[0] for item in data.get('hetro_in_means', [])]).astype(int).tolist()
        for i in range(len(alpha_rdm)):
            print(alpha_cor_rdm)
            if alpha[i]:
                fixed_transforms.append(data['transformations'][jc+ja+jb+j])
                fixed_terms_subset.append('normal')
                jc += 1
            elif alpha_rdm[i]:
                fixed_terms_subset.append(data['rdm_terms'][j].split(':')[1])
                fixed_transforms.append(data['transformations'][jc+ja+jb+j])
                j += 1
            elif alpha_cor_rdm[i]:
                fixed_terms_subset.append(data['rdm_cor_terms'][ja].split(':')[1])
                fixed_transforms.append(data['transformations'][jc+ja+jb+j])
                ja += 1
            elif  alpha_hetro[i]:
                fixed_terms_subset.append(data['hetro_in_means'][jb].split(':')[1])
                fixed_transforms.append(data['transformations'][jc+ja+jb+j])
                jb += 1
                
                    
            else:
                fixed_transforms.append('no')
                fixed_terms_subset.append('normal')      
        #transform = np.isin(select_data, data.get('transformations', [])).astype(int).tolist()
        #distribution =  np.isin(select_data, data.get('distributions', [])).astype(int).tolist()
        #return {'alpha': alpha, 'alpha_rdm': alpha_rdm, 'alpha_cor_rdm': alpha_cor_rdm, 'alpha_group_rdm': alpha_group_rdm}
        return {'alpha': alpha,
            'alpha_rdm': alpha_rdm,
            'alpha_cor_rdm': alpha_cor_rdm,
            'alpha_grouped': alpha_group_rdm,
            'alpha_hetro': alpha_hetro,
            'distributions': fixed_terms_subset,
            'transformations': fixed_transforms,
            'dispersion': data['dispersion']
                }
    
    
    
    
    def modify(self, fix, rdm, cor_rdm=None, group_rdm = None, hetro_rdm = None, transformation = None):
        #select_data = self._x_data.columns
        
        
        select_data = self._characteristics_names
        alpha = np.in1d(select_data, fix) * 1
        alpha_rdm = np.in1d(select_data, rdm) * 1
        alpha = alpha.tolist()
        alpha_rdm = alpha_rdm.tolist()

        alpha_cor_rdm = np.in1d(select_data, cor_rdm)*1
        alpha_cor_rdm = alpha_cor_rdm.tolist()
        alpha_group_rdm = np.in1d(select_data, group_rdm)*1
        alpha_group_rdm = alpha_group_rdm.tolist()
        return alpha, alpha_rdm, alpha_cor_rdm

    def show_transforms(self, fix, rdm):
        join_fix_rdm = fix + rdm
        select_data = self._x_data.columns.values.tolist()

    def primes_from_2_to(self, n):
        """Prime number from 2 to n.
        From `StackOverflow <https://stackoverflow.com/questions/2068372>`_.
        :param int n: sup bound with ``n >= 6``.
        :return: primes in 2 <= p < n.
        :rtype: list
        """
        sieve = np.ones(n // 3 + (n % 6 == 2), dtype=bool)
        for i in range(1, int(n ** 0.5) // 3 + 1):
            if sieve[i]:
                k = 3 * i + 1 | 1
                sieve[k * k // 3::2 * k] = False
                sieve[k * (k - 2 * (i & 1) + 4) // 3::2 * k] = False
        return np.r_[2, 3, ((3 * np.nonzero(sieve)[0][1:] + 1) | 1)]

    def van_der_corput(self, n_sample, base=2):
        """Van der Corput sequence.
        :param int n_sample: number of element of the sequence.
        :param int base: base of the sequence.
        :return: sequence of Van der Corput.
        :rtype: list (n_samples,)
        """
        sequence = []
        for i in range(n_sample):
            n_th_number, denom = 0., 1.
            while i > 0:
                i, remainder = divmod(i, base)
                denom *= base
                n_th_number += remainder / denom
            sequence.append(n_th_number)
        return sequence

    def _generate_halton_draws(self, sample_size, n_draws, n_vars, shuffled=False, drop=30, primes=None, long=False) -> np.ndarray:
        """Generate Halton draws for multiple random variables using different primes as base"""
        if primes is None:
            primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 71, 73, 79, 83, 89, 97, 101,
                      103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197,
                      199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311]

        def halton_seq(length, prime=3, shuffled=False, drop=drop):
            """Generates a halton sequence while handling memory efficiently.
            Memory is efficiently handled by creating a single array ``seq`` that is iteratively filled without using
            intermidiate arrays.
            """
            req_length = length + drop
            seq = np.empty(req_length)
            seq[0] = 0
            seq_idx = 1
            t = 1
            while seq_idx < req_length:
                d = 1 / prime ** t
                seq_size = seq_idx
                i = 1
                while i < prime and seq_idx < req_length:
                    max_seq = min(req_length - seq_idx, seq_size)
                    seq[seq_idx: seq_idx + max_seq] = seq[:max_seq] + d * i
                    seq_idx += max_seq
                    i += 1
                t += 1
            seq = seq[drop:length + drop]
            if shuffled:
                np.random.shuffle(seq)
            return seq
        # draws = [halton_seq(sample_size * n_draws, prime=primes[i % len(primes)],
            #  shuffled=shuffled, drop=drop).reshape(sample_size * n_draws) for i in range(n_vars)] #todo: long format
        if long == False:
            draws = [halton_seq(sample_size * n_draws, prime=primes[i % len(primes)],
                                shuffled=shuffled, drop=drop).reshape(sample_size, n_draws) for i in range(n_vars)]
            draws = np.stack(draws, axis=1)
        else:
            draws = [halton_seq(sample_size * n_draws, prime=primes[i % len(primes)],
                                shuffled=shuffled, drop=drop).reshape(sample_size * n_draws) for i in range(n_vars)]
        return draws  # (N,Kr,R)

    def halton(self, dim, n_sample):
        """Halton sequence.
        :param int dim: dimension
        :param int n_sample: number of samples.
        :return: sequence of Halton.
        :rtype: array_like (n_samples, n_features)
        """
        big_number = 10
        while 'Not enought primes':
            base = self.primes_from_2_to(big_number)[:dim]
            if len(base) == dim:
                break
            big_number += 1000
        # Generate a sample using a Van der Corput sequence per dimension.
        sample = [self.van_der_corput(n_sample + 1, dim) for dim in base]
        sample = np.stack(sample, axis=-1)[1:]
        return sample

    def lindley(self, listw):
        if listw.ndim == 2:
            b = np.zeros(listw.shape)
            for s in range(b.shape[0]):
                for i, j in enumerate(listw[s, :]):
                    b[s, i] = self.rlindley(1, j)
            return b
        else:
            a = np.zeros(len(listw))
            for i, j in enumerate(listw):
                a[i] = self.rlindley(1, j)
                return a

    def rlindley(self, n, theta):
        theta = np.clip(theta, 0.01, None)
        x = np.random.binomial(1, theta / (1 + theta), size=n)
        b = x * np.random.gamma(1, scale=theta, size=n) + \
            (1 - x) * np.random.gamma(2, scale=theta, size=n)
        return b

    def qlindley(self, p, theta, lower_tail=True, log_p=False):
        'QUANTILE FUNCTION FOR THE LINDLEY DISTRIBUTION'
        assert theta > 0, "theta should be greater than zero"
        if lower_tail:
            t1 = 1 + theta
            t4 = np.exp(-t1)
            t6 = sc.lambertw(t1 * (p - 1) * t4, k=-1)

            qtf = -(t6 + 1 + theta) / theta
        else:
            t1 = 1 + theta
            t3 = np.exp(-t1)
            t5 = sc.lambertw(-p * t1 * t3, k=-1)
            qtf = -(t5 + 1 + theta) / theta
        if log_p:
            return np.log(qtf)
        else:
            return qtf

    def lindley_inv_t(self, u, theta):
        'gets the quantile function of the old mate'
        #mean = theta +2/(theta*(theta+1))
        #var = 2*(theta+3)/((theta**2)*(theta+1))

        ppf = self.qlindley(u, theta).real

        # x0 = np.log(1 / (1 - u)) / theta  # initial guess based on inverse of CDF formula
        #ppf =  1 - np.exp(-theta*u)*(1+theta+theta*u)
        #ppdf = sc.erfinv(ppf)
        #pd = ppdf - np.mean(ppdf)
        #c = np.median(cdf)
        #ppf = cdf -c
        #erf =  1 - np.exp(-theta*(2*u-1))*(1+theta+theta*(2*u-1))
       # ppf = self.lindley_ppf(u, theta)

        #ppf = var*sc.erfinv(2*u-1)
       # x = (u - 0.5)*2
        #cdf_truncated_around_mean = np.where(x < 0, -(1 - np.exp(-theta*-x)*(1+theta+theta*-x) / (1 + theta)),  1 - np.exp(-theta*x)*(1+theta+theta*x) / (1 + theta) )
        #a = norm.ppf(u)
       # p2 = 0 + 1 * sc.erfinv(2*u-1)
        #import matplotlib.pyplot as plt
        #count, bins, ignored = plt.hist(cdf_truncated_around_mean.ravel(), 30, density=True)

        return ppf

    def lindley_ppf(self, u, theta, tol=1e-6, max_iter=100):
        # initial guess based on inverse of CDF formula
        x0 = np.log(1 / (1 - u)) / theta
        x = x0
        for i in range(max_iter):
            f = 1 + np.exp(-theta * x) * (1 + theta * x) - (1 - u)
            fp = -theta * np.exp(-theta * x) * \
                (1 + theta * x) - np.exp(-theta * x)
            x_new = x - f / fp
            if abs(x_new - x).any() < tol:
                return x_new
            x = x_new
        raise ValueError(
            "Failed to converge after {} iterations".format(max_iter))

    def lindley_new(self, theta):
        theta = np.clip(theta, 0.01, None)
        x = np.random.binomial(1, theta / (1 + theta))
        b = x * np.random.gamma(1, scale=theta) + \
            (1 - x) * np.random.gamma(2, scale=theta)
        return b

   
    def _compute_derivatives(self, betas, draws, betas_std=None, distribution=None):
        #N, N_draws, K = len(draws)/self.Ndraws, self.Ndraws, len(self._distribution)
        #N, D = draws.shape[0], draws.shape[1]
        N, R, Kr = draws.shape[0], draws.shape[2], draws.shape[1]
        der = dev.np.ones((N, Kr, R), dtype=draws.dtype)
        if len(self.none_handler(self.rdm_cor_fit)) == 0:
            Br_come_one = self.Br.copy()
            #Br_come_one = 
        else:

            Br_come_one = self.Br.copy()
        #betas_random = self._transform_rand_betas(betas, betas_std, draws)

        if any(set(distribution).intersection(['ln_normal', 'tn_normal'])):
            for k, dist_k in enumerate(distribution):
                if dist_k == 'ln_normal':
                    der[:, k, :] = Br_come_one[:, k, :]
                elif dist_k == 'tn_normal':
                    der[:, k, :] = 1*(Br_come_one[:, k, :] > 0)

        return der

    def _copy_size_display_as_ones(self, matrix):
        # grab the shape to copy
        please = matrix.shape
        der = dev.np.ones((please), dtype=matrix.dtype)
        return der

    def prepare_halton(self, dim, n_sample, draws, distribution, long=False, slice_this_way = None):
        #print('preparing storage for halton draws.......')

        sample_storage = self._generate_halton_draws(
            n_sample, draws, dim, long=long)
        #print('finished generation')
        # print('finished storage for halton draws.')
        if slice_this_way is None:
            group = 0
        
        
        if len(sample_storage.shape) == 2:
            for n_coef in range(len(distribution)):
                if distribution[n_coef] == 'normal':  # normal based
                    # todo check::
                    sample_storage[:, n_coef] = norm.ppf(
                        sample_storage[:, n_coef])
                elif distribution[n_coef] == 'gamma':
                    sample_storage[:, n_coef] = gamma.ppf(1,
                        sample_storage[:, n_coef])
                elif distribution[n_coef] == 'triangular':
                    draws_k = sample_storage[:, n_coef]
                    sample_storage[:, n_coef] = (np.sqrt(2 * draws_k) - 1) * (draws_k <= .5) + \
                        (1 - np.sqrt(2 * (1 - draws_k))) * (draws_k > .5)
                elif distribution[n_coef] == 'uniform':  # Uniform
                    sample_storage[:, n_coef] = 2*sample_storage[:, n_coef]-1
                elif distribution[n_coef] == 'lindley':
                    # print(self.sample_storage[:, n_coef])
                    sample_storage[:, n_coef] = self.lindley(
                        sample_storage[:, n_coef])
                else:
                    sample_storage[:, n_coef] = norm.ppf(
                        sample_storage[:, n_coef])
        elif len(sample_storage.shape) == 3:

            for n_coef in range(len(distribution)):
                slice_this_amount = 6
                cut_this_amount = 4
                if slice_this_way is None:
                    group = 0
                    slice_this_amount = 0
                    cut_this_amount = 0
    
                elif distribution[n_coef][:cut_this_amount] == 'trad':
                    
                    group = 0
                    
                else:
                   
                    group = 1
                if distribution[n_coef][slice_this_amount:] == 'normal':  # normal based
                    if group:
                        sample_storage[:, n_coef, :] = norm.ppf(sample_storage[slice_this_way, n_coef, :])
                    else: 
                        sample_storage[:, n_coef, :] = norm.ppf(
                        sample_storage[:, n_coef, :])
                elif distribution[n_coef][slice_this_amount:] == 'ln_normal':

                    mean = np.exp(0)
                    sd = np.exp(.5)
                    # mean = 0.5
                    #sd = .25
                    mu = np.log(
                        mean / np.sqrt(1 + (pow(sd, 2) / pow(mean, 2))))
                    std = np.sqrt(np.log(1 + (pow(sd, 2) / pow(mean, 2))))
                    mu = 0
                    
                  #  μ' = ln(μ) - (1/2) * ln(1 + (σ^2 / μ^2))
#σ' = sqrt(ln(1 + (σ^2 / μ^2)))
                    mu = np.log1p(0) - (1/2) * np.log1p(1 + (1 / 1))
                    sd = np.sqrt(np.log1p(1 + (1 / 1)))
                    mu = 0
                    sd = 0.25
                    #std = np.sqrt(sd)
                    #check = np.exp(norm.ppf(sample_storage[:, n_coef, :], mu, std))
                    #check2 = lognorm.ppf(sample_storage[:, n_coef, :], mu, std)
                    if group:
                         sample_storage[:, n_coef, :] = np.exp(
                            norm.ppf(sample_storage[slice_this_way, n_coef, :], mu, np.sqrt(sd))) 
                    else:
                        #sample_storage[:, n_coef, :] = np.exp(
                        #norm.ppf(sample_storage[:, n_coef, :], mu, np.sqrt(sd))) 
                       
                        sample_storage[:, n_coef, :] =  np.exp(
                        norm.ppf(sample_storage[:, n_coef, :], mu, np.sqrt(sd))) 
                    

                elif distribution[n_coef][slice_this_amount:] == 'tn_normal':
                    if group:
                        sample_storage[:, n_coef, :] =  norm.ppf(sample_storage[slice_this_way, n_coef, :]) *\
                        (norm.ppf(sample_storage[slice_this_way, n_coef, :]) > 0)
                    
                    else:
                        sample_storage[:, n_coef, :] =  norm.ppf(sample_storage[:, n_coef, :]) *\
                        (norm.ppf(sample_storage[:, n_coef, :]) > 0)
                  

                elif distribution[n_coef][slice_this_amount:] == 'gamma':
                    sample_storage[:, n_coef, :] = gamma.ppf(1,
                        sample_storage[:, n_coef, :])
                elif distribution[n_coef][slice_this_amount:] == 'triangular':
                    if group:
                        draws_k = sample_storage[slice_this_way, n_coef, :]
                    else:
                        draws_k = sample_storage[:, n_coef, :]
                    sample_storage[:, n_coef, :] = (np.sqrt(2 * draws_k) - 1) * (draws_k <= .5) + \
                        (1 - np.sqrt(2 * (1 - draws_k))) * (draws_k > .5)
                    #sample_storage[:, n_coef, :] = triang.ppf(sample_storage[:, n_coef, :], 0.5)
                elif distribution[n_coef][slice_this_amount:] == 'uniform':  # Uniform
                    if group:
                        sample_storage[:, n_coef, :] = 2 * \
                            sample_storage[slice_this_way, n_coef, :]-1
                    else:
                            
                        sample_storage[:, n_coef, :] = 2 * \
                            sample_storage[:, n_coef, :]-1

                elif distribution[n_coef][slice_this_amount:] == 'lindley':
                    # print(self.sample_storage[:, n_coef])
                     sample_storage[:, n_coef, :] = self.lindley(
                        sample_storage[:, n_coef, :])
                    #sample_storage[:, n_coef, :] = self.lindley_inv_t(
                     #   sample_storage[:, n_coef, :], 1)
                    #sample_storage[:, n_coef, :] = self.lindley_new(sample_storage[:, n_coef, :])
                    #sample_storage[:, n_coef, :] = self.lindley_inv_t(sample_storage[:, n_coef, :],1)
                else:
                    sample_storage[:, n_coef, :] = norm.ppf(
                        sample_storage[:, n_coef, :])

       # print('returning sample')
        return sample_storage
