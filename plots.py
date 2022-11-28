# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 12:45:55 2022

@author: khavu
"""

import dash
# from dash.dependencies import Input, Output
# from dash import dcc
from dash import html
# import plotly.graph_objs as go
# import plotly.express as px
# import random
# import text
# import math
import pandas as pd

df = pd.read_csv('players_allInone.csv')

# Del 1/3

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


app = dash.Dash(__name__)

app.layout = html.Div([
    html.H4(children='Football Projekt 2:'),
    generate_table(df)
])

if __name__ == '__main__':
    app.run_server(debug=True)



"""
season = []
for i in range(1,51):
    filename = "data/season-"+str(i)+".csv"
    c_dict = text.get_dictionary(filename)
    season.append(c_dict)
    

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1(children='Project 2: American Football',
            style = {'textAlign':'center', 'font-family' : 'Roboto'}),
    html.Div([
        dcc.Dropdown(
            id='tags-number',
            options=[{'label': str(i)+" tags", 'value': i} for i in [50,100,200,500]],
            value=50,
            style={'width':'50%','margin':'auto'}
        )
    ]),
    html.Div([
            dcc.Graph(id='word-cloud')
    ]),
    html.Div([
            dcc.Graph(id='word-distribution-bar')
    ])
])

def getXY(number):
    x_vals = [i*50 for i in range(int(math.sqrt(number))+1)]
    y_vals = [i*50 for i in range(int(math.sqrt(number))+1)]
    pairs = [(x,y) for x in x_vals for y in y_vals]
    random.shuffle(pairs)
    xy = [[],[]]
    for i in range(number):
        xy[0].append(pairs[i][0])
        xy[1].append(pairs[i][1])
    return xy

@app.callback(
    Output(component_id='word-cloud', component_property='figure'),
    Input(component_id='tags-number', component_property='value'))
def display_wordcloud(number):
    xy = getXY(number)
    # a set of <number> tags with text, size and color information
    tags = text.get_tags(number)
    data = go.Scatter(x=xy[0],
                     y=xy[1],
                     mode='text',
                     text=tags[0],
                     marker={'opacity': 0.8},
                     textfont={'size': tags[1]})
    layout = go.Layout({'xaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False},
                        'yaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False},
                        'height': 800})
    return go.Figure(data=[data], layout=layout)

@app.callback(
    Output(component_id='word-distribution-bar', component_property='figure'),
    Input('word-cloud', 'clickData'))
def display_click_data(clickData):
    x = [i for i in range(1,51)]
    y = [1 for i in range(1,51)]
    if clickData != None:
        clicked_word = clickData['points'][0]['text']
        y = text.get_distribution(season, clicked_word)
    return px.bar(x=x,
                  y=y,
                  labels={'x': 'season','y':'frequency'},
                  height=400)

if __name__ == '__main__':
    app.run_server(debug=True, port=8080)
    
"""