#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 13:43:39 2017

@author: katiekessler
"""

import pandas as pd
import matplotlib.pyplot as plt

sl = pd.read_csv('ACI - SL.csv')
avg = pd.read_csv('ACI - avg.csv')
colors = ['b','g','r','c','m','y','k', '#9033FF','#FB9513', '#92FB13','#3A5826','#89A9AC','#7A041D']

for j in range(4):
    for i in range(13):
        sl_list = sl[sl.columns[i+2]].tolist()
        avg_list = avg[avg.columns[i+2]].tolist()
        
        plt.title(str(list(sl)[i+2]) + " vs AVG " +  str(list(avg)[i+2]) + " Season " + str(j+1))
        plt.xlabel(str(list(sl)[i+2]))
        plt.ylabel("AVG " + str(list(avg)[i+2]))
        plt.scatter(sl_list[j::4], avg_list[j::4], color=colors[i])
        plt.show()


