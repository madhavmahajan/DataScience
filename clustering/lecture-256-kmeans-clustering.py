"""
Lecture 256 - K-means clustering for 6 countries with latitude and longitude
Lecture 258 - Clustering categorical data
Lecture 260 - Choosing number of clusters
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from sklearn.cluster import KMeans

file_name = "./data/3.01. Country clusters.csv"
data = pd.read_csv(file_name)

print("-" * 80)
print("Raw data from the csv file")
print(data.head())

print("-" * 80)
print("Description of raw data")
print(data.describe(include='all'))

print("-" * 80)
print("Scatter plot")
plt.scatter(data['Longitude'], data['Latitude'])
plt.xlim(-150, 150)
plt.ylim(-90, 90)
plt.show()

# Handling categorical data # lecture 258
# data_mapped = data.copy()
# data_mapped = data['Language'].map({'English': 0, 'German': 1, 'French':2})
# print(data_mapped)
# x = data.iloc[:, 1:4]

print("-" * 80)
print("Selecting the features (picked Latitude and Longitude, removed Country and Language)")
x = data.iloc[:, 1:3]
print(x)

# Choosing number of clusters
print("-" * 80)
print("Calculating WCSS for possible number of clusters 1 to 7")
wcss = []
for i in range(1, 7):
    kmeans = KMeans(i)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
    print("WCSS for {} cluster: {}".format(i, kmeans.inertia_))

print("-" * 80)
print("Plotting graph with WCSS on y-axis and number of clusters on x-axis")
number_of_clusters = range(1, 7)
plt.plot(number_of_clusters, wcss)
plt.show()

print("-" * 80)
print("After looking at the graph, we see an elbow shape")
print("After number of clusters is 3, there is not much change in the WCSS for rest of the clusters")
print("which concludes, 3 cluster solution is the best fit")

# Clustering
print("-" * 80)
print("Initiating KMeans clustering solution with 3 clusters")
kmeans = KMeans(3)
result = kmeans.fit(x)
print(result)

# Clustering results
print("-" * 80)
print("Identifying 3 clusters by fitting the data")
identified_clusters = kmeans.fit_predict(x)

print("-" * 80)
print("Creating new table with raw data and new column marking each record with a cluster")
data_with_clusters = data.copy()
data_with_clusters['Cluster'] = identified_clusters
print(data_with_clusters)

print("-" * 80)
print("Plotting data representing 3 clusters")
plt.scatter(data_with_clusters['Longitude'], data_with_clusters['Latitude'], c=data_with_clusters['Cluster'],
            cmap='rainbow')
plt.xlim(-150, 150)
plt.ylim(-90, 90)
plt.show()

