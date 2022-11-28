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
import glob

app = dash.Dash(__name__)


path = ('players_allInone.csv')

all_files = glob.glob(path)

all_files

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)
    
li

df = pd.concat(li, axis=0, ignore_index=True)
df

"""
app.layout = html.Div([
        html.H1("Plotting the IRIS data set"),
        html.Div([
            dcc.Dropdown(
                id='feature1',
                options=[{'label': i, 'value': i} for i in names],
                value='sepal-width'
            ),
            dcc.Dropdown(
                id='feature2',
                options=[{'label': i, 'value': i} for i in names],
                value='petal-width'
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
    figure = px.scatter(data, 
                      x=feature1,
                      y=feature2,
                      color="class")
    figure.update_traces(marker={'size': 15})
    return figure

if __name__ == '__main__':
    app.run_server(debug=True, port=8080)
    """