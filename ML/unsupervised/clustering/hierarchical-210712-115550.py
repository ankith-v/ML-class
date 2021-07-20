# Step 1: Data pre-processing

# importing libraries
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt


# importing dataset
dataset = pd.read_csv('C:\\Users\\rohan\\Desktop\\lab\\ML\\Unsupervised\\Clustering\\Mall_Customers.csv')
print(dataset.head())


# extracting the matrix feature
x = dataset.iloc[:, [3,4]].values


# Step 2: Finding the optimal number of clusters using the dendrogram 
import scipy.cluster.hierarchy as shc
dend = shc.dendrogram(shc.linkage(x, method='ward'))
plt.title("Dendrogram plot")
plt.ylabel("Euclidean distance")
plt.xlabel("Customers")
plt.show() 



# Step 3:  Training the HC model 
from sklearn.cluster import AgglomerativeClustering
hc = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
y_pred = hc.fit_predict(x)



# Step 4: Visualization of clusters 
plt.scatter(x[y_pred == 0,0], x[y_pred == 0,1], s = 100, c='blue', label='Cluster 1')
plt.scatter(x[y_pred == 1,0], x[y_pred == 1,1], s = 100, c='red', label='Cluster 2')
plt.scatter(x[y_pred == 2,0], x[y_pred == 2,1], s = 100, c='green', label='Cluster 3')
plt.scatter(x[y_pred == 3,0], x[y_pred == 3,1], s = 100, c='cyan', label='Cluster 4')
plt.scatter(x[y_pred == 4,0], x[y_pred == 4,1], s = 100, c='magenta', label='Cluster 5')
plt.title('Clusters of custmers')
plt.xlabel('Annual income')
plt.ylabel('Spending')
plt.legend()
plt.show()