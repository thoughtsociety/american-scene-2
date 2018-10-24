

# simple stock comparitor
from flask import Flask
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go

from datetime import datetime
import pandas as pd
import numpy as np
pd.core.common.is_list_like = pd.api.types.is_list_like
# import pandas_datareader.data as web # requires v0.6.0 or later


server = Flask(__name__)

economy = dash.Dash(name='Bootstrap_docker_app',
                 server=server,
                url_base_pathname='/economy/',
                csrf_protect=False)

# Colors for white bg with black text

text_color = 'rgb(36,36,36)'
bg_color = 'rgb(255,255,255)'
#grid_color = '#666666'
grid_color = 'ffffff'
black_text = '#000000'
block_quote_text = 'rgb(64,64,64)'
blue_text = 'rgb(51, 153, 255)'
hard_gray = 'rgb(77,77,77)'

s3_eco_mkt = "https://s3.us-east-2.amazonaws.com/tswrkdataset/economic/mkt_indices/"
s3_css_mycss = "https://s3.us-east-2.amazonaws.com/tswrkdataset/css/my.css"

# Get Chryddyp's CSS for Dash from Codepen
economy.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})
# mycss
economy.css.append_css({"external_url": s3_css_mycss})


# get four excel datafiles - 1 for DJIA and the other for Nasdaq Tech Sector

djia = pd.read_excel(s3_eco_mkt+"djia.xls")
ixic = pd.read_csv(s3_eco_mkt+"ixic.csv")
ndxt = pd.read_excel(s3_eco_mkt+"ndxt.xls")
gspc = pd.read_csv(s3_eco_mkt+"gspc.csv")


last_year = 2018
first_year = 2006

# Prepare a clean list of integer years from mkt_Index
# Return the list

def clean_mkt_index(mkt_Index):
    yrstr = []
    year_list = []  # holding unique year strings
    nyear = []

    for rawdatestr in mkt_Index['Date']:
        yrstr.append(rawdatestr[0:4]) # extract date info for all dates
    for years in np.unique(yrstr): # get unique date info by year
        year_list.append(years)
    del year_list[-1] # strip the last string which is invalid
    for nyr in year_list:
        nyear.append(int(nyr))
    return nyear

year_index = clean_mkt_index(djia) # integer years
year_index_strings = [str(item) for item in year_index] # year strings

options = []
i = 0

for year in year_index_strings:
    options.append({'label':'{}'.format(year),'value':year_index[i]})
    i+=1


economy.layout=html.Div([   # top,rt,bot,lft

    html.Div([

        html.Div([  # Upper-left div top
            html.H4('Nasdaq and S&P 500 Comparison', style={'color': blue_text}),
            dcc.Markdown('''***'''),
            dcc.Graph(id='djia_id',config={'displayModeBar':False},style={'border':'2px','float':'left'})

        ], style={'width': '49%',
                  'padding': '0px 0px 0px 0px', 'display': 'inline-block',
                  'box-sizing': 'border-box', 'border-width': '1px','paper_bgcolor':'rgba(0,0,0,0)',
                'plot_bgcolor':'rgba(0,0,0,0)'}
        ),

     # upper-left div top

        html.Div([  # Upper-right div
            html.H4('Nasdaq Tech Sector Closing Price', style={'color': blue_text}),
            dcc.Markdown('''***'''),
            dcc.Graph(id='ndxt_id',config={'displayModeBar':False},
                      style={'border':'2px','float':'right'}),  # djia graph

        ], style={'width': '49%',
                  'padding': '0px 0px 0px 0px', 'display': 'inline-block',
                  'box-sizing': 'border-box', 'border-width': '2px', 'border-color': 'grey'}

        ),
     ], style={'width':'99%', 'display': 'inline-block'}
),
    html.Div([

        html.Div([  # Upper-left div top
            html.H4('Nasdaq and S&P 500 Comparison', style={'color': blue_text}),
            dcc.Markdown('''***'''),
            dcc.Graph(id='djia_id_2',config={'displayModeBar':False},style={'border':'2px','float':'left'})

        ], style={'width': '49%',
                  'padding': '0px 0px 0px 0px', 'display': 'inline-block',
                  'box-sizing': 'border-box', 'border-width': '1px','paper_bgcolor':'rgba(0,0,0,0)',
                'plot_bgcolor':'rgba(0,0,0,0)'}
        ),

     # upper-left div top

        html.Div([  # Upper-right div
            html.H4('Nasdaq Tech Sector Closing Price', style={'color': blue_text}),
            dcc.Markdown('''***'''),
            dcc.Graph(id='ndxt_id_2',config={'displayModeBar':False},
                      style={'border':'2px','float':'right'}),  # djia graph

        ], style={'width': '49%',
                  'padding': '0px 0px 0px 0px', 'display': 'inline-block',
                  'box-sizing': 'border-box', 'border-width': '2px', 'border-color': 'grey'}

        ),
     ], style={'width':'99%', 'display': 'inline-block'}
),


        html.Div(
            dcc.Slider(  # The years range slider
            id='years-range-slider',
            min=2006,
            max=2018,
            value=2018,
            step=2,
            marks={i: '{}'.format(i) for i in year_index},

        ), style={'color': 'red', 'margin-top': '0px', 'width': '97.33%',
                  'padding': '30px 38px 30px 30px',
                  'paper_bgcolor': 'rgba(0,0,0,0)','plot_bgcolor':'rgba(0,0,0,0)'}  # top,rt,bot,lft}
            )


    ], className="._dash-undo-redo", style={'paper_bgcolor': 'rgba(0,0,0,0)','plot_bgcolor':'rgba(0,0,0,0)'}
)


#### Callbacks

# trace all the closing values from year.min to selected max.year using the 'value' (highest year)
# reshape the array in a temporary array and run it to the end.


@economy.callback(  # Stock # 1 - DJIA
    Output('djia_id', 'figure'),
    [Input('years-range-slider', 'value')])
def update_stock_graph(value):

    cutoff = (value - first_year) * 12

    f_ixic = ixic[0:cutoff]
    f_gspc = gspc[0:cutoff]

    fig = {
        'data': [
            go.Scatter(
                x=f_ixic['Date'],
                y=f_ixic['Close'],
                mode='lines',
                marker={
                    'size': 4,
                    'color': 'rgb(153, 0, 255)'
                },
                name='Nasdaq',
            ),
            go.Scatter(
                x=f_ixic['Date'],
                y=f_gspc['Close'],
                mode='markers',
                marker={
                    'size': 4,
                    'color': 'rgb(255, 0, 153)'
                },
                name='S&P-500',
            ),
        ],
        'layout': {'paper_bgcolor':'rgba(0,0,0,0)',
                   'plot_bgcolor': 'rgba(0,0,0,0)',
                   'font': {'color': grid_color},
                   'xaxis': {'title': 'Years', 'gridcolor': grid_color, 'range': [cutoff - first_year], 'step': 1},
                   'yaxis': {'title': 'Closing Price', 'gridcolor': grid_color},
                   'auto_size': False,
                   'width': 433,
                   'height': 433,
                   }
    }
    return fig

@economy.callback(  # Stock # 1 - DJIA
    Output('djia_id_2', 'figure'),
    [Input('years-range-slider', 'value')])
def update_stock_graph(value):

    cutoff = (value - first_year) * 12

    f_ixic = ixic[0:cutoff]
    f_gspc = gspc[0:cutoff]

    fig = {
        'data': [
            go.Scatter(
                x=f_ixic['Date'],
                y=f_ixic['Close'],
                mode='lines',
                marker={
                    'size': 4,
                    'color': 'rgb(153, 0, 255)'
                },
                name='Nasdaq',
            ),
            go.Scatter(
                x=f_ixic['Date'],
                y=f_gspc['Close'],
                mode='markers',
                marker={
                    'size': 4,
                    'color': 'rgb(255, 0, 153)'
                },
                name='S&P-500',
            ),
        ],
        'layout': {'paper_bgcolor':'rgba(0,0,0,0)',
                   'plot_bgcolor': 'rgba(0,0,0,0)',
                   'font': {'color': grid_color},
                   'xaxis': {'title': 'Years', 'gridcolor': grid_color, 'range': [cutoff - first_year], 'step': 1},
                   'yaxis': {'title': 'Closing Price', 'gridcolor': grid_color},
                   'auto_size': False,
                   'width': 433,
                   'height': 433,
                   }
    }
    return fig



@economy.callback(  # Stock #2 NDXT
    Output('ndxt_id', 'figure'),
    [Input('years-range-slider', 'value')])
def update_stock_graph(value):
    traces = []
    cutoff = (value - first_year) * 12
    f_ndxt = ndxt[0:cutoff]

    traces.append({'x': f_ndxt['Date'], 'y': f_ndxt['Close'], 'name': 'ndxt'}),

    fig = {
        'data': traces,
        'layout': {'paper_bgcolor':'rgba(0,0,0,0)',
                   'plot_bgcolor': 'rgba(0,0,0,0)',
                   'font': {'color': grid_color},
                   'xaxis': {'title': 'Years','gridcolor': grid_color},
                   'yaxis': {'gridcolor': grid_color},
                   'auto_size': False,
                   'width': 433,
                   'height': 400
                   }
    }
    return fig

@economy.callback(  # Stock #2 NDXT
    Output('ndxt_id_2', 'figure'),
    [Input('years-range-slider', 'value')])
def update_stock_graph(value):
    traces = []
    cutoff = (value - first_year) * 12
    f_ndxt = ndxt[0:cutoff]

    traces.append({'x': f_ndxt['Date'], 'y': f_ndxt['Close'], 'name': 'ndxt'}),

    fig = {
        'data': traces,
        'layout': {'paper_bgcolor':'rgba(0,0,0,0)',
                   'plot_bgcolor': 'rgba(0,0,0,0)',
                   'font': {'color': grid_color},
                   'xaxis': {'title': 'Years','gridcolor': grid_color},
                   'yaxis': {'gridcolor': grid_color},
                   'auto_size': False,
                   'width': 433,
                   'height': 400
                   }
    }
    return fig

if __name__ == '__main__':
    #economy.run_server(ssl_context='adhoc')
    economy.run_server(debug=True)
