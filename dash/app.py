

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

app = dash.Dash(name='Bootstrap_docker_app',
                 server=server,
                url_base_pathname='/dash/',
                csrf_protect=False)

# Colors for white bg with black text

text_color = 'rgb(36,36,36)'
bg_color = 'rgb(255,255,255)'
grid_color = '#666666'
black_text = '#000000'
block_quote_text = 'rgb(64,64,64)'
blue_text = 'rgb(51, 153, 255)'

# Get Chryddyp's CSS for Dash from Codepen

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})
#app.css.append_css({'/Users/salvideoguy/static/reset.css'})

# get four excel datafiles - 1 for DJIA and the other for Nasdaq Tech Sector

djia = pd.read_excel('/tmp/data/djia.xls')
ndxt = pd.read_excel('/tmp/data/ndxt.xls')
ixic = pd.read_csv('/tmp/data/ixic.csv')
gspc = pd.read_csv('/tmp/data/gspc.csv')

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


app.layout=html.Div([   # top,rt,bot,lft


# html.H3('Market Trends Over a Dozen Years',style={'color':'black',
#     'text-align':'center','background-color':bg_color,
#         'margin-bottom': '0px','padding':'10px 0px 0px 0px'}
#
#         ),


    # combi-plots with dropdown

    html.Div([ # Upper-left div top
    html.H3('Nasdaq and S&P 500 Comparison', style={'color': blue_text}),
    dcc.Markdown('''***'''),
    dcc.Graph(id='djia_id'), # djia graph
    dcc.Markdown('''***'''),
    html.Div([ # for quoteblock
    dcc.Markdown('''>Two indices in comparison: Looking at both the Nasdaq
    and S&P-500, we can see that they both easily reflect the *crash of 2009*
    right after the housing crisis starting taking effect.
    ''')

        ], style={'height':'200px'}
        ),
    dcc.Markdown('''***'''),
    ],style={'height':'200px','width':'40%',
              'padding':'10px 40px 10px 40px','display':'inline-block','border-width':'1px'}
    ),

    html.Div([  # Upper-right div
    html.H3('Nasdaq Tech Sector Closing Price', style={'color': blue_text}),
    dcc.Markdown('''***'''),
    dcc.Graph(id='ndxt_id'),  # djia graph
    dcc.Markdown('''***'''),
    html.Div([
    dcc.Markdown('''>**The Nasdaq Tech Sector Index**
    is a measure of the power of technology in the marketplace.
    Since tech is the engine of the bull market right now, it pays to
    keep a sharp eye on this sector now and into the future. **The Nasdaq Tech Sector Index**
    is a measure of the power of technology in the marketplace.
    Since tech is the engine of the bull market right now, it pays to
    keep a sharp eye on this sector now and into the future.
    
   ''')

        ], style={'height': '200px'}
        ),
    dcc.Markdown('''***'''),
    ], style={'height':'200px','width': '40%',
              'padding': '10px 40px 10px 40px', 'display': 'inline-block', 'border-width': '1px'}
    ),


    #dcc.Markdown('''***'''),
    # ],style={'height':'200px','width':'40%',
    #              'padding':'10px 40px 10px 40px','display':'inline-block'}
    # )
    #
    # html.Div([
    # dcc.Markdown('''***'''),
    # dcc.Graph(id='ndxt_id'), # ndxt graph
    # dcc.Markdown('''***'''),
    #     html.Div([
    #     dcc.Markdown('''>**Nasdaq Tech Sector Index** This is an index that
    #     has paced major indices on its own. '''
    #             )
    #         ],style={'height':'200px'}
    #         ),
    # dcc.Markdown('''***'''),
    # ],style={'height':'200px','display':'inline-block'} #'width':'33.333%'
    # ),
    #
    # html.Div([
    # dcc.Graph(id='djiaII_id'), # ndxt graph
    # dcc.Markdown('''***'''),
    #     html.Div([
    #     dcc.Markdown('''>**Dow-Jones Industrial Averate ** This is an index that
    #     has paced major indices on its own. '''
    #     ),
    #         ],style={'height':'200px'}
    #     ),
    # dcc.Markdown('''***'''),
    # ],style={'height':'200px','display':'inline-block'} #'width':'33.333%'
    # ),
    #
    # html.Div([
    # dcc.Graph(id='gspc_id'), # ndxt graph
    # dcc.Markdown('''***'''),
    # dcc.Markdown('''>**Standard & Poor 500** This is an index that
    # has paced major indices on its own. '''
    # ),
    # dcc.Markdown('''***'''),
    # ],style={'height':'200px','display':'inline-block'} #'width':'33.333%'
    # ),
    #
    # html.Div([
    # dcc.Graph(id='ixic2_id'), # ixic graph
    # dcc.Markdown('''***'''),
    # dcc.Markdown('''>**Nasdaq Index** This is an index that
    # has paced major indices on its own. '''
    # ),
    # dcc.Markdown('''***'''),
    # ],style={'height':'200px','display':'inline-block'} #'width':'33.333%'
    # ),
    #
    # html.Div([
    # dcc.Graph(id='gspc2_id'), # s&p graph
    # dcc.Markdown('''***'''),
    # dcc.Markdown('''>**Standard & Poor 500** This is an index that
    # has paced major indices on its own. '''
    # ),
    # dcc.Markdown('''***'''),
    # ],style={'height':'200px','display':'inline-block'} #'width':'33.333%'
    # ),
    #
html.Div(dcc.Slider(  # The years range slider
            id='years-range-slider',
            min=2006,
            max=2018,
            value=2018,
            step=2,
            marks= {i: '{}'.format(i) for i in year_index},

        ), style={'color':'red','margin-top': '0px','width': '97.33%',
                  'padding':'30px 38px 30px 30px', # top,rt,bot,lft
                  'background-color':bg_color}
    )

]

)

#### Callbacks

# trace all the closing values from year.min to selected max.year using the 'value' (highest year)
# reshape the array in a temporary array and run it to the end.

# button callbacks to navigate between the three apps

# @app.callback(
#    Input('dash1_button',pressed)
# def select_dash1_graph(pressed):
#    if pressed:
#        html
# )

@app.callback( # Stock # 1 - DJIA
    Output('djia_id', 'figure'),
    [Input('years-range-slider', 'value')])
def update_stock_graph(value):

    # print (value)

    # original cutoff for the slider
    # cutoff = (value - first_year) * 12

    '''
    To use the dropdown, produce a slice range that grabs just the rows
    from the selected year and copies it into the f_djia df
    each date has 12 rows of data - 1 for each month
    To set a lower and upper mask to slice the df, it is the first row of the chosen date +12

    value = integer year.  years go from 2006 - 2018 or 6-18.  This is essentially a range of 12 years.
    For 12 months.  So the index range is 0-143.  If the selected year is 2010


    '''

    #year_val = (int(value) - 2005) - 1
    #year_end = year_val + 12


    traces = []
    cutoff = (value - first_year) * 12

    f_djia = djia[0:cutoff]
    f_ndxt = ndxt[0:cutoff]
    f_ixic = ixic[0:cutoff]
    f_gspc = gspc[0:cutoff]

    #f_djia = djia[year_val:year_end]
    #f_ndxt = ndxt[year_val:year_end]
    #f_ixic = ixic[year_val:year_end]
    #f_gspc = gspc[year_val:year_end]



    # traces.append({'x': f_djia['Date'], 'y': f_djia['Close'], 'name': 'djia'}),
    # traces.append({'x': f_ndxt['Date'], 'y': f_ndxt['Close'], 'name': 'ndxt'}),
    # traces.append({'x': f_ixic['Date'], 'y': f_ixic['Close'], 'name': 'ixic'}),
    # traces.append({'x': f_gspc['Date'], 'y': f_gspc['Close'], 'name':'gspc'}),

    # fig = {
    #     'data': traces,
    #     'layout': {'title':'DJIA, NDXT, NASDAQ, S&P Closings',
    #                'paper_bgcolor':bg_color,'plot_bgcolor':bg_color,
    #                'font': {'color':text_color},
    #                'xaxis':{'gridcolor':grid_color,'range':[cutoff-first_year],'step':1},
    #                'yaxis': {'gridcolor': grid_color},
    #                'auto_size':False,
    #                'width':433,
    #                'height':400
    #
    # }
    # }
    fig = {
        'data': [
            go.Scatter(
                x=f_ixic['Date'],
                y=f_ixic['Close'],
                mode='lines',
                marker = {
                    'size':4,
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
        'layout':{ 'paper_bgcolor': bg_color, 'plot_bgcolor': bg_color,
                   'font': {'color': text_color},
                   'xaxis': {'title':'Years','gridcolor': grid_color, 'range': [cutoff - first_year], 'step': 1},
                   'yaxis': {'title':'Closing Price','gridcolor': grid_color},
                   'auto_size': False,
                   'width': 433,
                   'height': 400
                }
        }
    return fig


@app.callback( # Stock #2 NDXT
    Output('ndxt_id', 'figure'),
    [Input('years-range-slider', 'value')])
def update_stock_graph(value):

    traces = []
    cutoff = (value - first_year) * 12
    f_ndxt = ndxt[0:cutoff]

    traces.append({'x': f_ndxt['Date'], 'y': f_ndxt['Close'], 'name': 'ndxt'}),

    fig = {
        'data': traces,
        'layout': {'paper_bgcolor':bg_color,'plot_bgcolor':bg_color,'font': {'color':text_color},
                   'xaxis': {'gridcolor': grid_color},
                   'yaxis': {'gridcolor': grid_color} ,
                   'auto_size': False,
                   'width':433,
                   'height':400
                   }
    }
    return fig
#
# @app.callback( # Stock #3 IXIC
#     Output('djiaII_id', 'figure'),
#     [Input('years-range-slider', 'value')])
# def update_stock_graph(value):
#
#     traces = []
#     cutoff = (value - first_year) * 12
#     f_djia = djia[0:cutoff]
#
#     traces.append({'x': f_djia['Date'], 'y': f_djia['Close'], 'name': 'djia'}),
#
#     fig = {
#         'data': traces,
#         'layout': {'title':'Djia Closing Price',
#                    'paper_bgcolor':bg_color,'plot_bgcolor':bg_color,'font': {'color':text_color},
#                    'xaxis': {'gridcolor': grid_color},
#                    'yaxis': {'gridcolor': grid_color} ,
#                    'auto_size': False,
#                    'width': 433,
#                    'height': 400
#                    }
#     }
#     return fig
#
# @app.callback( # Stock #4 GSPC
#     Output('gspc_id', 'figure'),
#     [Input('years-range-slider', 'value')])
# def update_stock_graph(value):
#
#     traces = []
#     cutoff = (value - first_year) * 12
#     f_gspc = gspc[0:cutoff]
#
#     traces.append({'x': f_gspc['Date'], 'y': f_gspc['Close'], 'name': 'gspc'})
#     fig = {
#         'data': traces,
#         'layout': {'title':'S&P 500 Closing Price',
#                    'paper_bgcolor':bg_color,'plot_bgcolor':bg_color,'font': {'color':text_color},
#                    'xaxis': {'gridcolor': grid_color},
#                    'yaxis': {'gridcolor': grid_color} ,
#                    'auto_size': False,
#                    'width':433,
#                    'height':400
#                    }
#     }
#     return fig
#
# @app.callback( # Stock #3 IXIC
#     Output('ixic2_id', 'figure'),
#     [Input('years-range-slider', 'value')])
# def update_stock_graph(value):
#
#     traces = []
#     cutoff = (value - first_year) * 12
#     f_ixic = ixic[0:cutoff]
#
#     traces.append({'x': f_ixic['Date'], 'y': f_ixic['Close'], 'name': 'ixic2'}),
#
#     fig = {
#         'data': traces,
#         'layout': {'title':'Nasdaq-100 Closing Price',
#                    'paper_bgcolor':bg_color,'plot_bgcolor':bg_color,'font': {'color':text_color},
#                    'xaxis': {'gridcolor': grid_color},
#                    'yaxis': {'gridcolor': grid_color} ,
#                    'auto_size': False,
#                    'width':433,
#                    'height':400
#                    }
#     }
#     return fig
#
# @app.callback( # Stock #4 GSPC
#     Output('gspc2_id', 'figure'),
#     [Input('years-range-slider', 'value')])
# def update_stock_graph(value):
#
#     traces = []
#     cutoff = (value - first_year) * 12
#     f_gspc = gspc[0:cutoff]
#
#     traces.append({'x': f_gspc['Date'], 'y': f_gspc['Close'], 'name': 'gspc2'})
#     fig = {
#         'data': traces,
#         'layout': {'title':'S&P 500 Closing Price',
#                    'paper_bgcolor':bg_color,'plot_bgcolor':bg_color,'font': {'color':text_color},
#                    'xaxis': {'gridcolor': grid_color},
#                    'yaxis': {'gridcolor': grid_color} ,
#                    'auto_size': False,
#                    'width':433,
#                    'height':400
#                    }
#     }
#     return fig


if __name__ == '__main__':
    #app.run_server(ssl_context='adhoc')
    app.run_server(debug=True)
