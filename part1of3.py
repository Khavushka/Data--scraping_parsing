# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 11:32:13 2022

@author: frede
"""

#opg 3 part 1 

# count the numbers of different resluts and display them in a decreasingly orderlist

import pandas as pd


nfl_data = "C:/Users/frede/OneDrive/Dokumenter/Python Scripts/AmFoot/players_allInone.csv"

# Combining the columns PtsW and PtsL, and rearranging them in ascending order and countning the occurence of the same results
df = pd.read_csv(nfl_data, index_col=0)

# creatining af new variable, 
nfl_new= df.groupby(['PtsW','PtsL']).size().reset_index(name="time")

# rearring to descending order 
nf2 = nfl_new.sort_index(ascending= False)



# count the number of different results 
# make an empty list 
# creat counter 
# if not on list append 
# if on list add 1 
# sort in decreasingly order

# part 2 
# Scrabe and parse together and make a csv of that one page
# create table with dash and plotty
# sort it 