#!/usr/bin/env python
# coding: utf-8

# In[26]:


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import plotly
import dash_table


# In[127]:


stylesheet = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=stylesheet)

#new = MetMuseum[['Object ID','Department','AccessionYear','Object Name','Title','Culture','Country','Classification','Link Resource']]
#new.dropna(subset = ['Culture','Country','Classification','Title'], inplace=True)
#new.to_csv('newMET.csv')

MET= pd.read_csv("newMET.csv", index_col=False)
options = ['1939.0', '1940.0','1941.0','1942.0','1943.0','1944.0','1945.0','1946.0','1947.0']
MET = MET[MET['AccessionYear'].isin(options)]

dff = MET.groupby('AccessionYear', as_index=False)[['Object ID','Country','Culture']].nunique()
#dff.columns=['AccessionYear','Total Objects Amount', 'Countries Count', 'Culture Types Count']
print (dff[:9])

app.layout = html.Div([
    html.Div([
        html.H1(children = 'MET Museum Collections Sample around World War II Period',
               style = {
                   'textAlign':'center',
                   'color':'#00008b'
               }),
        html.Div(children= 'The Metropolitan Museum of Art presents over 5,000 years of art from around the world. Founded in 1870, The Museum lives in two iconic sites in New York City, USA. The dashboard summarizes the information of over seven hundred objects information from MET. This project is designed to simulate the trend that how’s the new enroll collections’ amount changes during World War II Period. Considering the effect after the war, this database also includes two more years after year 1945.',
                style={
                    'textAlign':'left',
                    'color':'#000000'
                }),  
        
        dcc.Markdown("""
                 ###### search criteria
                 - Object Amount: Total objects amount counted by the object ID
                 - Culture: Information about the culture, or people from which an object was created
                 - Country: Country where the artwork was created or found

                 """),
    html.Div([
        html.Div([
            html.H3(children = 'Objects total counted by year',
               style = {
                   'textAlign':'center',
                   'color':'#00008b'
               }),
        ],className='nine columns')
    ],className='row'),  
        
         html.Div(children= 'Please select the year in the left to observe the changes of graphs below',
                style={
                    'textAlign':'left',
                    'color':'#000000'
                }),             
        
        dash_table.DataTable(
            id='datatable_id',
            data=dff.to_dict('records'),
            columns=[
                {"name": i, "id": i, "deletable": False, "selectable": False} for i in dff.columns
            ],
            editable=False,
            filter_action="native",
            sort_action="native",
            sort_mode="multi",
            row_selectable="multi",
            row_deletable=False,
            selected_rows=[],
            page_action="native",
            page_current= 0,
            page_size= 9,

style_cell_conditional=[
                {'if': {'column_id': 'AccessionYear'},
                 'width': '30%', 'textAlign': 'left'},
                {'if': {'column_id': 'Objects ID'},
                 'width': '30%', 'textAlign': 'left'},
                {'if': {'column_id': 'Country'},
                 'width': '30%', 'textAlign': 'left'},
                {'if': {'column_id': 'Culture'},
                 'width': '30%', 'textAlign': 'left'},
            ],
        ),
    ],className='row'),  
                                                                              
    html.Div([
        html.Div([
            html.H6('Select a category to see their ratios'),
            dcc.Dropdown(id='piedropdown',
               options=[{'label': 'Object Amount', 'value': 'Object ID'},
                        {'label': 'Country', 'value': 'Country'},
                        {'label': 'Culture', 'value': 'Culture'}
            ],
            value='Object ID',
            multi=False,
            clearable=False
        ),
        ],className='nine columns')
    ],className='row'),   
        
    html.Div([
       html.Div([        
           dcc.Graph(id='piechart'),
           ],className='nine columns'),
                                                                              
    ],className='row'),        

    html.Div([
        html.Div([
            html.H6('Select a category to see how objects distributed within MET art departments'),
            dcc.Dropdown(id='bardropdown',
               options=[{'label': 'Country', 'value': 'Country'},
                        {'label': 'Culture', 'value': 'Culture'}
                ],
                value='Culture',
                multi=False,
                clearable=False
            ),
        ],className='nine columns'),    
    ],className='row'),   
    
    html.Div([
         html.Div([
             dcc.Graph(id='barchart'),
             ],className='nine columns')

    ],className='row'),
    
    html.Br(),
    html.Br(),
    dcc.Markdown("""
                 ##### References:
                 Here is a list of data sources and references used in this course project.
                 - The Metropolitan Museum of Art Collection API:https://metmuseum.github.io
                 - Dash Plotly Multipel Output & Input:https://www.youtube.com/watch?v=dgV3GGFMcTc&t=1758s
                 - Interactive Dashboard with Python: https://www.youtube.com/watch?v=acFOhdo_bxw

                 April 2021, Florence Gu
                 """)



])
    
@app.callback(
    [Output('piechart', 'figure'),
     Output('barchart', 'figure')],
    [Input('datatable_id', 'selected_rows'),
     Input('piedropdown', 'value'),
     Input('bardropdown', 'value')]
)
def update_data(chosen_rows,piedropval,bardropval):
    if len(chosen_rows)==0:
        df_filterd = dff[dff['AccessionYear'].isin(['1939.0', '1940.0','1941.0','1942.0','1943.0','1944.0','1945.0','1946.0','1947.0'])]
    else:
        print(chosen_rows)
        df_filterd = dff[dff.index.isin(chosen_rows)]

    pie_chart=px.pie(
            data_frame=df_filterd,
            names='AccessionYear',
            values=piedropval,
            hole=.3,
            labels={'AccessionYear':'Years','Object ID':'Total Objects Amount'},
            title='The Ratio of Objects Amount among Years'
            )
    

    list_chosen_years=df_filterd['AccessionYear'].tolist()
    df_bar = MET[MET['AccessionYear'].isin(list_chosen_years)]

    bar_chart =px.bar(
            data_frame=df_bar,
            x='Department',
            y=bardropval,
            color='AccessionYear',
            labels={'AccessionYear':'AccessionYear', 'Department':'MET Museum Department'},
            title='The Attributes of Objects Managed by Each Department'
            )
     
    bar_chart.update_layout(uirevision='foo')

    return (pie_chart,bar_chart)


if __name__ == '__main__':
    app.run_server()


# In[ ]:




