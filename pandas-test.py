import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn import linear_model

sl = pd.read_csv('5yrSeaLevel.csv')
avg = pd.read_csv('5yrAvg.csv')

sl_list = sl[sl.columns[0]].tolist()
avg_list = avg[avg.columns[0]].tolist()

# sl_list = sl_list[0:200]
# avg_list = avg_list[0:200]

sl_list = [int(i * 100) for i in sl_list]
avg_list = [int(j * 100) for j in avg_list]

avg_arr = np.array(avg_list).reshape(-1, 1)
sl_arr = np.array(sl_list).ravel()

x_train = avg_arr[:200]
y_train = sl_arr[:200]

x_test = avg_arr[200:]
y_test = sl_arr[200:]

"""K-Nearest Neighbors Test"""
# knn = KNeighborsClassifier(n_neighbors=3)
# knn.fit(x_train, y_train)
#
# pred = float(knn.predict(61) / 100)
# print("Predicted sea level given an index of 0.61: ", pred)
# print("Expected output: -4.09, SL ALA 2016 Season 3")

"""Linear Regression Test"""
# regr = linear_model.LinearRegression()
#
# regr.fit(x_train, y_train)
#
# print("Coefficients: " + str(regr.coef_))
#
# pred = float(regr.predict(61) / 100)
# print("Predicted sea level given an index of 0.61: ", pred)
# print("Expected output: -4.09, SL ALA 2016 Season 3")
#
# # I dunno what these are really, but they look pretty bad
# print("Mean squared error: ", np.mean((regr.predict(x_test) - y_test) ** 2))
# print("Variance score: ", regr.score(x_test, y_test))
