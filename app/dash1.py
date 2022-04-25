import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly_express as px

df = px. data.gapminder()
markdown_text = '''
# Test markdown
This is test markdown !!!
'''

app = dash.Dash()
app.layout = html.Div(children=[
    html.H1(children='Hello Dash H1!!!'),
    html.H2(children='Hello Dash H2!!!'),
    html.H3(children='Hello Dash H3!!!'),

    dcc.Graph(
        id='test_graph',
        figure=px.scatter(df, x='gdpPercap', y='lifeExp', log_x=True),
        style={}
    

    ),

    dcc.Markdown(children=markdown_text)
])

if __name__=='__main__':
    app.run_server(debug=True,host='0.0.0.0',port=8001)