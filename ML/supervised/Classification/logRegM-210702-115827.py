from sklearn import datasets
import numpy as np

digits = datasets.load_digits()

x = digits.data
y = digits.target

# splitting
from   sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state=0)

# convert to numpy array to see the shape
x_train = np.array(x_train)
x_test = np.array(x_test)
y_train = np.array(y_train)
y_test = np.array(y_test)

# print(x_train.shape)
# print(x_test.shape)


from sklearn.linear_model import LogisticRegression
reg = LogisticRegression(solver='sag', max_iter=1000, multi_class='multinomial')
reg.fit(x_train, y_train)



y_pred = reg.predict(x_test)


# comparing 
import pandas as pd
df = pd.DataFrame({'Real':y_test, 'Predicted':y_pred})
# print(df)



# test accuracy
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

from sklearn.metrics import accuracy_score, classification_report
# print('Accuracy score',accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
