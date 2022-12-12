# Parsing Project 2 (American Football)

# These are the modules we are using
import os
from bs4 import BeautifulSoup
import pandas as pd

 # We start by sorting our data  
files = sorted(os.listdir("data"))

# We are using a for loop, and creating an empty list that we can use in beautifulsoup
for file in files:
    path = open('data/'+file, encoding='ISO-8859-1').read()
    soup = BeautifulSoup(path)
    data = []

 # We are using BS to find all of the 'tr' for the data we want to extract    
 # Then using a for loop to loop through each of the variables and extract the data from the attributes
    for header in soup.find_all('tr'):  
        if header.find('th', attrs={'data-stat':'week_num'}).text != "Week" and header.find("th", attrs={"data-stat":"week_num"}).text != "":
            try:
                Week = header.find('th', attrs={'data-stat':'week_num'}).text
                Day = header.find('td', attrs={'data-stat':'game_day_of_week'}).text
                Date = header.find('td', attrs={'data-stat': 'game_date'}).text
                Time = header.find('td', attrs={'data-stat': 'gametime'}).text
                Winner = header.find('td', attrs={'data-stat': 'winner'}).text
                Loser = header.find('td', attrs={'data-stat': 'loser'}).text
                PtsW = header.find('td', attrs={'data-stat': 'pts_win'}).text
                PtsL = header.find('td', attrs={'data-stat':'pts_lose'}).text 
                data.append([Week, Day, Date, Time, Winner, Loser, PtsW, PtsL])
            except:
                continue
#Taking our dataframe and turning it into csv file 
    dataFrame = pd.DataFrame(data = data, columns = ('Week', 'Day', 'Date', 'Time', 'Winner', 'Loser', 'PtsW', 'PtsL'))  
    
    dataFrame.to_csv('season/' + file + '.csv')
  
