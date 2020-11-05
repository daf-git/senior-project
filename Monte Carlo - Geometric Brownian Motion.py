# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 16:03:42 2018

@author: nchou
"""

# Import
import matplotlib.pyplot as plt
import numpy as np

# Variables
P = 10000 # Principal
mu = .0666666 # Expected Return
sigma = 0.15 # Risk
t = 10 # Time in Years
t_int = .05 # Size of Each Calculation Interval
trials = 1000 # Number of Trials to Simulate

# Technical Junk
n = round(t/t_int) # Convert t/dt to integer for "l" and distribution sampling
dt = np.linspace(0, t, n) # Linear Space from 0, t in intervals of t/dt

# Geometric Brownian Motion Loop
for ii in range(trials):
    dW = np.cumsum(np.random.standard_normal(size=n))*np.sqrt(t_int) # Sampling from Normal Distribution
    k = (mu-0.5*sigma**2)*dt + sigma*dW # Geometric Brownian Motion
    S = P*np.exp(k) # Growth of Principal
    plt.plot(dt, S)

plt.show(plt.plot(dt, S))
