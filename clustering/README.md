## Clustering

###K-Mean Clustering

1. Unsupervised machine learning
2. Aim to find homogeneous subgroups of data points with similar characteristics

####Steps
1. Choose the number of clusters
2. Specify the cluster seeds or centroid
3. Assign each point to a centroid
4. Adjust the centroids
5. Repeat step 3 and 4, until no other assignments are not required

####Choosing number of clusters
To choose number of clusters, Elbow point graph is used to find optimum number of clusters (i.e. value of K).
To plot Elbow point graph, we compute WCSS (Within Cluster Sum of Squares) for each K value and plot it against K-value
on x-axis.
To find the optimum K-value, look for a point in the graph after which WCSS has stopped decreasing relatively.

If we minimize WCSS(within cluster sum of square), we have reached the perfect clustering solution

NOTE - As number of clusters increases, WCSS decreases, which is good
kmeans._inertia is WCSS value provided by sklearn module

###Dendogram and heatmaps


