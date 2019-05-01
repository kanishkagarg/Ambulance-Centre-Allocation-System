#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 09:20:40 2019

@author: kanishka
"""

import numpy as np
import pandas as pd
import math
dataset = pd.read_csv('locations_data full.csv')
X = dataset.iloc[:,[8,9,50]].values




def distance(origin, destination):
    """
    Calculate the Haversine distance.

    Parameters
    ----------
    origin : tuple of float
        (lat, long)
    destination : tuple of float
        (lat, long)

    Returns
    -------
    distance_in_km : float

    Examples
    --------
    >>> origin = (48.1372, 11.5756)  # Munich
    >>> destination = (52.5186, 13.4083)  # Berlin
    >>> round(distance(origin, destination), 1)
    504.2
    """
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371  # km

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c

    return d



d=distance((48.1372, 11.5756),(52.5186, 13.4083))
print(d)

X1 = X[0:10,:]
print(X1)
  
for i in X1:
    dist = 0.0
    distance_initial_lon = 0.0
    distance_initial_lat = 0.0
    temp = i[2]
    distance_initial_lon = i[0]
    distance_initail_lat = i[1]
    dist_intra = (1/(i[0]*i[1]))
    while(i[2]==temp):
        dist = dist + distance((distance_initial_lat,distance_initial_lon),(i[1],i[0]))
    dist_intra = dist_intra * dist
    dist_intra = math.average(dist_intra)
    print(dist_intra)