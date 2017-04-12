import numpy as np
import pandas as pd
# from sklearn.neighbors import KNeighborsClassifier

sl = pd.read_csv('5yrSeaLevel.csv')
avg = pd.read_csv('5yrAvg.csv')
print(sl.tail())
print(avg.tail())
print(sl[0:10])
# ca = np.array(df['t90 USC 5'].tolist())
# print(ca)
# print(type(ca))
sl_arr = np.array(sl[0:200])
avg_arr = np.array(avg[0:200])

# knn = KNeighborsClassifier(n_neighbors=3)
# knn.fit(avg_arr, sl_arr)
#
# pred = knn.predict(0.79)
# print("Predicted sea level given an index of 0.79: ", pred)
# print("Expected output: -0.60  (USA 2016 Season 3)")
