import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly_express as px

df = px. data.gapminder()
app = dash.Dash()
app.layout = html.Div(children=[
    html.H1(children='Hello Dash H1!!!'),
    html.H2(children='Hello Dash H2!!!'),
    html.H3(children='Hello Dash H3!!!'),
])

if __name__=='__main__':
    app.run_server(port=8001)