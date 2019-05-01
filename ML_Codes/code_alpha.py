#Importing Libraries

#DBSCAN

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy
from sklearn.cluster import DBSCAN
from sklearn import metrics

 #Importing Dataset

dataset = pd.read_csv('locations_data full.csv')
X = dataset.iloc[:,[8,9]].values

db = DBSCAN(eps=0.009, min_samples=25).fit(X)

core_samples_mask = np.zeros_like(db.labels_, dtype=bool)

core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_
components = db.components_
core_sample_indices=db.core_sample_indices_
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

print('Estimated number of clusters: %d' % n_clusters_)
print(np.unique(labels))

#Adding to the main dataset

import csv
rows=[]
fields=[]
with open('locations_data full.csv','r') as csv_input:
    csvreader= csv.reader(csv_input)
    fields=next(csvreader)
    for row in csvreader:
        rows.append(row)
fields.append("CLUSTERS_with_DBSCAN")
i=0        
for row in rows:
    row.append(labels[i])
    i+=1        

with open('locations_data full.csv','w') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)
    

##Addibg Components
#import csv
#rows=[]
#fields=[]
#with open('DBCSAN.csv','r') as csv_input:
#    csvreader= csv.reader(csv_input)
#    fields=next(csvreader)
#    for row in csvreader:
#        rows.append(row)
#fields.append("CLUSTERS_with_DBSCAN")
#i=0        
#for row in rows:
#    row.append(components[i][0])
#    i+=1        
#
#with open('DBCSAN.csv','w') as csvfile:
#    csvwriter=csv.writer(csvfile)
#    csvwriter.writerow(fields)
#    csvwriter.writerows(rows)
#Centre to a csv file
import pandas as pd 
pd.DataFrame(components).to_csv("DBCSAN.csv") 

#PLOT

import matplotlib.pyplot as plt
  
  # Black removed and is used for noise instead.
unique_labels = set(labels)
colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))
for k, col in zip(unique_labels, colors):
    if k == -1:
        col = 'k'
    class_member_mask = (labels == k)
    xy = X[class_member_mask & core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,markeredgecolor='k', markersize=14)
    xy = X[class_member_mask & ~core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,markeredgecolor='k', markersize=6)
plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()


