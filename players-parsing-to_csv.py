# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 10:12:27 2022

@author: khavu
"""

import os
from bs4 import BeautifulSoup
import pandas as pd


data = []

files = sorted(os.listdir("data"))
for file in files:
    path = open('data/'+file, encoding='ISO-8859-1').read()
    soup = BeautifulSoup(path)
    
    for header in soup.find_all('tr'):  
        # if header.find('th', attrs={'data-stat':'week_num'}).text != "Week" and header.find("th", attrs={"data-stat":"week_num"}).text != "":
        if header.find('th', attrs={'data-stat':'week_num'}).text != "Week":
            try:
                Week = header.find('th', attrs={'data-stat':'week_num'}).text
                Day = header.find('td', attrs={'data-stat':'game_day_of_week'}).text
                Date = header.find('td', attrs={'data-stat': 'game_date'}).text
                Time = header.find('td', attrs={'data-stat': 'gametime'}).text
                Winner = header.find('td', attrs={'data-stat': 'winner'}).text
                if header.find('td', attrs={'data-stat':'game_location'}).text != "" and header.find("td", attrs={"data-stat":"game_location"}).text != "":
                    try:
                        Location = header.find('td', attrs={'data-stat': 'game_location'}).text
                    except:
                        continue
                Loser = header.find('td', attrs={'data-stat': 'loser'}).text
                PtsW = header.find('td', attrs={'data-stat': 'pts_win'}).text
                PtsL = header.find('td', attrs={'data-stat':'pts_lose'}).text 
                YdsW = header.find('td', attrs={'data-stat':'yards_win'}).text
                TOW = header.find('td', attrs={'data-stat':'to_win'}).text
                YdsL = header.find('td', attrs={'data-stat': 'yards_lose'}).text
                TOL = header.find('td', attrs={'data-stat': 'to_lose'}).text
                data.append([Week, Day, Date, Time, Winner, Location, Loser, PtsW, PtsL, YdsW, TOW, YdsL, TOL])
            except:
                continue

    dataFrame = pd.DataFrame(data = data, columns = ('Week', 'Day', 'Date', 'Time', 'Winner', 'Location', 'Loser', 'PtsW', 'PtsL', 'YdsW', 'TOW', 'YdsL', 'TOL'))  
    
    dataFrame.to_csv('players_allInone.csv')
  
