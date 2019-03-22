#LATEST CODE

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


 #Importing Dataset

dataset = pd.read_csv('locations_data.csv')
X = dataset.iloc[:,[4,27,29]].values
y = dataset.iloc[:,[43]].values

#Encoding Categorical Data

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
lab_X = LabelEncoder()
X[:,0] = lab_X.fit_transform(X[:,0])

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
lab_X = LabelEncoder()
X[:,1] = lab_X.fit_transform(X[:,1])

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
lab_X = LabelEncoder()
X[:,2] = lab_X.fit_transform(X[:,2])

#Decision Tree

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Fitting classifier to the Training set
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion = 'entropy', random_state =0)
classifier.fit(X_train,y_train )

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)



               
#Accuracy = 0
#for i in y_test:
#    Accuracy = Accuracy+abs(y_test-y_pred)
#    
#Accuracy= Accuracy/y_test.length()

#Visualising tne Tree
import graphviz 
from graphviz import Source
from sklearn import tree
dot_data = tree.export_graphviz(classifier, out_file=None)

graph = graphviz.Source(dot_data) 
graph.render("name of file",view = True)