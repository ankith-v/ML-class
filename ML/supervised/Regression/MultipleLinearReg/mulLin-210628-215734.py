import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('C:\\Users\\rohan\\Desktop\\lab\\ML\\Supervised\\MultipleLinear\\Startups_Data.csv')
# print(dataset.head(10))
# print(dataset.shape)


X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values



# Encoding your categorical data
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
cat = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [3])], remainder='passthrough')
X = np.array(cat.fit_transform(X))
# print(X)


# Splitting data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


# TRainng
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)


# Predicting
# predicting
y_pred = regressor.predict(X_test)


df = pd.DataFrame({'Real values':y_test, 'Predicted values':y_pred})
print(df)

from sklearn.metrics import r2_score
print('R2 score:', r2_score(y_test, y_pred))
