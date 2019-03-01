#Importing Libraries

#Decision Tree Regression

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from collections import Counter

 #Importing Dataset

dataset = pd.read_csv('locations_data.csv')
X = dataset.iloc[:,[1,5,6,23,26,27,28,29,30,31,32,33,34]].values
y = dataset.iloc[:,[43]].values


# List for Encoding categorical data
L = [0,1]

# Encoding categorical data
# Encoding the Independent Variable
for i in L:
    from sklearn.preprocessing import LabelEncoder, OneHotEncoder
    labelencoder_X = LabelEncoder()
    X[:, i] = labelencoder_X.fit_transform(X[:,i])
    onehotencoder = OneHotEncoder(categorical_features = [1])
    X = onehotencoder.fit_transform(X).toarray()


#Avoiding Dummy Variable Trap

X = X[:,2:]


#Splittung the data into training and test set
from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test= train_test_split(X,y,test_size=0.3,random_state=0)


#Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

#Fitting Regressor Model to Dataset
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(X_train,y_train )


#Predicting a new result 
y_pred = regressor.predict(X_test)


#Visualising the  Decision Tree Regression Model Results
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = X_train[:,0]
y = X_train[:,1]
z = y_train

ax.scatter(x, y, z, c='r', marker='+')

ax.set_title(' Decision Tree Regression Model  ')
ax.set_xlabel(' Male/Female')
ax.set_ylabel(' Age ')
ax.set_zlabel(' Calories ')

x1 = X_test[:,0]
y1 = X_test[:,1]
z1 = regressor.predict(X_test)
ax.scatter(x1, y1, z1, c='b', marker='*')
plt.show()



