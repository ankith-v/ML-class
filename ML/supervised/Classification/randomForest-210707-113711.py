import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.sparse import data


# importing dataset 

dataset = pd.read_csv('C:\\Users\\rohan\\Desktop\\lab\ML\\Supervised\\Classification\\Social_Network_Ads.csv')
# print(dataset.head())
# print(dataset.shape)


# extract independent and dependent variables 
x = dataset.iloc[:, [2,3]].values
y = dataset.iloc[:, -1].values



# Splitting into train and test 
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.25)



# feature scaling
from sklearn.preprocessing import StandardScaler
st_x = StandardScaler()
x_train = st_x.fit_transform(x_train)
x_test = st_x.transform(x_test)



# training model on the training set
from sklearn.ensemble import RandomForestClassifier
classfier = RandomForestClassifier(n_estimators=20, criterion="entropy")
classfier.fit(x_train, y_train)



# prediction
y_pred = classfier.predict(x_test)


# compare data 
df = pd.DataFrame({'Real':y_test, 'Predicted':y_pred})
print(df)



# accuracy confusion matrix 
from sklearn.metrics import confusion_matrix, accuracy_score
print(confusion_matrix(y_test, y_pred))
print(accuracy_score(y_test, y_pred))


