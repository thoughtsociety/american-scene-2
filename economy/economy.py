#######
# First Milestone Project: Develop a Stock Ticker
# dashboard that either allows the user to enter
# a ticker symbol into an input box, or to select
# item(s) from a dropdown list, and uses pandas_datareader
# to look up and display stock data on a graph.
######

# EXPAND STOCK SYMBOL INPUT TO PERMIT MULTIPLE STOCK SELECTION
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import base64

from flask import Flask
import plotly.graph_objs as go

from datetime import datetime
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web # requires v0.6.0 or later

# some color constants that work with our theme

white_text = '#ffffff'
text_color = 'rgb(36,36,36)'
bg_color = 'rgb(255,255,255)'
grid_color = '#666666'
black_text = '#000000'
block_quote_text = 'rgb(64,64,64)'
blue_text = 'rgb(51, 153, 255)'
hard_gray = 'rgb(77,77,77)'


economy = dash.Dash(name='Bootstrap_docker_app',
                url_base_pathname='/economy/',
                csrf_protect=False)
server = economy.server

#
# External assets
#
s3_css_mycss = "https://s3.us-east-2.amazonaws.com/tswrkdataset/css/my.css"

economy.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})
economy.css.append_css({"external_url": s3_css_mycss})




nsdq = pd.read_csv("https://s3.us-east-2.amazonaws.com/tswrkdataset/economic/mkt_indices/NASDAQcompanylist.csv")

# logo_image = "https://s3.us-east-2.amazonaws.com/tswrkdataset/static/thought.png"
#
#

nsdq.set_index('Symbol', inplace=True)


options = []
for tic in nsdq.index:
    options.append({'label':'{} {}'.format(tic,nsdq.loc[tic]['Name']), 'value':tic})

'''
    This code block builds a set of divs that consist of :
        1. H1 and H3 labels
        2. Drop-down component to select the stock
        3. Date range picker component
        4. Button to initiate the selection
        5. Graph object within the div
'''

# def get_logo():
#     encoded_image = base64.b64encode(open(logo_image, "rb").read())
#     logo = html.Div(
#         html.Img(
#             src="data:image/png;base64,{}".format(encoded_image.decode()), height="42"
#         ),
#         style={"marginTop": "0"},
#         className="sept columns",
#     )
#     return logo


economy.layout = html.Div([
# html.Div([ get_logo() ]),
html.H2('Compare Stocks',style={'color':'rgb(0, 138, 230)'}),

html.Div([
    html.H4('Select stock symbols:', style={'paddingRight':'30px','color':'rgb(0, 138, 230)'}),
    dcc.Dropdown(
        id='my_ticker_symbol',
        options=options,
        value=['TSLA'],
        multi=True
    )
], style={'display':'inline-block', 'verticalAlign':'top', 'width':'30%','padding-bottom':'10'}),

html.Div([
    html.H4('Select date range:',style={'color':'rgb(0, 138, 230)'}),
    dcc.DatePickerRange(
        id='my_date_picker',
        min_date_allowed=datetime(2015, 1, 1),
        max_date_allowed=datetime.today(),
        start_date=datetime(2018, 1, 1),
        end_date=datetime.today(),

    )
], style={'display':'inline-block','padding': '0px 10px 0px 20px','height':'10%'} # top,rt,bot,lft
),

html.Div([
    html.Button(
        id='submit-button',
        n_clicks=0,
        children='Submit',
        style={'fontSize':16, 'marginLeft':'30px'}
    ),
], style={'display':'inline-block','color':'rgb(0, 138, 230)'}),

dcc.Graph(
    id='my_graph',
    figure={
        'data': [
            {'x': [1,2], 'y': [3,1]},

        ]
    }, style = {'border':'2px white solid'},
    className="._dash-undo-redo",
    config={'displayModeBar':False}

    # 'border':'2px','border-style': 'solid','color':'rgb(0, 138, 230)'
)
] )

@economy.callback(
    Output('my_graph', 'figure'),
    [Input('submit-button', 'n_clicks')],
    [State('my_ticker_symbol', 'value'),
    State('my_date_picker', 'start_date'),
    State('my_date_picker', 'end_date')])
def update_graph(n_clicks,stock_ticker, start_date, end_date):  #
    start = datetime.strptime(start_date[:10], '%Y-%m-%d')
    end = datetime.strptime(end_date[:10], '%Y-%m-%d')
    traces = []
    for tic in stock_ticker:
        df = web.DataReader(tic,'iex',start,end)
        traces.append({'x':df.index, 'y': df.close, 'name':tic})
    fig = {
        'data': traces,
        'layout':
            go.Layout(
                title= ','.join(stock_ticker)+ 'Closing Prices',
                titlefont=dict(family='Helvetica Neue', size=32, color=white_text),
                #legend=dict(font=dict(family='sans-serif', size=12, color=white_text)),
                xaxis=dict(tickfont=dict(size=12, color=white_text)),
                yaxis=dict(tickfont=dict(size=12, color=white_text)),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)'
            )
        #{'title':', '.join(stock_ticker)+' Closing Prices'}
    }
    return fig

if __name__ == '__main__':
    #economy.run_server(ssl_context='adhoc')
    economy.run_server()
