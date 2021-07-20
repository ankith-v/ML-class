
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('C:\\Users\\rohan\\Desktop\\lab\\ML\\Supervised\\DecisionTreeReg\\IceCreamData.csv')
# print(dataset.head())
# print(dataset.shape)
X = dataset['Temperature'].values
y = dataset['Revenue'].values


# Splitting dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1)


# Training DTR on training dataset 
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor()
regressor.fit(X_train.reshape(-1,1), y_train.reshape(-1,1))


# predicting
y_pred = regressor.predict(X_test.reshape(-1,1))


# Compare
df = pd.DataFrame({'Real values':(y_test.reshape(-1)), 'Predicted values':y_pred})
print(df)


X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X_test, y_test, color = 'red')
plt.scatter(X_test, y_pred, color = 'green')
plt.title("Decision tree")
plt.xlabel('Temperature')
plt.ylabel("Revenue")
plt.show()

# plt.plot(X_grid, regressor.predict(X_grid),color = 'black')
# plt.title("Decision tree")
# plt.xlabel('Temperature')
# plt.ylabel("Revenue")
# plt.show()
