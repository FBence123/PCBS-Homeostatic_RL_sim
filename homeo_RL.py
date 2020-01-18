# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 13:12:22 2019

@author: Bence Farkas
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patch
import scipy.stats as scista
import numpy as np

## Set parameters

#Parameters of the simulation
A = 500 #Number of simulated agents
N = 10 #Number of simulated trials

#Parameters of the RL model
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
choice_l = np.zeros((N,A))

##Useful functions to model the experiment

def ethanol (norm): #ethanol response, normalizes a beta distribution to an arbitrary range
    x = np.arange(1/47,1,1/47)
    y = scista.beta.pdf(x = x, a = 1.35, b = 6)
    y = list(np.concatenate((np.zeros(3), y)))
    y = [-(((y[j]-min(y))*norm)/max(y)-min(y)) for j in range(len(y))]
    return y

def tolerance (norm): #tolerance response, normalizes a beta distribution to an arbitrary range
    x = np.arange(1/50,1,1/50)
    y = list(scista.beta.pdf(x = x, a = 2.2, b = 6))
    y = [((y[j]-min(y))*norm)/max(y)-min(y) for j in range(len(y))]
    y[0] = 0
    return y

## Perform the simulations

for a in range(A):
    Q_tol_a = 0
    Q_nul_a = 23 #Initial values chosen to qualitatively match the study
    for t in range(N):
        
        # Make choice
        p_tol[t,a] = 1 / (1 + np.exp(beta * (Q_nul_a - Q_tol_a)))
        choice = int(np.random.rand() < p_tol[t,a])
    
        # Ethanol injection
        if t != 8:
            y = ethanol(14)
            temp[t,:,a] = [temp[t,j,a] + y[j] for j in range(temp.shape[1])]
        
        # Tolerance response if chosen
        if choice == 1:
           y = tolerance(12)
           temp[t,:,a] = [temp[t,j,a] + y[j] for j in range(temp.shape[1])]
            
        # Calculate drives and rewards
        D = [pow((abs((h_star - temp[t,j,a])))**n,1/m) for j in range(temp.shape[1])]
        R = sum([gamma**j * (D[j] - D[j+1]) for j in range(len(D)-1)])
        
        # Q-learning
        if choice == 1:
            Q_tol_a += alpha* (R - Q_tol_a)
        else:
            Q_nul_a += alpha* (R - Q_nul_a)
        Q_tol[t+1,a] = Q_tol_a
        Q_nul[t+1,a] = Q_nul_a
        choice_l[t,a] = choice

## Create the plots

#Ethanol injection plot (Figure 3B)
y = ethanol(1.4)
plt.figure()
plt.plot(np.arange(0,49),y,"k-")
plt.hlines(0,0,49,colors = "silver", linestyles = "dashed")
plt.vlines([2,3,4,5,6],-1.5,1.5,colors = ["red","silver","silver","silver","silver"])
plt.annotate("Ethanol injection",xy=(2,0.5),xytext=(12,1), arrowprops=dict(facecolor='red', shrink=0.05, connectionstyle="angle3,angleA=0,angleB=90"))
plt.xticks(np.arange(0,49,6),np.arange(0,25,3))
plt.ylim([-1.5,1.5])
plt.xlabel("Hour")
plt.ylabel("Change of temperature")
plt.title("Ethanol injection")

#Tolerance response plot (Figure 3D)
y = tolerance(1.2)
plt.figure()
plt.plot(np.arange(0,49),y,"k-")
plt.hlines(0,0,49,colors = "silver", linestyles = "dashed")
plt.vlines([0,3,4,5,6],-1.5,1.5,colors = ["green","silver","silver","silver","silver"])
plt.annotate("Tolerance response",xy=(0,-0.5),xytext=(12,-1), arrowprops=dict(facecolor='green', shrink=0.05, connectionstyle="angle3,angleA=0,angleB=90"))
plt.xticks(np.arange(0,49,6),np.arange(0,25,3))
plt.ylim([-1.5,1.5])
plt.xlabel("Hour")
plt.ylabel("Change of temperature")
plt.title("Tolerance response")

#Tolerance response + ethanol injection plot (Figure 3F)
y = ethanol(1.4)
y2 = tolerance(1.2)
y = [y[i] + y2[i] for i in range(len(y))]
plt.figure()
plt.plot(np.arange(0,49),y,"k-")
plt.hlines(0,0,49,colors = "silver", linestyles = "dashed")
plt.vlines([0,2,3,4,5,6],-1.5,1.5,colors = ["green","red","silver","silver","silver","silver"])
plt.annotate("Ethanol injection",xy=(2,-0.7),xytext=(12,-0.7), arrowprops=dict(facecolor='red', shrink=0.05, connectionstyle="angle3,angleA=0,angleB=90"))
plt.annotate("Tolerance response",xy=(0,-1),xytext=(12,-1), arrowprops=dict(facecolor='green', shrink=0.05, connectionstyle="angle3,angleA=0,angleB=90"))
plt.annotate("30'",xy=(3,1.3),xytext=(15,1.3), arrowprops=dict(facecolor='silver', shrink=0.05, connectionstyle="angle3,angleA=0,angleB=90"))
plt.annotate("60'",xy=(4,1.1),xytext=(15,1.1), arrowprops=dict(facecolor='silver', shrink=0.05, connectionstyle="angle3,angleA=0,angleB=90"))
plt.annotate("90'",xy=(5,0.9),xytext=(15,0.9), arrowprops=dict(facecolor='silver', shrink=0.05, connectionstyle="angle3,angleA=0,angleB=90"))
plt.annotate("120'",xy=(6,0.7),xytext=(15,0.7), arrowprops=dict(facecolor='silver', shrink=0.05, connectionstyle="angle3,angleA=0,angleB=90"))
plt.xticks(np.arange(0,49,6),np.arange(0,25,3))
plt.ylim([-1.5,1.5])
plt.xlabel("Hour")
plt.ylabel("Change of temperature")
plt.title("Tolerance response + Ethanol injection")

#Response probability plot (Figure 3C)
plt.figure()
plt.plot(np.arange(1,11),p_tol.mean(1),"k-")
plt.plot(np.arange(1,11),p_tol.mean(1),"ko")
plt.ylim([0,1])
plt.xticks(np.arange(1,11),["1","2","3","4","5","6","7","8","E1","R1"])
plt.gca().add_patch(patch.Polygon([[8.5,0],[9.5,0],[9.5,1],[8.5,1]],color = "silver"))
plt.xlabel("Blocks")
plt.ylabel("Response probability")

#Temperature changes plot (Figure 3C)
figtemp = temp.mean(2)
figtemp = figtemp[:,3:7]
plt.figure()
plt.xlim([-1,40])
plt.ylim([-15,15])
for n in range(N):
    plt.plot(range(n*4,(n*4)+4),figtemp[n,:],"ko")
    plt.plot(range(n*4,(n*4)+4),figtemp[n,:],"k-")
plt.hlines(0,-1,40,colors = "silver", linestyles = "dashed")
plt.gca().add_patch(patch.Polygon([[32,-15],[35,-15],[35,15],[32,15]],color = "silver"))
plt.xticks(np.arange(1.5,40,4),["1","2","3","4","5","6","7","8","E1","R1"])
plt.yticks(range(-15,16,5),[i/10 for i in range(-15,16,5)])
plt.annotate("30'",xy=(0,-11),xytext=(6,12.5), arrowprops=dict(facecolor='red', shrink=0.05, connectionstyle="angle3,angleA=0,angleB=90"))
plt.annotate("60'",xy=(1,-13),xytext=(6,10.5), arrowprops=dict(facecolor='red', shrink=0.05, connectionstyle="angle3,angleA=0,angleB=90"))
plt.annotate("90'",xy=(2,-13.5),xytext=(6,8.5), arrowprops=dict(facecolor='red', shrink=0.05, connectionstyle="angle3,angleA=0,angleB=90"))
plt.annotate("120'",xy=(3,-13),xytext=(6,6.5), arrowprops=dict(facecolor='red', shrink=0.05, connectionstyle="angle3,angleA=0,angleB=90"))
plt.xlabel("Blocks")
plt.ylabel("Change of temperature")