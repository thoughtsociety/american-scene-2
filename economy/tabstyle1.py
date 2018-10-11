# coding=utf-8

import dash
import dash_html_components as html
import dash_core_components as dcc

from dash.dependencies import Input, Output

app = dash.Dash()

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})



tabs_styles = {
    'height': '54px'
	# 'color': 'rgb(51,153,255)'
}
tab_style = {
    'borderBottom': '2px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold',
	'font-size':'24px',
	'color': 'rgb(51,153,255)'
}

tab_selected_style = {
    'borderTop': '2px solid #d6d6d6',
    'borderBottom': '2px solid #d6d6d6',
    'backgroundColor': '#119DFF',
	'font-size':'24px',
    'color': 'white',
    'padding': '6px'
}

app.layout = html.Div([
    dcc.Tabs(id="tabs-styled-with-inline", value='tab-1', children=[
        dcc.Tab(label='Economic', value='tab-1', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Elections', value='tab-2', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Social', value='tab-3', style=tab_style, selected_style=tab_selected_style),
        # dcc.Tab(label='Tab 4', value='tab-4', style=tab_style, selected_style=tab_selected_style),
    ], style=tabs_styles),
    html.Div(id='tabs-content-inline')
]) #,style={'width':'90%'})

@app.callback(Output('tabs-content-inline', 'children'),
              [Input('tabs-styled-with-inline', 'value')])
def render_content(tab):
	if tab == 'tab-1':
	    return html.Div([
			dcc.Graph(
			id='example-graph',
			figure={
			        'data': [
			        {'x': [1, 2, 3], 'y': [4, 1, 2],
			         'type': 'bar', 'name': 'SF'},
			        {'x': [1, 2, 3], 'y': [2, 4, 5],
			         'type': 'bar', 'name': u'Montréal'},
			    ]
				        }
			        )
		        ]),

	elif tab == 'tab-2':
	    return html.Div([
		    dcc.Graph(
		    id='example-graph-1',
		    figure={
			    'data': [
				    {'x': [1, 2, 3], 'y': [1, 4, 1],
				     'type': 'bar', 'name': 'SF'},
				    {'x': [1, 2, 3], 'y': [1, 2, 3],
				     'type': 'bar', 'name': u'Montréal'},
			    ]
		    }
	    )
		        ]),
	elif tab == 'tab-3':
	    return html.Div([
		    dcc.Graph(
		    id='example-graph-2',
		    figure={
			    'data': [
				    {'x': [1, 2, 3], 'y': [1, 4, 1],
				     'type': 'bar', 'name': 'SF'},
				    {'x': [1, 2, 3], 'y': [1, 2, 3],
				     'type': 'bar', 'name': u'Montréal'},
			    ]
		    }
	    )
		        ])



if __name__ == '__main__':
    app.run_server(debug=True)