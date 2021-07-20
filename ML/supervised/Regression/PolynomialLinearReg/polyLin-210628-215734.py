import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('C:\\Users\\rohan\\Desktop\\lab\\ML\\Supervised\\PolynomialLinearReg\\PositionSalaries_Data.csv')
# print(dataset.head())
# print(dataset.shape)


X = dataset.iloc[:,1:-1].values
y = dataset.iloc[:,-1].values


# Build linear reg model
from sklearn.linear_model import LinearRegression
lin_regs = LinearRegression()
lin_regs.fit(X, y)



# Build polynimial linear reg model
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=2)
X_poly = poly_reg.fit_transform(X)
lin_reg = LinearRegression()
lin_reg.fit(X_poly, y)



# predicting
y_pred = lin_reg.predict(X_poly)


df = pd.DataFrame({'Real values':y, 'Predicted values':y_pred})
print(df)

from sklearn.metrics import r2_score
print('R2 score:', r2_score(y, y_pred))


# visualization
plt.scatter(X, y, color='red')
plt.scatter(X, y_pred, color='green')
plt.plot(X, y_pred, color='black')
plt.title('Polynomial Reg')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()


# plt.scatter(X, y, color='red')
# plt.plot(X, lin_regs.predict(X), color='black')
# plt.title('Polynomial Reg')
# plt.xlabel('Position level')
# plt.ylabel('Salary')
# plt.show()


# plt.scatter(X, y, color='red')
# plt.scatter(X, y_pred, color='green')
# plt.plot(X, y_pred, color='black')
# plt.title('Polynomial Reg')
# plt.xlabel('Position level')
# plt.ylabel('Salary')
# plt.show()