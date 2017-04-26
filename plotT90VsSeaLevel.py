#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 20:02:26 2017

@author: katiekessler
"""


import pandas as pd
import matplotlib.pyplot as plt

sl = pd.read_csv('ACI - SL.csv')
t90 = pd.read_csv('ACI - t90.csv')
colors = ['b','g','r','c','m','y','k', '#9033FF','#FB9513', '#92FB13','#3A5826','#89A9AC','#7A041D']

for j in range(4): #go through every season
    for i in range(13): #go through every region
        sl_list = sl[sl.columns[i+2]].tolist()
        t90_list = t90[t90.columns[i+2]].tolist()
        
        plt.title(str(list(t90)[i+2])+ " vs " + str(list(sl)[i+2]) + " Season " + str(j+1))
        plt.xlabel(str(list(t90)[i+2]))
        plt.ylabel(str(list(sl)[i+2]))
        
        plt.scatter(t90_list[j::4], sl_list[j::4], color=colors[i])
        plt.show()