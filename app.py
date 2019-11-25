#!/usr/bin/env python
# coding: utf-8

# <div><div><div><div><h1>Dash Installation</h1><p><!-- react-text: 18130 -->In your terminal, install several dash libraries.
# These libraries are under active development,
#     
# <code>
# pip install dash==1.6.0  # The core dash backend
# pip install dash-daq==0.2.1  # DAQ components (newly open-sourced!)
# </code>

# <div><hr><h4>Generating HTML with Dash</h4><p><!-- react-text: 18300 -->Dash apps are composed of two parts. The first part is the "<!-- /react-text --><code>layout</code><!-- react-text: 18302 -->" of
# the app and it describes what the application looks like.
# The second part describes the interactivity of the application.<!-- /react-text --></p><p><!-- react-text: 18304 -->Dash provides Python classes for all of the visual components of
# the application. We maintain a set of components in the
# <!-- /react-text --><code>dash_core_components</code><!-- react-text: 18306 --> and the <!-- /react-text --><code>dash_html_components</code><!-- react-text: 18308 --> library
# </p></div>

# In[ ]:


#Here's a quick example

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)
server = app.server
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'line', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'line', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=False)


# <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">
# 
# [http://localhost:8050](http://localhost:8050)
# 
# Press  <i class="fa fa-stop"></i>  in the tool bar before execute the next cell

# Note:
# <ol><li><!-- react-text: 515 -->The <!-- /react-text --><code>layout</code><!-- react-text: 517 --> is composed of a tree of "components" like <!-- /react-text --><code>html.Div</code><!-- react-text: 519 -->
# and <!-- /react-text --><code>dcc.Graph</code><!-- react-text: 521 -->.<!-- /react-text --></li><li><!-- react-text: 523 -->The <!-- /react-text --><code>dash_html_components</code><!-- react-text: 525 --> library has a component for every HTML
# tag. The <!-- /react-text --><code>html.H1(children='Hello Dash')</code><!-- react-text: 527 --> component generates
# a <!-- /react-text --><code>&lt;h1&gt;Hello Dash&lt;/h1&gt;</code><!-- react-text: 529 --> HTML element in your application.<!-- /react-text --></li><li><!-- react-text: 531 -->Not all components are pure HTML. The <!-- /react-text --><code>dash_core_components</code><!-- react-text: 533 --> describe
# higher-level components that are interactive and are generated with
# JavaScript, HTML, and CSS through the React.js library.<!-- /react-text --></li><li><!-- react-text: 535 -->Each component is described entirely through keyword attributes.
# Dash is <!-- /react-text --><em><!-- react-text: 537 -->declarative<!-- /react-text --></em><!-- react-text: 538 -->: you will primarily describe your application
# through these attributes.<!-- /react-text --></li><li><!-- react-text: 540 -->The <!-- /react-text --><code>children</code><!-- react-text: 542 --> property is special. By convention, it's always the
# first attribute which means that you can omit it:
# <!-- /react-text --><code>html.H1(children='Hello Dash')</code><!-- react-text: 544 --> is the same as <!-- /react-text --><code>html.H1('Hello Dash')</code><!-- react-text: 546 -->.
# Also, it can contain a string, a number, a single component, or a
# list of components.<!-- /react-text --></li><li><!-- react-text: 548 -->The fonts in your application will look a little bit different than
# what is displayed here. This application is using a
# custom CSS stylesheet to modify the default styles of the elements, add<!-- /react-text --><pre><code>app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})
# </code></pre><!-- react-text: 554 -->to your file to get the same look and feel of these examples.<!-- /react-text --></li></ol>

# <h4>More about HTML</h4>
# 
# <p><!-- react-text: 557 -->The <!-- /react-text --><code>dash_html_components</code><!-- react-text: 559 --> library contains a component class for every
# HTML tag as well as keyword arguments for all of the HTML arguments.<!-- /react-text --></p>

# In[ ]:


#Here's a quick example that generates a `Table` from a Pandas dataframe.
import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd

df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/'
    'c78bf172206ce24f77d6363a2d754b59/raw/'
    'c353e8ef842413cae56ae3920b8fd78468aa4cb2/'
    'usa-agricultural-exports-2011.csv')

def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )

app = dash.Dash()
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

app.layout = html.Div(children=[
    html.H4(children='US Agriculture Exports (2011)'),
    generate_table(df)
])

if __name__ == '__main__':
    app.run_server(debug=False)


# <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">
# 
# [http://localhost:8050](http://localhost:8050)
# 
# Press  <i class="fa fa-stop"></i>  in the tool bar before execute the next cell

# <div><h4>More about Visualization</h4><p><!-- react-text: 1082 -->The <!-- /react-text --><code>dash_core_components</code><!-- react-text: 1084 --> library includes a component called <!-- /react-text --><code>Graph</code><!-- react-text: 1086 -->.<!-- /react-text --></p><p><code>Graph</code><!-- react-text: 1089 --> renders interactive data visualizations using the open source
# <!-- /react-text --><a href="https://github.com/plotly/plotly.js"><!-- react-text: 1091 -->plotly.js<!-- /react-text --></a><!-- react-text: 1092 --> JavaScript graphing
# library. Plotly.js supports over 35 chart types and renders charts in
# both vector-quality SVG and high-performance WebGL.<!-- /react-text --></p><p><!-- react-text: 1094 -->The <!-- /react-text --><code>figure</code><!-- react-text: 1096 --> argument in the <!-- /react-text --><code>dash_core_components.Graph</code><!-- react-text: 1098 --> component is
# the same <!-- /react-text --><code>figure</code><!-- react-text: 1100 --> argument that is used by <!-- /react-text --><code>plotly.py</code><!-- react-text: 1102 -->, Plotly's
# open source Python graphing library.
# Check out the <!-- /react-text --><a href="https://plot.ly/python"><!-- react-text: 1104 -->plotly.py documentation and gallery<!-- /react-text --></a><!-- react-text: 1105 -->
# to learn more.<!-- /react-text --></p></div>

# In[3]:


import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})


df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/' +
    '5d1ea79569ed194d432e56108a04d188/raw/' +
    'a9f9e8076b837d541398e999dcbac2b2826a81f8/'+
    'gdp-life-exp-2007.csv')

app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                go.Scatter(
                    x=df[df['continent'] == i]['gdp per capita'],
                    y=df[df['continent'] == i]['life expectancy'],
                    text=df[df['continent'] == i]['country'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.continent.unique()
            ],
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'GDP Per Capita'},
                yaxis={'title': 'Life Expectancy'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server()


# <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">
# 
# [http://localhost:8050](http://localhost:8050)
# 
# Press  <i class="fa fa-stop"></i>  in the tool bar before execute the next cell

# <div><h4>Core Components</h4><p><!-- react-text: 1341 -->The <!-- /react-text --><code>dash_core_components</code><!-- react-text: 1343 --> includes a set a higher-level components like
# dropdowns, graphs, markdown blocks, and more.<!-- /react-text --></p><p><!-- react-text: 1345 -->Like all Dash components, they are described entirely declaratively.
# Every option that is configurable is available as a keyword argument
# of the component.<!-- /react-text --></p></div>
# 
# Here are a few of the available components:

# In[5]:


import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash()
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})


app.layout = html.Div([
    html.Label('Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
    ),

    html.Label('Multi-Select Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value=['MTL', 'SF'],
        multi=True
    ),

    html.Label('Radio Items'),
    dcc.RadioItems(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
    ),

    html.Label('Checkboxes'),
    dcc.Checklist(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value=['MTL', 'SF']
    ),

    html.Label('Text Input'),
    dcc.Input(value='MTL', type='text'),

    html.Label('Slider'),
    dcc.Slider(
        min=1,
        max=8,
        marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 9)},
        value=5,
    ),
], style={'columnCount': 2})

if __name__ == '__main__':
    app.run_server(debug=False)


# <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">
# 
# [http://localhost:8050](http://localhost:8050)
# 
# Press  <i class="fa fa-stop"></i>  in the tool bar before execute the next cell

# <div><h3>Summary</h3><p><!-- react-text: 1702 -->The <!-- /react-text --><code>layout</code><!-- react-text: 1704 --> of a Dash app describes what the app looks like.
# The <!-- /react-text --><code>layout</code><!-- react-text: 1706 --> is a hierarchical tree of components.
# The <!-- /react-text --><code>dash_html_components</code><!-- react-text: 1708 --> library provides classes for all of the HTML
# tags and the keyword arguments describe the HTML attributes like <!-- /react-text --><code>style</code><!-- react-text: 1710 -->,
# <!-- /react-text --><code>className</code><!-- react-text: 1712 -->, and <!-- /react-text --><code>id</code><!-- react-text: 1714 -->.
# The <!-- /react-text --><code>dash_core_components</code><!-- react-text: 1716 --> library generates higher-level
# components like controls and graphs.<!-- /react-text --></p><p><!-- react-text: 1718 -->For reference, see:<!-- /react-text --></p></div>
# 
# <ul>
# <li><code>dash_core_components</code> <a href = https://plot.ly/dash/dash-core-components> gallery<!-- /react-text --></a></li>
# <li><code>dash_html_components</code> <a href = https://plot.ly/dash/dash-html-components> gallery<!-- /react-text --></a></li></ul>
