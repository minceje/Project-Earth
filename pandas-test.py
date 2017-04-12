import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

sl = pd.read_csv('5yrSeaLevel.csv')
avg = pd.read_csv('5yrAvg.csv')

sl_list = sl[sl.columns[0]].tolist()
avg_list = avg[avg.columns[0]].tolist()

sl_list = sl_list[0:200]
avg_list = avg_list[0:200]

sl_list = [int(i * 100) for i in sl_list]
avg_list = [int(j * 100) for j in avg_list]

sl_arr = np.array(sl_list).reshape(-1, 1)
avg_arr = np.array(avg_list).reshape(-1, 1)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(avg_arr, sl_arr)

pred = knn.predict(61)
print("Predicted sea level given an index of 61 (0.61 * 100): ", pred)
print("Expected output: -409 (-4.09 * 100 for ALA 2016 Season 3)")
