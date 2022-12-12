#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 10:44:42 2022

@author: kasperhannberg
"""
#adds rank to franchise
from dash import Dash, html, Input, Output, dash_table
import pandas as pd
import pandas as pd

#Load the data
data = pd.read_csv("franchise.csv")

#Sorts a data frame in Ascending or Descending order of passed Column
df = data.sort_values(by=['Wins','Ties'], ascending=False)

#type-cast both the columns of interest to str and combine them by concatenating them.
#Convert these back to numerical values so that they could be differentiated based on their magnitude.
col1 = df["Wins"].astype(str) 
col2 = df["Ties"].astype(str)
df['Rank'] = (col1+col2).astype(int).rank(method='dense', ascending=False).astype(int)
df.sort_values('Rank')

df.to_csv('franchise_rank.csv')
