import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
    html.H1('コールバック'),
    dcc.Input(id='input_test_id', value='initial value', type='text'),
    html.Div(id='output_div_id')
])

@ app.callback(
    Output('output_div_id', 'children'),
    Input('input_test_id', 'value')
) 

def update_output_div(input_value):
    return '入力は"{}"です。'.format(input_value)

if __name__ == '__main__':
    app.run_server(debug=True,host='0.0.0.0',port=8001)