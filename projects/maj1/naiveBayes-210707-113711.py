import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



# importing dataset 
dataset = pd.read_csv('Social_Network_Ads-210701-145355.csv')
# print(dataset.head())
# print(dataset.shape)



x = dataset.iloc[:, [2,3]].values
y = dataset.iloc[:, -1].values


# splitting train and test data 
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.25)



# feature scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)



# Training naive bayes model on training dataset 
from sklearn.naive_bayes import GaussianNB 
classifier = GaussianNB()
classifier.fit(x_train, y_train)

# Predicting the test set 
y_pred = classifier.predict(x_test)

# Compare test and predicted values 
df = pd.DataFrame({'Real':y_test, 'Predicted':y_pred})
print(df)

# Accuracy 
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
print(confusion_matrix(y_test, y_pred))
print(accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))



# Visualizing training set
from matplotlib.colors import ListedColormap 
x_set, y_set = x_train, y_train
x1, x2 = np.meshgrid(np.arange(start =x_set[:,0].min()-1, stop = x_set[:,0].max()+1, step = 0.01),
                    np.arange(start =x_set[:,1].min()-1, stop = x_set[:,1].max()+1, step = 0.01))
plt.contourf(x1,x2, classifier.predict(np.array([x1.ravel(), x2.ravel()]).T).reshape(x1.shape),
            alpha=0.75, cmap = ListedColormap(('red', 'green')))


for i, j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[y_set == j, 0], x_set[y_set == j , 1],
    c = ListedColormap(('red', 'green')) (i), label = j)

plt.title("Naive Bayes(Training set)")
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

plt.title("Naive Bayes(Testing set)")
plt.xlabel('age')
plt.ylabel('salary')
plt.legend()
plt.show()