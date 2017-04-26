#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 14:00:21 2017

@author: katiekessler
"""

import pandas as pd
import matplotlib.pyplot as plt

sl = pd.read_csv('ACI - SL.csv')
cdd = pd.read_csv('ACI - CDD.csv')
colors = ['b','g','r','c','m','y','k', '#9033FF','#FB9513', '#92FB13','#3A5826','#89A9AC','#7A041D']

for j in range(4): #go through every season
    for i in range(13): #go through every region
        sl_list = sl[sl.columns[i+2]].tolist()
        cdd_list = cdd[cdd.columns[i+2]].tolist()
        
        plt.title(str(list(cdd)[i+2])+ " vs " + str(list(sl)[i+2]) + " Season " + str(j+1))
        plt.xlabel(str(list(cdd)[i+2]))
        plt.ylabel(str(list(sl)[i+2]))
        
        plt.scatter(cdd_list[j::4], sl_list[j::4], color=colors[i])
        plt.show()
