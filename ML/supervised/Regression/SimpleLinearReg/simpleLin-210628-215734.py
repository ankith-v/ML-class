import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('C:\\Users\\rohan\\Desktop\\lab\\ML\\Supervised\\SimpleLinearReg\\Salary_Data.csv')
print(dataset.head())

X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values
# print(X)
# print(y)

# print(dataset.shape)

# Splitting data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)



# TRainng
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)


# predicting
y_pred = regressor.predict(X_test)


df = pd.DataFrame({'Real values':y_test, 'Predicted values':y_pred})
print(df)

from sklearn.metrics import r2_score
print('R2 score:', r2_score(y_test, y_pred))


plt.scatter(X_test, y_test, color='red')
plt.scatter(X_test, y_pred, color='green')
plt.plot(X_train, regressor.predict(X_train), color='black')
plt.title('Salary vs Exp')
plt.xlabel('YearsExp')
plt.ylabel('Salary')
plt.show()
