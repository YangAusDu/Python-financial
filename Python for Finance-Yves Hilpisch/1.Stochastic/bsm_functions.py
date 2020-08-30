#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 16:34:48 2020

@author: D.Y.
"""
import numpy as np
import math
from scipy import stats

'''
parameters:
=========================
S0:  
    initial stock price
K:  
    strike price
T:   
    time to maturity
r:   
    risk free rate
sigma:
    volatility
sigma_est:
    estimated sigma
itr:
    iteration
    '''

def bsm_call_value(S0, K, T, r, sigma):
    '''the implementation of BSM'''
    d1 = (np.log(S0/K) + (r + 0.5 * sigma ** 2) * T ) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    C0 = S0 * stats.norm.cdf(d1, 0, 1) - K * math.exp(-r) * stats.norm.cdf(d2)
    
def bsm_vega(S0,K, T, r, sigma):
    S0 = float(S0)
    d1 = (np.log(S0/K) + (r + 0.5 * sigma ** 2) * T ) / (sigma * np.sqrt(T))
    vega = S0 * stats.norm.cdf(d1, 0, 1) * math.sqrt(T)
    return vega

def bsm_call_imp_vol(S0, K, T, r, C0, sigma_est, itr = 100):
    for i in range(itr):
        sigma_est -= (bsm_call_value(S0, K, T, r, sigma_est)-C0) / 
            bsm_vega(S0, K, T, r, sigma_est)
    return sigma_est
        
    
