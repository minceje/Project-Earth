import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn import linear_model

# can easily change the file names here
sl = pd.read_csv('./CSV Data Set Files for Code/ACI - SL.csv')
avg = pd.read_csv('./CSV Data Set Files for Code/ACI - avg.csv')

# use data from the first column (ALA region) in each file, again this can be changed here
sl_list = sl[sl.columns[2]].tolist()
avg_list = avg[avg.columns[2]].tolist()

# convert floats to ints for the classifier (may not be needed with different algorithms)
sl_list = [int(i * 100) for i in sl_list]
avg_list = [int(j * 100) for j in avg_list]

# convert to 1D numpy arrays for use in training models
avg_arr = np.array(avg_list).reshape(-1, 1)
sl_arr = np.array(sl_list).ravel()

# take the first 200 data points to use as our training set
x_train = avg_arr[:200]
y_train = sl_arr[:200]

# the last ~20 points become out testing set (we can change this separation as well)
x_test = avg_arr[200:]
y_test = sl_arr[200:]

"""K-Nearest Neighbors Test"""
# NOTE: this is meant as a classifier algorithm and is not a suitable application of knn
knn = KNeighborsClassifier(n_neighbors=3)  # Create K-Nearest model object
knn.fit(x_train, y_train)  # fit model to training data

pred = float(knn.predict(61) / 100)  # test by predicting a single value
print("Predicted sea level given an index of 0.61: ", pred)
print("Expected output: -4.09, SL ALA 2016 Season 3")

"""Linear Regression Test"""
regr = linear_model.LinearRegression()  # Create a linear regressor object

regr.fit(x_train, y_train)  # fit the model over the training data

print("Coefficients: " + str(regr.coef_))  # check the coefficients, little utility here given the overall results

pred = float(regr.predict(61) / 100)  # test by predicting a single value
print("Predicted sea level given an index of 0.61: ", pred)
print("Expected output: -4.09, SL ALA 2016 Season 3")

# attempt at calculating mean squared error for our model given predictive performance on our testing data
print("Mean squared error: ", np.mean((regr.predict(x_test) - y_test) ** 2))
print("Variance score: ", regr.score(x_test, y_test))
