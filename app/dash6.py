import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly_express as px
import pandas as pd

import dash_table

df = px.data.gapminder()
# df = df[df['continent']=='Asia']

app = dash.Dash()


app.layout = html.Div([
    html.H1('表の挿入'),
    html.H2('Gapminder Data', style={'textAlign':'center'}),
    dash_table.DataTable(
        style_cell={"textAlign":"center","width":"100px"},
        fixed_rows={"headers":True},
        page_size=15,
        sort_action = 'native',
        filter_action = 'native',
        columns=[{"name":col,"id":col} for col in df.columns],
        data=df.to_dict('records'),
        fill_width = False
    )
])


if __name__ == '__main__':
    app.run_server(debug=True,host='0.0.0.0',port=8001)