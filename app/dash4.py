import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly_express as px
import pandas as pd

df = px.data.gapminder()
df = df[df['continent']=='Asia']

app = dash.Dash()

year_options=[]
for year in df['year'].unique():
    year_options.append({'label':str(year), 'value':year})

app.layout = html.Div([
    html.H1('コールバック2ーグラフ'),
    dcc.Graph(id='graph'),
    dcc.Dropdown(id='select-year',options=year_options, value=df['year'].min())
])

@ app.callback(
    Output('graph', 'figure'),
    Input('select-year', 'value')
) 

def update_fugure(selected_year):
    filtered_df = df[df['year']==selected_year]
    figure = px.scatter(filtered_df, x='gdpPercap',y='lifeExp', log_x=True, color='continent')
    return figure

if __name__ == '__main__':
    app.run_server(debug=True,host='0.0.0.0',port=8001)