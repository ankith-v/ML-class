# Data ore processing
from numpy import random
import pandas as pd 
import matplotlib.pyplot as plt 


dataset = pd.read_csv('projects\mini2\Mall_Customers-210707-122914.csv')
# print(dataset.head())


# Extracting Independent variables
x = dataset.iloc[:,[3,4]].values


# Finfing optimal no. of custers using elbow method
from sklearn.cluster import KMeans
wcss_list = []      #initilize


for i in range(1,11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state= 45)
    kmeans.fit(x)
    wcss_list.append(kmeans.inertia_)

plt.plot(range(1,11), wcss_list)
plt.title('The elbow graph')
plt.xlabel('No. of clusters')
plt.ylabel('wcss list')
plt.show()



# Training the k-means on dataset 
kmeans = KMeans(n_clusters=5, init='k-means++', random_state= 45)
y_pred = kmeans.fit_predict(x)



# visualisation of clusters
plt.scatter(x[y_pred == 0,0], x[y_pred == 0,1], s = 100, c='blue', label='Cluster 1')
plt.scatter(x[y_pred == 1,0], x[y_pred == 1,1], s = 100, c='red', label='Cluster 2')
plt.scatter(x[y_pred == 2,0], x[y_pred == 2,1], s = 100, c='green', label='Cluster 3')
plt.scatter(x[y_pred == 3,0], x[y_pred == 3,1], s = 100, c='cyan', label='Cluster 4')
plt.scatter(x[y_pred == 4,0], x[y_pred == 4,1], s = 100, c='magenta', label='Cluster 5')
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=200, c='yellow', label='Centriod' )
plt.title('Clusters')
plt.xlabel('Annual income')
plt.ylabel('Spending')
plt.legend()
plt.show()