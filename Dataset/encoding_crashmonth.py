#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 13:01:53 2019

@author: kanishka
"""

import pandas as pd

def preProcessResponsibleVehiclesData(data):

    #Encode Vehicles Involved with a custom logic
    data.loc [data['Crash_Month'].str.contains('January',case=False), 'Encoded_Crash_Month']='0'
    data.loc [data['Crash_Month'].str.contains('Feburary',case=False), 'Encoded_Crash_Month']='0'
    data.loc [data['Crash_Month'].str.contains('March',case=False), 'Encoded_Crash_Month']='0'
    data.loc [data['Crash_Month'].str.contains('April',case=False), 'Encoded_Crash_Month']='0'
    data.loc [data['Crash_Month'].str.contains('May',case=False), 'Encoded_Crash_Month']='1'
    data.loc [data['Crash_Month'].str.contains('June',case=False), 'Encoded_Crash_Month']='1'
    data.loc [data['Crash_Month'].str.contains('July',case=False), 'Encoded_Crash_Month']='1'
    data.loc [data['Crash_Month'].str.contains('August',case=False), 'Encoded_Crash_Month']='1'
    data.loc [data['Crash_Month'].str.contains('September',case=False), 'Encoded_Crash_Month']='2'
    data.loc [data['Crash_Month'].str.contains('October',case=False), 'Encoded_Crash_Month']='2'
    data.loc [data['Crash_Month'].str.contains('November',case=False), 'Encoded_Crash_Month']='2'
    data.loc [data['Crash_Month'].str.contains('December',case=False), 'Encoded_Crash_Month']='2'
    data.loc [data['Crash_Month'] =='', 'Encoded_Crash_Month']='3'

    encodedVehiclesResponsible=pd.get_dummies(data['Encoded_Crash_Month'],prefix='Crash_Month')
    data['Crash_Month_0']=encodedVehiclesResponsible['Crash_Month_0']
    data['Crash_Month_1']=encodedVehiclesResponsible['Crash_Month_1']
    data['Crash_Month_2']=encodedVehiclesResponsible['Crash_Month_2']


    data=data.drop(['Crash_Month'],axis=1)
    data=data.drop(['Encoded_Crash_Month'],axis=1)

    return data
