from matplotlib.colors import ListedColormap
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


dataset = pd.read_csv('C:\\Users\\rohan\\Desktop\\lab\ML\\Supervised\\Classification\\Social_Network_Ads.csv')
# print(dataset.head())

# print(dataset.shape)


# extracting
x = dataset.iloc[:, [2,3]].values
y = dataset.iloc[:, -1].values



# splitting
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test =train_test_split(x,y,test_size=0.25, random_state=0)



# feature scaling
from sklearn.preprocessing import StandardScaler
st_x = StandardScaler()
x_train = st_x.fit_transform(x_train)
x_test = st_x.transform(x_test)



# Training model on train data 
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(x_train, y_train)



# Prediction
y_pred = classifier.predict(x_test)



# comparing 
df = pd.DataFrame({'Real':y_test, 'Predicted':y_pred})
# print(df)



# test accuracy
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
# print('Confusion matrix',cm)



# from sklearn.metrics import accuracy_score, precision_score, recall_score, mean_squared_error,f1_score, classification_report
# print('Accuracy score',accuracy_score(y_test, y_pred))
# print('precision_score ',precision_score(y_test, y_pred))
# print('recall_score',recall_score(y_test, y_pred))
# print('mean_squared_error',mean_squared_error(y_test, y_pred))
# print('F1 score',f1_score(y_test, y_pred))
# print(classification_report(y_test, y_pred))




# Visualizing training set 
x_set, y_set = x_train, y_train
x1, x2 = np.meshgrid(np.arange(start =x_set[:,0].min()-1, stop = x_set[:,0].max()+1, step = 0.01),
                    np.arange(start =x_set[:,1].min()-1, stop = x_set[:,1].max()+1, step = 0.01))
plt.contourf(x1,x2, classifier.predict(np.array([x1.ravel(), x2.ravel()]).T).reshape(x1.shape),
            alpha=0.75, cmap = ListedColormap(('red', 'green')))


for i, j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[y_set == j, 0], x_set[y_set == j , 1],
    c = ListedColormap(('red', 'green')) (i), label = j)

plt.title("Logistic reg")
plt.xlabel('age')
plt.ylabel('salary')
plt.legend()
plt.show()


# Visualizing test set 
x_set, y_set = x_test, y_test
x1, x2 = np.meshgrid(np.arange(start =x_set[:,0].min()-1, stop = x_set[:,0].max()+1, step = 0.01),
                    np.arange(start =x_set[:,1].min()-1, stop = x_set[:,1].max()+1, step = 0.01))
plt.contourf(x1,x2, classifier.predict(np.array([x1.ravel(), x2.ravel()]).T).reshape(x1.shape),
            alpha=0.75, cmap = ListedColormap(('red', 'green')))


for i, j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[y_set == j, 0], x_set[y_set == j , 1],
    c = ListedColormap(('red', 'green')) (i), label = j)

plt.title("Logistic reg")
plt.xlabel('age')
plt.ylabel('salary')
plt.legend()
plt.show()