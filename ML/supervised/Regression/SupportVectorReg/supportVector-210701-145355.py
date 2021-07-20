
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('C:\\Users\\rohan\\Desktop\\lab\\ML\\Supervised\\SupportVectorReg\\SampleData.csv')
# print(dataset.head())
print(dataset.shape)

X = dataset.iloc[:,0].values
y = dataset.iloc[:,1].values
# print(X)
# print(y)


# Feature scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X.reshape(-1,1))
y = sc_y.fit_transform(y.reshape(-1,1))
# print(X)
# print(y)


# traning
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)
# print(y_test)


# training the SVR on training set 
from sklearn.svm import SVR
regressor = SVR(kernel='rbf')
regressor.fit(X_train.reshape(-1,1), y_train.reshape(-1,1))


# predictng
y_pred = regressor.predict(X_test)
y_pred = sc_y.inverse_transform(y_pred)
# print(y_pred)


# Compare
df = pd.DataFrame({'Real values':sc_y.inverse_transform(y_test.reshape(-1)), 'Predicted values':y_pred})
print(df)


X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(sc_X.inverse_transform(X_test), sc_y.inverse_transform(y_test), color = 'red')
plt.scatter(sc_X.inverse_transform(X_test), y_pred, color = 'green')


# plt.plot(X_grid, regressor.predict(X_grid),color = 'black')
plt.title("SVR")
plt.xlabel('Hours')
plt.ylabel("Marks")
plt.show()





# Standardize features by removing the mean and scaling to unit variance
# The standard score of a sample x is calculated as:
# z = (x - u) / s
# where u is the mean of the training samples or zero if with_mean=False, 
# and s is the standard deviation of the training samples or one if with_std=False.











# arange for creating a range of values from min value of X to max value of X 
# with a difference of 0.01 between two consecutive values
# X_grid = np.arange(min(X), max(X), 0.01)
  
# reshape for reshaping the data into a len(X_grid)*1 array, i.e. to make
# a column out of the X_grid values
# X_grid = X_grid.reshape((len(X_grid), 1)) 