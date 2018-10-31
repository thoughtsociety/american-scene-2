# coding=utf-8

from flask import Flask
import plotly.graph_objs as go

import dash_core_components as dcc
import dash_html_components as html
import dash

from dash.dependencies import Input, Output

# hard_gray = '#ffffff'
text_color = 'rgb(36,36,36)'
bg_color = 'rgb(255,255,255)'
grid_color = '#a6a6a6'
#hard_gray = '#000000'
block_quote_text = 'rgb(64,64,64)'
blue_text = 'rgb(51, 153, 255)'
hard_gray = 'rgb(77,77,77)'

server = Flask(__name__)

elections = dash.Dash(__name__,
                server=server,
                url_base_pathname='/elections/',
                csrf_protect=False)


s3_css_mycss = "https://s3.us-east-2.amazonaws.com/tswrkdataset/css/my.css"
s3_css_typography = "https://s3.us-east-2.amazonaws.com/tswrkdataset/css/typography.css"


# elections.config.include_asset_files = True
#
# elections.css.append_css("my.css")

# chris's css
elections.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})
# my and typography.css from S3 bucket
elections.css.append_css({"external_url": s3_css_mycss})
# elections.css.append_css({"external_url": s3_css_typography})

tabs_styles = {
    'height': '54px'
	# 'color': 'rgb(51,153,255)'
}
tab_style = {
    'borderBottom': '2px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold',
	'font-size':'24px',
	'color': hard_gray,
	'backgroundColor':'rgba(0,0,0,0)'
}

tab_selected_style = {
    'borderTop': '2px solid #d6d6d6',
    'borderBottom': '2px solid #d6d6d6',
    'backgroundColor': '#119DFF',
	'font-size':'24px',
	'color': hard_gray,
    'padding': '6px'
}


elections.layout = html.Div([
    dcc.Tabs(id="tabs-styled-with-inline", value='tab-1', children=[
        dcc.Tab(label='Economic', value='tab-1', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Elections', value='tab-2', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Social', value='tab-3', style=tab_style, selected_style=tab_selected_style)

    ], style=tabs_styles),
	# html.H1("This should be big and black"),
    html.Div(id='tabs-content-inline')
], style={'border-width': '2px', 'border-color': hard_gray}
)



@elections.callback(Output('tabs-content-inline', 'children'),
              [Input('tabs-styled-with-inline', 'value')])
def render_content(tab):

	if tab == 'tab-1':
		return html.Div([

			dcc.Graph(
			config={
				'displayModeBar':False

				#'queueLength':0
			},
			id='example-graph-1',
			figure = {
		        'data': [
		        {'x': [1, 2, 3], 'y': [4, 1, 2],
		         'type': 'bar', 'name': 'SF','color':'rgb(77,77,77)'},
		        {'x': [1, 2, 3], 'y': [2, 4, 5],
		         'type': 'bar', 'name': u'Montréal'},
		        ],
				'layout': go.Layout(
					title='This is the Economic Slide',
					titlefont=dict(family='Helvetica Neue', size=32, color=hard_gray),
					legend=dict(font=dict(family='sans-serif', size=12, color=hard_gray)),
					xaxis=dict(tickfont=dict(size=12, color=hard_gray)),
					yaxis=dict(tickfont=dict(size=12, color=hard_gray)),
					paper_bgcolor='rgba(0,0,0,0)',
					plot_bgcolor='rgba(0,0,0,0)'
				)
			}
			)
		], className="._dash-undo-redo")

	elif tab == 'tab-2':
		return html.Div([
			dcc.Graph(
			config={
				'displayModeBar': False
			},
			id='example-graph-2',
			figure={
				'data': [
					{'x': [1, 2, 3], 'y': [3, 2, 4],
					 'type': 'bar', 'name': 'SF', 'color': 'rgb(77,77,77)'},
					{'x': [1, 2, 3], 'y': [1, 2, 3],
					 'type': 'bar', 'name': u'Montréal'}
				],
				'layout': go.Layout(
					title='This is the Elections Slide',
					titlefont=dict(family='Helvetica Neue', size=32, color=hard_gray),
					legend=dict(font=dict(family='sans-serif', size=12, color=hard_gray)),
					xaxis=dict(tickfont=dict(size=12, color=hard_gray)),
					yaxis=dict(tickfont=dict(size=12, color=hard_gray)),
					paper_bgcolor='rgba(0,0,0,0)',
					plot_bgcolor='rgba(0,0,0,0)'
				)
			}
			)
		],className="._dash-undo-redo")

	elif tab == 'tab-3':
		return html.Div([
			dcc.Graph(
			config={
				'displayModeBar': False
			},
			id='example-graph-3',
			figure={
				'data': [
					{'x': [1, 2, 3], 'y': [2, 4, 3],
					 'type': 'bar', 'name': 'SF', 'color': 'rgb(77,77,77)'},
					{'x': [1, 2, 3], 'y': [4, 5, 2],
					 'type': 'bar', 'name': u'Montréal'},
				],
				'layout': go.Layout(
					title='This is the Social Slide',
					titlefont=dict(family='Helvetica Neue', size=32, color=hard_gray),
					legend=dict(font=dict(family='sans-serif',size=12,color=hard_gray)),
					xaxis=dict(tickfont=dict(size=12,color=hard_gray)),
					yaxis=dict(tickfont=dict(size=12,color=hard_gray)),
					paper_bgcolor='rgba(0,0,0,0)',
					plot_bgcolor='rgba(0,0,0,0)'
				)
			}
			)
		],className="._dash-undo-redo")




	#
	# elif tab == 'tab-2':
	#     return html.Div([
	# 	    dcc.Graph(
	# 	    id='example-graph-2',
	# 	    figure={
	# 			    'data': [
	# 				    {'x': [1, 2, 3], 'y': [1, 4, 1],
	# 				     'type': 'bar', 'name': 'SF'},
	# 				    {'x': [1, 2, 3], 'y': [1, 2, 3],
	# 				     'type': 'bar', 'name': u'Montréal'},
	# 			    ],
	# 			    'layout': go.Layout(
	# 					title = 'This is the Elections Slide',
	# 					titlefont=dict(family='Helvetica Neue',
	# 					               size=15,
	# 					               color= hard_gray),
	# 					legend=dict(color=hard_gray),
	# 					paper_bgcolor = 'rgba(0,0,0,0)',
	# 					plot_bgcolor = 'rgba(0,0,0,0)'
	# 				    )
	# 		        }
	#             )
	# 	])
	#
	# elif tab == 'tab-3':
	#     return html.Div([
	# 	    dcc.Graph(
	# 	    id='example-graph-3',
	# 	    figure={
	# 			    'data': [
	# 				    {'x': [1, 2, 3], 'y': [2, 4, 3],
	# 				     'type': 'bar', 'name': 'SF'},
	# 				    {'x': [1, 2, 3], 'y': [2, 1, 3],
	# 				     'type': 'bar', 'name': u'Montréal'},
	# 			    ],
	# 				'layout': go.Layout(
	# 					title = 'This is the Social Slide',
	# 					titlefont=dict(family='Helvetica Neue',
	# 					               size=15,
	# 					               color= hard_gray),
	# 					legend=dict(color=hard_gray),
	# 					paper_bgcolor = 'rgba(0,0,0,0)',
	# 					plot_bgcolor = 'rgba(0,0,0,0)'
	# 				    )
	# 		        }
	#             )
	# 	])
	#


if __name__ == '__main__':
	elections.run_server(debug=True)