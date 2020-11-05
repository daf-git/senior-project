# -*- coding: utf-8 -*-
"""
Created on Mon May 15 00:30:29 2017

@author: choun
"""
import numpy as np
import matplotlib.pyplot as plt


S0 = 75.93  # stock price
K = np.arange(54, 83, 1)  # strike price


# Binomial Model
price = np.maximum(S0 - K, 0)

    
# Import Data
x, y = np.genfromtxt('C:/Users/choun/OneDrive/Documents/Antioch/Senior ' +
                     'Project/Code/Data Sets/pricekdata.csv', unpack=True,
                     delimiter=',')


plt.xlabel('K', fontsize=14)
plt.ylabel('Price', fontsize=14)
plt.plot(K, price)  # price on k
plt.plot(x, y, "o", color='darkgreen')  # Real Data
    