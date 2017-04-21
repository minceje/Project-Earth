#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 14:06:01 2017

@author: karlmaier
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

sl = pd.read_csv('ACI - SL.csv')
avg = pd.read_csv('ACI - avg.csv')
colors = ['b','g','r','c','m','y','k', '#9033FF','#FB9513', '#92FB13','#3A5826','#89A9AC','#7A041D']

#for j in range(4):#seasons
#for i in range(13):#regions
sl_list = sl[sl.columns[11]].tolist()
avg_list = avg[avg.columns[11]].tolist()
x0 = sl_list[3::4]
y0 = avg_list[3::4]

x = np.array(x0).reshape(-1,1)
y = np.array(y0).reshape(-1,1)

x_train = x[:-2]
y_train = y[:-2]

x_test = x[-2:]
y_test = y[-2:]

regr = linear_model.LinearRegression()

regr.fit(x_train, y_train)

print('Coefficients: ' + str(regr.coef_))

pred = regr.predict([.5])
print pred
print("R-squared: ", regr.score(x_test, y_test))
plt.title("AVG " + str(list(avg)[11])+ " vs " + str(list(sl)[11]) + " Season " + str(4))
plt.xlabel("AVG " + str(list(avg)[11]))
plt.ylabel(str(list(sl)[11]))
plt.scatter(x, y, color='black')
plt.plot(x_test, regr.predict(x_test), color='blue', linewidth=3)
plt.show()