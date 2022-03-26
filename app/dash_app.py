from app import data_request
from dash import dcc, html, Dash, dash_table
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objs as go


def create_dash_application(flask_app):    
    raised_data= data_request.segmentate_information(data_request.raised_incidences_month())
    closed_data= data_request.segmentate_information(data_request.closed_incidences_month())
    backlog_data= data_request.segmentate_information(data_request.backlog_incidences_month())
    incident_time = data_request.sla_achivement(data_request.incidences_time_priority()[0])
    incidents_type= data_request.incidences_type_month()
    # for x in range(1,len(data_frames)):

    dash_app = Dash( server= flask_app , name="Raised-1", url_base_pathname="/raised_incidents_1/", external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css'])
    dash_app.layout = html.Div(
        children=[
            dcc.Graph(
                id="Graph-2",
                figure=go.Figure(data=[go.Scatter(x=raised_data[0]['Months'], y=raised_data[0]['Incidences'])])
            )
        ]
    )
    
    dash_app = Dash( server= flask_app , name="Raised-2", url_base_pathname="/raised_incidents_2/", external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css'])
    dash_app.layout = html.Div(
        children=[
            dcc.Graph(
                id="Graph-3 ",
                figure=px.bar(
                    raised_data[1], 
                    x="Months", 
                    y="Incidences", 
                    barmode="group")
            )
        ]
    )

    dash_app = Dash( server= flask_app , name="Raised-3", url_base_pathname="/raised_incidents_3/", external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css'])
    dash_app.layout = html.Div(
        children=[
            dcc.Graph(
                figure={
                    'data': [
                        {'x': raised_data[2]['Months'], 'y': raised_data[2]['Incidences'], 'type': 'bar', 'name': 'Alto'},
                        {'x': raised_data[3]['Months'], 'y': raised_data[3]['Incidences'], 'type': 'bar', 'name': 'Medio'},
                        {'x': raised_data[4]['Months'], 'y': raised_data[4]['Incidences'], 'type': 'bar', 'name': 'Bajo'},
                    ],
                    'layout': {
                        'title': 'Dash Data Visualization'
                    }
                }
            )
        ]
    )

    dash_app = Dash( server= flask_app , name="closed-1", url_base_pathname="/closed_incidents_1/", external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css'])
    dash_app.layout = html.Div(
        children=[
            dcc.Graph(
                id="Graph-2",
                figure=go.Figure(data=[go.Scatter(x=closed_data[0]['Months'], y=closed_data[0]['Incidences'])])
            )
        ]
    )

    dash_app = Dash( server= flask_app , name="Backlog-2", url_base_pathname="/closed_incidents_2/", external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css'])
    dash_app.layout = html.Div(
        children=[
            dcc.Graph(
                figure={
                    'data': [
                        {'x': closed_data[1]['Months'], 'y': closed_data[1]['Incidences'], 'type': 'bar', 'name': 'Critical'},
                        {'x': closed_data[2]['Months'], 'y': closed_data[2]['Incidences'], 'type': 'bar', 'name': 'Alto'},
                        {'x': closed_data[3]['Months'], 'y': closed_data[3]['Incidences'], 'type': 'bar', 'name': 'Medio'},
                        {'x': closed_data[4]['Months'], 'y': closed_data[4]['Incidences'], 'type': 'bar', 'name': 'Bajo'},
                    ],
                    'layout': {
                        'title': 'Dash Data Visualization'
                    }
                }
            )
        ]
    )

    dash_app = Dash( server= flask_app , name="Backlog-1", url_base_pathname="/backlog_incidents_1/", external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css'])
    dash_app.layout = html.Div(
        children=[
            dcc.Graph(
                id='Graph1',
                figure=go.Figure(data=[go.Scatter(x=backlog_data[0]['Months'], y=backlog_data[0]['Incidences'])])
                )
        ]
    )

    dash_app = Dash( server= flask_app , name="Backlog-2", url_base_pathname="/backlog_incidents_2/", external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css'])
    dash_app.layout = html.Div(
        children=[
            dcc.Graph(
                figure={
                    'data': [
                        {'x': backlog_data[1]['Months'], 'y': backlog_data[1]['Incidences'], 'type': 'bar', 'name': 'Critical'},
                        {'x': backlog_data[2]['Months'], 'y': backlog_data[2]['Incidences'], 'type': 'bar', 'name': 'Alto'},
                        {'x': backlog_data[3]['Months'], 'y': backlog_data[3]['Incidences'], 'type': 'bar', 'name': 'Medio'},
                        {'x': backlog_data[4]['Months'], 'y': backlog_data[4]['Incidences'], 'type': 'bar', 'name': 'Bajo'},
                    ],
                    'layout': {
                        'title': 'Dash Data Visualization'
                    }
                }
            )
        ]
    )

    dash_app = Dash( server= flask_app , name="Type Incidents-1", url_base_pathname="/type_incidents/", external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css'])
    dash_app.layout = html.Div(
        children=[
            dash_table.DataTable(
                id='datatable-interactivity',
                columns=[
                    {"name": i, "id": i, "deletable": True, "selectable": True} for i in incidents_type.columns
                ],
                data=incidents_type.to_dict('records'),
                editable=False,
                sort_action="native",
                sort_mode="multi",
                row_deletable=False,
                fixed_columns=True,
                selected_columns=[],
                selected_rows=[],
                page_current= 0,
                page_size= 15
            )
        ]
    )

    dash_app = Dash( server= flask_app , name="", url_base_pathname="/time_incidents_1/", external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css'])
    dash_app.layout = html.Div(
        children=[
            
            
            
        ]
    )

    return dash_app
