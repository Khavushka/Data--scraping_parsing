import os
from bs4 import BeautifulSoup
import pandas


data = []

files = sorted(os.listdir("data"))

for file in files:
    text = open('data/'+ file).read()
    soup = BeautifulSoup(text)
    for body in soup.find('tbody').text:
       if soup.find('tr'):
        Week_num = soup.find('th', attrs={'data-stat':'week_num'}).text
        Week = soup.find('td', attrs={'data-stat':'game_day_of_week'}).text
        Date = soup.find('td', attrs={'data-stat': 'game_date'}).text
        Time = soup.find('td', attrs={'data-stat': 'gametime'}).text
        Winner = soup.find('td', attrs={'data-stat': 'winner'}).text
        data.append([Week_num, Week, Date, Time])
        print(body)
                
df = pandas.DataFrame(data,columns = ['Week_num', 'Week', 'Date','Time'])
df.to_csv('players.csv', index=False, encoding='utf-8')


"""
    #for incident in soup.find('table', attrs={'id':'games', 'data-cols-to-freeze':"1,3"}):
        #thead = incident.find('thead')   
        #if soup.find('tr'):  
            #print(t)
         #   Day = soup.find('th', attrs={'aria-label':'Day'}).text
          #  Date = soup.find('th', attrs={'aria-label': 'Date'})
           # Week = soup.find('th', attrs={'aria-label':'Week'})
            #Time = soup.find('th', attrs={'aria-label':'Time'})
            #print(Time)
"""