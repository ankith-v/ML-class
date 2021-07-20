# Import libraries 
import numpy as np
from sklearn import datasets
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt



# Determine centriods
centers = [[0.5,2],[-1,-1],[1.5,1]]



# create datasets
X, y = make_blobs(n_samples=750, centers=centers, cluster_std=0.5, random_state=0)


# normalize 
X = StandardScaler().fit_transform(X)


# visualize
plt.scatter(X[:,0], X[:,1], c = y, cmap='Paired')
plt.show()



# create DBSCAN object 
from sklearn.cluster import DBSCAN
db = DBSCAN(eps=0.4, min_samples=20)
db.fit(X)



# visualize DBSCAN 
y_pred = db.fit_predict(X)
plt.scatter(X[:,0], X[:,1], c = y_pred, cmap='Paired')
plt.title('Clusters determined using DBSCAN')
plt.show()




print(db.labels_[db.labels_ == -1].size)
labels = db.labels_

clusters = len(set(labels)) - (1 if -1 in labels else 0)
noise = list(labels).count(-1)
print('clusters',clusters)
print('noise',noise)


from sklearn import metrics
print('Silhoette score:', metrics.silhouette_score(X, labels))