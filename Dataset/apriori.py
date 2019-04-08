#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 09:31:42 2019

@author: kanishka
"""

#Apriori
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Data Preprocessing
dataset = pd.read_csv('locations_data_filtered.csv', header = None)
transactions = []
for i in range(0, 10):
    transactions.append([str(dataset.values[i,j]) for j in range(0, 13)])

# Training Apriori on the dataset
from apyori import apriori
rules = apriori(transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2)

# Visualising the results
results = list(rules)