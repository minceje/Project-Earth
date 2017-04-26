#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 22:36:46 2017

@author: karlmaier
"""

"""
Created on Wed Apr 19 14:06:01 2017

@author: karlmaier
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model


sl = pd.read_csv('CSV Data Set Files for Code/ACI - SL.csv')
t10 = pd.read_csv('CSV Data Set Files for Code/ACI - CDD.csv')
colors = ['b','g','r','c','m','y','k', '#9033FF','#FB9513', '#92FB13','#3A5826','#89A9AC','#7A041D']

for j in range(4):
    for i in range(13):
        sl_list = sl[sl.columns[i+2]].tolist()
        t10_list = t10[t10.columns[i+2]].tolist()

        xo = sl_list[j::4]
        yo = t10_list[j::4]

        x = np.array(xo).reshape(-1,1)
        y = np.array(yo).reshape(-1,1)

        x_train = x[:-2]
        y_train = y[:-2]

        x_test = x[-2:]
        y_test = y[-2:]

        regr = linear_model.LinearRegression()

        regr.fit(x_train, y_train)

        plt.title(str(list(t10)[i+2])+ " vs " + str(list(sl)[i+2]) + " Season " + str(j+1))
        plt.xlabel(str(list(t10)[i+2]))
        plt.ylabel(str(list(sl)[i+2]))
        

        print("R-Squared" + str(regr.score(x_test,y_test)))
        

        

        plt.scatter(x, y, color='black')
        plt.plot(x_test, regr.predict(x_test), color='blue', linewidth=3)
        plt.show()
