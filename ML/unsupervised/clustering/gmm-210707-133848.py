# Importing dataset 

import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('C:\\Users\\rohan\\Desktop\\lab\\ML\\Unsupervised\\Clustering\\Clustering_gmm.csv')
# print(data.head())


# plt.scatter(data['Weight'], data['Height']) 
# plt.xlabel('Weight')
# plt.ylabel('Height')
# plt.title('Data visualisation')
# plt.show()



# training kmeans model 
# from sklearn.cluster import KMeans
# kmeans = KMeans(n_clusters=4)
# kmeans.fit(data)



# # prediction for kmeans 
# pred = kmeans.predict(data)
# # print(pred)
# frame = pd.DataFrame(data)
# frame['cluster'] = pred
# frame.columns = ['Weight', 'Height', 'cluster']


# # plotting 
# color = ['blue', 'green', 'black', 'yellow']
# for k in range(0,4):
#     data = frame[frame['cluster']==k]
#     plt.scatter(data['Weight'], data['Height'], c=color[k])
# plt.title('K-means')
# plt.show()




# Gaussian Mixture Model - build
# Training GMM  
from sklearn.mixture import GaussianMixture
gmm = GaussianMixture(n_components=4)
gmm.fit(data)



# prediction for gmm
pred = gmm.predict(data)
frame = pd.DataFrame(data)
frame['cluster'] = pred
frame.columns = ['Weight', 'Height', 'cluster']



# PLotting 
color = ['blue', 'green', 'black', 'yellow']
for k in range(0,4):
    data = frame[frame['cluster']==k]
    plt.scatter(data['Weight'], data['Height'], c = color[k])
plt.show()

