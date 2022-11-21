# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 12:45:55 2022

@author: khavu
"""

import pandas as pd
import dash
from dash.dependencies import Input, Output
from dash import dcc
from dash import html
import plotly.express as px

app = dash.Dash(__name__)

names=['winner', 'loser', 'PtsW', 'PtsW']
path = pd.read_csv('season/page1.html.csv')


#minwinner = path['table'].min()

app.layout = html.Div([
        html.H1("Project 2: American Football"),
        html.Div([
            dcc.Dropdown(
                id='feature1',
                options=[{'label': i, 'value': i} for i in names],
                value='Winner'
            ),
            dcc.Dropdown(
                id='feature2',
                options=[{'label': i, 'value': i} for i in names],
                value='Loser'
            ),
        ]),
        html.Div([
            dcc.Graph(id='scatterplot') 
        ])
])

@app.callback(
    Output(component_id='scatterplot', component_property='figure'),
    [
        Input(component_id='feature1', component_property='value'),
        Input(component_id='feature2', component_property='value')
    ]
)
def update_output(feature1, feature2):
    figure = px.scatter(path, 
                      x=feature1,
                      y=feature2,
                      color="class")
    figure.update_traces(marker={'size': 15})
    return figure

if __name__ == '__main__':
    app.run_server(debug=True, port=8080)