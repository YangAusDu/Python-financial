#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 23:01:13 2020

@author: D.Y
"""

# -*- coding: utf-8 -*-



import numpy as np
import numpy.random as npr
import math

def gen_sn(M, I, anti_paths = True, mo_match = True):
    """
    M: INT
        number of time interval for discretization
    I: INT
        number of paths to be simulated
    anti_paths: BOOLEAN
        use of antithetic variates
    mo_macth:BOOLEAN
        use of moment matching
    
    RETURN:
    =======
    M+1 by I matrix of random number.        
    """
    if anti_paths == True:
        sn = npr.standard_normal((M+1, int(I/2)))
        sn = np.concatenate((sn, -sn),axis = 1)
    else:
        sn = npr.standard_normal((M,I))
        
    if mo_match == True:
        sn = (sn - sn.mean())/sn.std()
    return sn


def gbm_mcs_stat(K):
    '''valuation of Europian call option 
    by Monte Carlo

    K: float
        strike price
    RETURN:
    ======
    Estimated present value of the option
    '''
    s0, r, sigma, T, I = 100, 0.05, 0.25, 1.0, 50000
    sn = gen_sn(1,I)
    #simulating stock price
    st = s0 * np.exp((r-0.5 * sigma ** 2) * T + sigma*math.sqrt(T)*sn[1])
    hT = np.maximum(st - K, 0)
    c0 = math.exp(-r*T) * np.mean(hT)
    return c0

    
def gbm_mcs_dyna(K, option = 'call'):
    '''valuation of Europian call option 
    by Monte Carlo
    
    K: float
        strike price
    RETURN:
    ======
    Estimated present value of the option
    '''
    S0, r, sigma, T, I , M= 100, 0.05, 0.25, 1.0, 50000, 50
    dt = T/M
    S = np.zeros((M+1,I))
    S[0] = S0
    sn = gen_sn(M,I)
    for t in range(1, M+1):
        S[t] = S[t-1] * np.exp(
            (r-0.5*sigma **2)*dt + sigma * math.sqrt(dt)* sn[t])
    if option == 'call':
        hT = np.maximum(S[-1]-K,0)
    else:
        hT = np.maximum(k-S[-1],0)
    c0 = math.exp(-r*T)*np.mean(hT)
    return c0

