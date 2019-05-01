#Importing Libraries

#KMEANS

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from collections import Counter

 #Importing Dataset

dataset = pd.read_csv('locations_data full.csv')
X = dataset.loc[:,['Crash_Longitude_GDA94','Crash_Latitude_GDA94']]

##Using Elbow method to find the number of clusters
#from sklearn.cluster import KMeans
#wcss = []
#for i in range(1,11):
#    kmeans = KMeans(n_clusters = i,init = 'k-means++', max_iter = 300, n_init = 10,random_state =0)
#    kmeans.fit(X)
#    wcss.append(kmeans.inertia_)
#
#plt.plot(range(1,11),wcss)
#plt.title('The Elbow Method')
#plt.xlabel('No of Clusters')
#plt.ylabel('WCSS')
#plt.show()

id_n=80
kmeans = KMeans(n_clusters=id_n, random_state=0).fit(X)
id_label=kmeans.labels_
cluster_centre = kmeans.cluster_centers_
#plot result
ptsymb = np.array(['b.','r.','m.','g.','c.','k.','b*','r*','m*','r^']);
plt.figure(figsize=(12,12))
plt.ylabel('Longitude', fontsize=12)
plt.xlabel('Latitude', fontsize=12)
for i in range(id_n):
    cluster=np.where(id_label==i)[0]
    plt.plot(X.Crash_Longitude_GDA94[cluster].values,X.Crash_Latitude_GDA94[cluster].values,ptsymb[i])
plt.show()

#Adding to the main dataset K-means Result

import csv
rows=[]
fields=[]
with open('locations_data full.csv','r') as csv_input:
    csvreader= csv.reader(csv_input)
    fields=next(csvreader)
    for row in csvreader:
        rows.append(row)
fields.append("CLUSTERS_with_KMEAN")
i=0        
for row in rows:
    row.append(id_label[i])
    i+=1        

with open('locations_data full.csv','w') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

#Centre to a csv file
import pandas as pd 
pd.DataFrame(cluster_centre).to_csv("K_mean.csv")


#Just the labels
import pandas as pd 
pd.DataFrame(id_label).to_csv("Send_to_sky.csv")