import pandas as pd
from collections import Counter

resultat = pd.read_csv("players_allInone.csv", index_col='Date')

df = pd.DataFrame(resultat, columns= ['Winner', 'Location', 'Loser'])
df['Winner'].value_counts().idxmax()
df['Loser'].value_counts().idxmax()
df['Location'].value_counts().idxmax()

# df.Date.mode()

# df['Winner'].value_counts().nlargest()

df.to_csv('del_3_resultat.csv')