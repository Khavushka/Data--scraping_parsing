import os
from bs4 import BeautifulSoup
import pandas as pd


data = []
     
        
files = sorted(os.listdir("data"))

for file in files:
    text = open('data/'+ file, encoding="ISO-8859-1").read()
    soup = BeautifulSoup(text, 'html.parser')
    
    players = soup.findAll('table', attrs={'id': 'games'})
    
    for play in players:
        try:
            Week = play.find('th', attrs={'class':'right'}).text
            Day = play.find('td', attrs={'class':'left','data-stat':'game_day_of_week'}).text
            Date = play.find('td', attrs={'data-stat': 'game_date'}).text
            Winner = play.find('td', attrs={'data-stat': 'winner'}).text
            Loser = play.find('td', attrs={'data-stat': 'loser'}).text
            PtsW = play.find('td', attrs={'data-stat': 'pts_win'}).text
            PtsL = play.find('td', attrs={'data-stat':'pts_lose'}).text
            data.append([Week, Day, Date, Winner, Loser, PtsW, PtsL])
        except AttributeError:
            print('Invalid cell')

           
df = pd.DataFrame(data,columns = ['Week', 'Day', 'Date', 'Winner/tie', 'Loser/tie', 'PtsW', 'PtsL'])
df.to_csv('players.csv', index=False)

def season():
    moby = open("players.csv", "r")
    x = 1
    for i in moby:
        if "Week" in str(i) and "Year" not in str(i):
            title = str('season/'+"season" + str(x) + ".csv")
            season_chap = open(title, "w")
            x+=1
        season_chap.write(i)
    season_chap.close()
    moby.close()
season()

