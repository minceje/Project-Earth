import numpy as np
import pandas as pd
from sklearn.svm import SVR

# can easily change the file names here
sl = pd.read_csv('SeaLevel.csv')
avg = pd.read_csv('Avg.csv')

# use data from the first column (ALA region) in each file, again this can be changed here
sl_list = sl[sl.columns[0]].tolist()
avg_list = avg[avg.columns[0]].tolist()

# restrict data to season 1 of each year only
sl_list = sl_list[0::4]
avg_list = avg_list[0::4]

# convert to 1D numpy arrays for use in training models
avg_arr = np.array(avg_list).reshape(-1, 1)
sl_arr = np.array(sl_list).ravel()

# take the first 40 data points to use as our training set
x_train = avg_arr[:40]
y_train = sl_arr[:40]

# the last 16 points become out testing set (we can change this separation as well)
x_test = avg_arr[40:]
y_test = sl_arr[40:]

"""SVM Regression"""
svmreg = SVR()
svmreg.fit(x_train, y_train)

pred = svmreg.predict([x_test[15]])
print("Predicted value: ", pred)
print("Expected value: ", y_test[15])
print("R-squared: ", svmreg.score(x_test, y_test))
