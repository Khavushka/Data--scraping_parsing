import os
from bs4 import BeautifulSoup
#import pandas as pd
import csv
    
 
     
files = sorted(os.listdir("data"))

for file in files:
    page = open('data/'+ file, encoding="ISO-8859-1").read()
    soup = BeautifulSoup(page, 'html.parser')    
    data = [] 
    
    for players in soup.findAll('tr'):
        if players.find('th', attrs={'data-stat': "week_num"}).text != "Week" and players.find("th", attrs={"data-stat":"week_num"}).text != "":
            data.append(players)

    csvFile = open("season/players" + file[4:8], "w")    
    csvWritter = csv.writer(csvFile)
    
    for play in data:
        try:
            Week = play.find('th', attrs={'data-stat':'week_num'}).text
            Day = play.find('td', attrs={'data-stat':'game_day_of_week'}).text
            Date = play.find('td', attrs={'data-stat': 'game_date'}).text
            Winner = play.find('td', attrs={'data-stat': 'winner'}).text
            Loser = play.find('td', attrs={'data-stat': 'loser'}).text
            PtsW = play.find('td', attrs={'data-stat': 'pts_win'}).text
            PtsL = play.find('td', attrs={'data-stat':'pts_lose'}).text 
        except AttributeError:
            print('Invalid cell')         
        df =  (Week, Day, Date, Winner, Loser, PtsW, PtsL)
        csvWritter.writerow(df)
