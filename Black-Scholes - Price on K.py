# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 22:11:15 2017

@author: choun
"""

# references:
# http://gosmej1977.blogspot.com/2013/02/black-and-scholes-formula.html
# http://stackoverflow.com/questions/14050824/add-sum-of-values-of-two-lists-into-new-list
# http://stackoverflow.com/questions/22276066/python-plot-multiple-graphs-on-the-same-figure
# http://stackoverflow.com/questions/13545388/plot-data-from-csv-file-with-matplotlib
import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt


# Variables
S0 = 1409.22  # put dashed line at underlying price
K = np.arange(600, 2000, 100)
r = 0.1
sigma = 15
t = 23 / 365


# Black-Scholes Call Model
def d1(S0, K, r, sigma, t):
    return(np.log(S0 / K) + (r + sigma ** 2/2) * t) / (sigma * np.sqrt(t))


def d2(S0, K, r, sigma, t):
    return(np.log(S0 / K) + (r - sigma ** 2/2) * t)/(sigma * np.sqrt(t))


def BlackScholes(type, S0, K, r, sigma, t):
    if type == "P":  # if == "P", then Put; otherwise, call
        return (K * np.exp(-r * t) * ss.norm.cdf(-d2(S0, K, r, sigma, t)) -
                S0 * ss.norm.cdf(-d1(S0, K, r, sigma, t)))
    else:
        return (S0 * ss.norm.cdf(d1(S0, K, r, sigma, t)) -
                K * np.exp(-r * t) * ss.norm.cdf(d2(S0, K, r, sigma, t)))


# Import Data
#x, y = np.genfromtxt('C:/Users/choun/OneDrive/Documents/Antioch/Senior ' +
 #                    'Project/Code/Data Sets/S&P 500/Underlying - Jan 01' + 
  #                   ' 2008.csv - formatted', unpack=True,
   #                  delimiter=',')


plt.xlabel('K', fontsize=16)
plt.ylabel('Price', fontsize=16)
plt.plot(K, BlackScholes('C', S0, K, r, sigma, t), color='blue')
#plt.plot(x, y, "o", color='red')
