import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly_express as px
import pandas as pd

df = px.data.gapminder()
# df = df[df['continent']=='Asia']

app = dash.Dash()

year_options=[]
for year in df['year'].unique():
    year_options.append({'label':str(year), 'value':year})

continent_options=[]
for continent in df['continent'].unique():
    continent_options.append({'label':str(continent),'value':continent})

app.layout = html.Div([
    html.H1('コールバック3ーグラフ'),
    dcc.Graph(id='graph'),
    html.H3('年を選んでください'),
    dcc.Dropdown(id='select-year',options=year_options, value=df['year'].min(),style={'width':'30%'}),
    html.H3('大陸を選んでください'),
    dcc.Dropdown(id='select-continent',options=continent_options, value='Asia',style={'width':'30%'}),

])

@ app.callback(
    Output('graph', 'figure'),
    Input('select-year', 'value'),
    Input('select-continent','value')
) 

def update_figure(selected_year, selected_continent):
    df2 = df[df['year']==selected_year]
    filtered_df = df[df['continent']==selected_continent]
    figure = px.scatter(filtered_df, x='gdpPercap',y='lifeExp', log_x=True)
    return figure

if __name__ == '__main__':
    app.run_server(debug=True,host='0.0.0.0',port=8001)