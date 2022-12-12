# Parsing Project 2 (American Football)

# These are the modules we are using
import os
from bs4 import BeautifulSoup
import pandas as pd


 # We start by sorting our data    
        
files = sorted(os.listdir("data"))

# We are using a for loop, and creating an empty list that we can use in beautifulsoup
for file in files:
    data = []
    text = open('data/'+ file, encoding="ISO-8859-1").read()
    soup = BeautifulSoup(text, 'html.parser')
  
# We are using BS to find all of the ids for the data we want to extract 
    players = soup.findAll('table', attrs={'id': 'games'})
  
# We are using a for loop to loop through each of the variables and extract the data from the attributes
    for play in players:
        try:
            Week = play.find('th', attrs={'class':'right'})
            Day = play.find('td', attrs={'class':'left','data-stat':'game_day_of_week'})
            Date = play.find('td', attrs={'data-stat': 'game_date'})
            Winner = play.find('td', attrs={'data-stat': 'winner'})
            Loser = play.find('td', attrs={'data-stat': 'loser'})
            PtsW = play.find('td', attrs={'data-stat': 'pts_win'})
            PtsL = play.find('td', attrs={'data-stat':'pts_lose'})
            data.append([Week, Day, Date, Winner, Loser, PtsW, PtsL])
        except AttributeError:
            print('Invalid cell')

 # Here we are taking our dataframe and turning it into csv file          
df = pd.DataFrame(data,columns = ['Week', 'Day', 'Date', 'Winner/tie', 'Loser/tie', 'PtsW', 'PtsL'])
df.to_csv(f"season/'players-{file}.csv'", index=False)
