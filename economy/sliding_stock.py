#
# An experimental sliding-stock application
#


# Imports  =============================================

import plotly
plotly.__version__

import plotly.plotly as py
import plotly.graph_objs as go
import plotly.offline as pyo
from datetime import datetime
import pandas_datareader.data as web
import numpy as np
import scipy
from scipy.linalg import norm

#         =============================================



df_aapl = web.DataReader('AAPL.US', 'quandl',
                    datetime(2016, 10, 1),
                    datetime(2018, 10, 29))

#df_appl_norm = [number/scipy.linalg.norm(df_aapl) for number in df_aapl]

df_msft = web.DataReader('MSFT.US', 'quandl',
                     datetime(2016, 10, 1),
                     datetime(2018, 10, 29))

df_fred_gdp = web.DataReader('GDP', 'fred',
                     datetime(2016, 10, 1),
                     datetime(2018, 10, 29))

df_gdp_norm = [number/norm(df_fred_gdp['GDP']) for number in df_fred_gdp]

traces = []

#traces.append({'x': f_djia['Date'], 'y': f_djia['Close'], 'name': 'djia'}),

# traces.append( {trace_appl = go.Scatter(x=list(df_aapl.index),y=list(df_aapl.High))} )
# traces.append( {trace_msft = go.Scatter(x=list(df_msft.index),y=list(df_msft.High))} )

trace_appl = go.Scatter(x=list(df_aapl.index),y=list(df_aapl.High),name='Apple')
trace_msft = go.Scatter(x=list(df_msft.index),y=list(df_msft.High),name='Microsoft')
trace_gdp = go.Scatter(x=list(df_gdp_norm.index),y=list(df_gdp_norm.GDP),name='GDP')

traces.append(trace_appl)
traces.append(trace_msft)
traces.append(trace_gdp)

data = traces
layout = dict(
    title='Time series with range slider and selectors',
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label='1m',
                     step='month',
                     stepmode='backward'),
                dict(count=6,
                     label='6m',
                     step='month',
                     stepmode='backward'),
                dict(count=1,
                    label='YTD',
                    step='year',
                    stepmode='todate'),
                dict(count=1,
                    label='1y',
                    step='year',
                    stepmode='backward'),
                dict(step='all')
            ])
        ),
        rangeslider=dict(
        visible = True
        ),
        type='date'
    )
)

fig = dict(data=data, layout=layout)
pyo.plot(fig,filename='slider.html')