#Importing Libraries

#KMEANS

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from collections import Counter

 #Importing Dataset

dataset = pd.read_csv('locations_data.csv')
X = dataset.loc[:,['Crash_Longitude_GDA94','Crash_Latitude_GDA94']]

id_n=23
kmeans = KMeans(n_clusters=id_n, random_state=0).fit(X)
id_label=kmeans.labels_

#plot result
ptsymb = np.array(['b.','r.','m.','g.','c.','k.','b*','r*','m*','r^']);
plt.figure(figsize=(12,12))
plt.ylabel('Longitude', fontsize=12)
plt.xlabel('Latitude', fontsize=12)
for i in range(id_n):
    cluster=np.where(id_label==i)[0]
    plt.plot(X.Crash_Longitude_GDA94[cluster].values,X.Crash_Latitude_GDA94[cluster].values,ptsymb[i])
plt.show()

#Adding to the main dataset

import csv
rows=[]
fields=[]
with open('locations_data.csv','r') as csv_input:
    csvreader= csv.reader(csv_input)
    fields=next(csvreader)
    for row in csvreader:
        rows.append(row)
fields.append("CLUSTERS_with_KMEAN")
i=0        
for row in rows:
    row.append(id_label[i])
    i+=1        

with open('locations_data.csv','w') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)
    