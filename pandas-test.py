import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

sl = pd.read_csv('5yrSeaLevel.csv')
avg = pd.read_csv('5yrAvg.csv')
# print(sl.tail())
# print(avg.tail())
# print(sl[0:10])
# ca = np.array(df['t90 USC 5'].tolist())
# print(ca)
# print(type(ca))
sl_list = sl[sl.columns[0]].tolist()
avg_list = avg[avg.columns[0]].tolist()

sl_list = sl_list[0:200]
avg_list = avg_list[0:200]

sl_list = [int(i * 100) for i in sl_list]
avg_list = [int(j * 100) for j in avg_list]
print(sl_list)

sl_arr = np.array(sl_list).reshape(-1, 1)
avg_arr = np.ravel(avg_list)

# knn = KNeighborsClassifier(n_neighbors=3)
# knn.fit(avg_list, sl_list)
#
# pred = knn.predict(70)
# print("Predicted sea level given an index of 0.79: ", pred)
# print("Expected output: -0.60  (USA 2016 Season 3)")
