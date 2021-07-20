import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


dataset = pd.read_csv('Social_Network_Ads-210701-145355.csv')
# print(dataset.head())

# print(dataset.shape)


x = dataset.iloc[:, [2,3]].values
y = dataset.iloc[:,-1].values


# splitting into training and test dataset 
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test =train_test_split(x,y,test_size=0.25, random_state=0)



# feature scaling 
from sklearn.preprocessing import StandardScaler
st_x = StandardScaler()
x_train = st_x.fit_transform(x_train)
x_test = st_x.transform(x_test)



# Fitting decision tree model to traing set 
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)
classifier.fit(x_train, y_train)



# Prediction
y_pred = classifier.predict(x_test)



# comparing 
df = pd.DataFrame({'Real':y_test, 'Predicted':y_pred})
# print(df)



# test accuracy
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)



from sklearn.metrics import accuracy_score, classification_report
# print('Accuracy score',accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

