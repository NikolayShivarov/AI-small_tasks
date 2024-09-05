# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 23:21:14 2023

@author: NikolayShivarov
"""
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN



df = pd.read_csv("data_assignment3.csv")


plt.figure(1)
plt.scatter(df["phi"], df["psi"], s = 0.05)
plt.title("Phi and Psi angles")
plt.xlabel("Phi")
plt.ylabel("Psi")
plt.grid()

plt.figure(2)
plt.hist2d(df["phi"], df["psi"], bins = (40,40), cmap = cm.gist_rainbow )
plt.colorbar()

wcss = []
k_values = [1, 2, 3, 4, 5, 6, 7, 8]
for k in k_values:
    kmeans = KMeans(n_clusters=k, n_init=10, random_state=0)
    clusters = kmeans.fit_predict(df[["phi", "psi"]])
    wcss.append(kmeans.inertia_)
    
plt.figure(3)
plt.plot(range(1, 9), wcss, marker='o', linestyle='--')
plt.title("Elbow method for optimal number of clusters")
plt.xlabel("Number of Clusters")
plt.ylabel("Within-Cluster Sum of Squares (WCSS)")
plt.grid()  


plt.figure(4)
kmeans = KMeans(n_clusters=2, n_init=10, random_state=0)
clusters = kmeans.fit_predict(df[["phi", "psi"]])
plt.scatter(df["phi"], df["psi"], c=clusters, cmap="viridis", s = 0.05)
plt.title("Kmeans K = 2")
plt.xlabel("Phi")
plt.ylabel("Psi")

plt.figure(5)
kmeans = KMeans(n_clusters=3, n_init=10, random_state=0)
clusters = kmeans.fit_predict(df[["phi", "psi"]])
plt.scatter(df["phi"], df["psi"], c=clusters, cmap="viridis", s = 0.05)
plt.title("Kmeans K = 3")
plt.xlabel("Phi")
plt.ylabel("Psi")

plt.figure(6)
kmeans = KMeans(n_clusters=4, n_init=10, random_state=0)
clusters = kmeans.fit_predict(df[["phi", "psi"]])
plt.scatter(df["phi"], df["psi"], c=clusters, cmap="viridis", s = 0.05)
plt.title("Kmeans K = 4")
plt.xlabel("Phi")
plt.ylabel("Psi")

               
plt.figure(7)
dbscan = DBSCAN(eps=10, min_samples=200)
clusters = dbscan.fit_predict(df[['phi', 'psi']])
outliers = clusters == -1
plt.scatter(df["phi"], df["psi"], c=clusters, cmap="viridis", s = 0.05)
plt.title("DBSCAN")
plt.xlabel("Phi")
plt.ylabel("Psi") 

df["Outliers"] = outliers
outlier_counts = df.groupby("residue name")["Outliers"].sum()

plt.figure(8)
outlier_counts.plot(kind="bar")
plt.title("Outliers by Amino Acid Residue Type")
plt.xlabel("Amino Acid Residue Type")
plt.ylabel("Outlier Count")

df_pro = df[df["residue name"] == "PRO"]
plt.figure(9)
dbscan_pro = DBSCAN(eps=10, min_samples=15)
clusters_pro = dbscan_pro.fit_predict(df_pro[['phi', 'psi']])
plt.scatter(df_pro["phi"], df_pro["psi"], c=clusters_pro, cmap="viridis", s=0.5)
plt.title("DBSCAN for Residue Type PRO")
plt.xlabel("Phi")
plt.ylabel("Psi")




    
    
    
    
    
    