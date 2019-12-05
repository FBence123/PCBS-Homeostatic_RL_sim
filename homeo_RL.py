# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 13:12:22 2019

@author: Bence Farkas
"""

import matplotlib.pyplot as plt
import scipy.stats as scista
import numpy as np

## Set parameters

A = 500
N = 10
h_star = 0
m = 2
n = 4
gamma = 0.96
alpha = 0.2
beta = 0.1
Q_tol = np.zeros((N+1,A))
Q_nul = np.zeros((N+1,A))
Q_tol_a = 0
Q_nul_a = 23
Q_tol[0,:] = Q_tol_a
Q_nul[0,:] = Q_nul_a
temp = np.zeros((N,49,A))
p_tol = np.zeros((N,A))
c_l = np.zeros((N,A))

for a in range(A):
    Q_tol_a = 0
    Q_nul_a = 23
    for t in range(N):
        
        # Make choice
        p_tol[t,a] = 1 / (1 + np.exp(beta * (Q_nul_a - Q_tol_a)))
        c = int(np.random.rand() < p_tol[t,a])
    
        # Ethanol injection
        x = np.arange(1/47,1,1/47)
        y = scista.beta.pdf(x = x, a = 1.35, b = 6)
        y = list(np.concatenate((np.zeros(3), y)))
        y = [((y[j]-min(y))*14)/max(y)-min(y) for j in range(len(y))]
        temp[t,:,a] = [temp[t,j,a] - y[j] for j in range(temp.shape[1])]
        
        # Tolerance response if chosen
        if c == 1:
           x = np.arange(1/50,1,1/50)
           y = list(scista.beta.pdf(x = x, a = 2.2, b = 6))
           y = [((y[j]-min(y))*12)/max(y)-min(y) for j in range(len(y))]
           y[0] = 0
           temp[t,:,a] = [temp[t,j,a] + y[j] for j in range(temp.shape[1])]
            
        # Calculate drives and rewards
        D = [pow((abs((h_star - temp[t,j,a])))**n,1/m) for j in range(temp.shape[1])]
        R = sum([gamma**j * (D[j] - D[j+1]) for j in range(len(D)-1)])
        
        # Q-learning
        if c == 1:
            Q_tol_a += alpha* (R - Q_tol_a)
        else:
            Q_nul_a += alpha* (R - Q_nul_a)
        Q_tol[t+1,a] = Q_tol_a
        Q_nul[t+1,a] = Q_nul_a
        c_l[t,a] = c


plt.figure()
temp_plot = temp.mean(2)
plt.plot(temp_plot.mean(1))
plt.figure()
plt.plot(p_tol.mean(1))