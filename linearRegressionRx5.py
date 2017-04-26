#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 13:52:33 2017

@author: katiekessler
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

sl = pd.read_csv('ACI - SL.csv')
rx5 = pd.read_csv('ACI - rx5.csv')
colors = ['b','g','r','c','m','y','k', '#9033FF','#FB9513', '#92FB13','#3A5826','#89A9AC','#7A041D']

for j in range(4): #go through every season
    for i in range(13): #go through every region
        sl_list = sl[sl.columns[i+2]].tolist()
        rx5_list = rx5[rx5.columns[i+2]].tolist()
        
        xo1 = sl_list[j::4]
        yo1 = rx5_list[j::4]

        #linear regression
        x = np.array(xo1).reshape(-1,1)
        y = np.array(yo1).reshape(-1,1)

        x_train = x[:-2]
        y_train = y[:-2]

        x_test = x[-2:]
        y_test = y[-2:]

        regr = linear_model.LinearRegression()

        regr.fit(x_train, y_train)

        print("R-squared: " + str(list(rx5)[i+2]) + " " + str(regr.score(x_test,y_test)))

        #print('Coefficients: ' + str(regr.coef_))

        #pred = regr.predict([10])
        #print 'Linear Regression ' + str(pred)

        """plt.scatter(x, y, color='black')
        plt.plot(x_test, regr.predict(x_test), color='blue', linewidth=3)
        plt.show()
"""
        
        plt.title(str(list(rx5)[i+2])+ " vs " + str(list(sl)[i+2]) + " Season " + str(j+1))
        plt.xlabel(str(list(rx5)[i+2]))
        plt.ylabel(str(list(sl)[i+2]))
        
        plt.scatter(rx5_list[j::4], sl_list[j::4], color=colors[i])
        plt.plot(x_test, regr.predict(x_test), color='blue', linewidth=3)
        plt.show()







    

