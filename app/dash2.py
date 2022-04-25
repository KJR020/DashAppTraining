from logging import PlaceHolder
from tkinter.tix import CheckList
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly_express as px



app = dash.Dash()
app.layout = html.Div(children=[
    html.H2(children='Dropdown'),
    dcc.Dropdown(
        options=[
            {'label':'東京','value':'Tokyo'},
            {'label':'大阪','value':'Osaka'},
            {'label':'北海道','value':'Hokkaido'}
        ]
    ),

    html.H2(children='Slider'),
    dcc.Slider(min=0,max=10,step=1),

    html.H2(children='Input text'),
    dcc.Textarea(
        placeholder='ここに値を書いてね',
        style={"width":"50%"}
    ),

    html.H2(children='Check list'),
    dcc.Checklist(
        options=[
            {'label':'東京','value':'Tokyo'},
            {'label':'大阪','value':'Osaka'},
            {'label':'北海道','value':'Hokkaido'}
        ]
    ),

    html.H2(children='Radio button'),
    dcc.RadioItems(
        options=[
            {'label':'東京','value':'Tokyo'},
            {'label':'大阪','value':'Osaka'},
            {'label':'北海道','value':'Hokkaido'}
        ],value='Osaka'
    )
])

if __name__=='__main__':
    app.run_server(debug=True,host='0.0.0.0',port=8001)