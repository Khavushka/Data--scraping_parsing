import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px

app = dash.Dash(__name__)

names=['Winner', 'Loser', 'Location', 'class']
data = pd.read_csv('del_3_resultat.csv',names=names)

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
            dcc.Graph(id='graph') 
        ])
])

@app.callback(
    Output(component_id='graph', component_property='figure'),
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