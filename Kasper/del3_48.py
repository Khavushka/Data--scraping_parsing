#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 21:28:06 2022

@author: kasperhannberg
"""

###create an all-time NFL table with rank, franchise.
###1. scrape webpage - Got all active franchises  
###2. save to csv:
###3. (W)wins, (T)draws, (L)losses and points


import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.pro-football-reference.com/teams/index.htm"
r = requests.get(URL)

states=[] # a list to store information form the append

soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib

table = soup.find('tbody') #main table for parsing

for team in table.findAll('tr'): # looping relevant information
    state = {}
    state['Teams'] = team.find('th').text 
    state['Wins'] = team.find('td', attrs={'data-stat':'wins'}).text 
    state['Losses'] = team.find('td', attrs={'data-stat':'losses'}).text
    state['Ties'] = team.find('td', attrs={'data-stat':'ties'}).text
    states.append(state) 

filename = 'team_easyon.csv' # saving file to .csv
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['Teams','Wins','Losses','Ties'])
    w.writeheader()
    for state in states:
        w.writerow(state)