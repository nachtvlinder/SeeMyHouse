import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

app = dash.Dash()

app.layout = html.Div([

    html.H1('SeeMyHouse'),

    dcc.Markdown('''
        A python script for rendering a 3D model 
        of a house at given coordinates 
        based on a user-provided GeoTIFF.
    '''),

    dcc.Graph(
        id='graph',
        # figure={
        #     'data' [
        #         # go.Bar(x=[1, 2, 3], y=[4, 1, 2])
        #     ]
        # }
    )

])
