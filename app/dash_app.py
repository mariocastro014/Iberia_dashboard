from app import data_requets
from dash import dcc, html, Dash
import plotly.express as px
import plotly.graph_objs as go


def create_dash_application(flask_app):
    raised_incidences = data_requets.raised_incidences_month()
    total = raised_incidences.groupby(['Months'])['Incidences'].sum().reset_index()
    critical = raised_incidences[raised_incidences['Priority']=='Crítica']
    alta = raised_incidences[raised_incidences['Priority']=='Alta']
    media = raised_incidences[raised_incidences['Priority']=='Media']
    baja = raised_incidences[raised_incidences['Priority']=='Baja']
   
    
    # data_frame_bars = [total,critical]
    
    # for x in range(1,len(data_frame_bars)):
    dash_app = Dash( server= flask_app , name="Dashboard-1", url_base_pathname="/total_incidents_1/", external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css'])
    dash_app.layout = html.Div(
        children=[
            dcc.Graph(
                id="Graph-1",
                figure=go.Figure(data=[go.Scatter(x=total['Months'], y=total['Incidences'])])
            ),
            dcc.Graph(
                id="Graph-2",
                figure=px.bar(total, x="Months", y="Incidences", barmode="group")
            )
        ]
    )
    
    dash_app = Dash( server= flask_app , name="Dashboard-2", url_base_pathname="/total_incidents_2/", external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css'])
    dash_app.layout = html.Div(
        children=[
            dcc.Graph(
                id="Graph-3 ",
                figure=px.bar(critical, x="Months", y="Incidences", barmode="group")
            )
        ]
    )
    dash_app = Dash( server= flask_app , name="Dashboard-3", url_base_pathname="/total_incidents_3/", external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css'])
    dash_app.layout = html.Div(
        children=[
            dcc.Graph(
                figure={
                    'data': [
                        {'x': alta['Months'], 'y': alta['Incidences'], 'type': 'bar', 'name': 'Alto'},
                        {'x': media['Months'], 'y': media['Incidences'], 'type': 'bar', 'name': 'Medio'},
                        {'x': baja['Months'], 'y': baja['Incidences'], 'type': 'bar', 'name': 'Bajo'},
                    ],
                    'layout': {
                        'title': 'Dash Data Visualization'
                    }
                }
            )
        ]
    )
 
    return dash_app  