from os import linesep
import pandas as pd
import numpy as np

df_train = pd.read_csv('C:\\Users\\rohan\\Desktop\\lab\\ML\\Supervised\\LinearReg\\train.csv')
# print(df_train)
df_test = pd.read_csv('C:\\Users\\rohan\\Desktop\\lab\\ML\\Supervised\\LinearReg\\test.csv')
# print(df_test)
print(df_train.shape)
# print(df_test.shape)
# x = df_train['y'].mode()
# df_train.fillna(x, inplace=True)
df_train.dropna(inplace=True)
print(df_train.shape)


x_train = df_train['x']
y_train = df_train['y']
x_test = df_test['x']
y_test = df_test['y']


x_train = np.array(x_train)
y_train = np.array(y_train)
x_test = np.array(x_test)
y_test = np.array(y_test)

# print(x_train)
# print(x_test)
# print(y_train)
# print(y_test)


x_train = x_train.reshape(-1,1)
x_test = x_test.reshape(-1,1)
# print(x_test)
# print(x_train)


from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
# pip install scikit-learn 


regress = LinearRegression(normalize=True)
regress.fit(x_train,y_train)
y_pred = regress.predict(x_test)
print(r2_score(y_test,y_pred))
