from flask import session,redirect, url_for
from app import data_requets
from dash import dcc, html, Dash
import plotly.express as px


def create_dash_application(flask_app):
    # if "username" not in session:
    #         return redirect(url_for(errors.not_autorized()))
    
    # else:  + str(x) +"
    data_oracle = data_requets.raised_incidences_month()
    total = data_oracle.groupby(['Months'])['Incidences'].sum().reset_index()
    critical = data_oracle[data_oracle['Priority']=='Crítica']
    alta = data_oracle[data_oracle['Priority']=='Alta']
    media = data_oracle[data_oracle['Priority']=='Media']
    baja = data_oracle[data_oracle['Priority']=='Baja']

    data_frame_bars = [total,critical, alta, media, baja]
    
    for x in range(0, len(data_frame_bars)-1):
        print(x)
        dash_app = Dash( server= flask_app , name="Dashboard", url_base_pathname="/total_incidents_"+ str(x) +"/")
        dash_app.layout = html.Div(
            children=[
                dcc.Graph(
                    id="Graph-1",
                    figure=px.bar(data_frame_bars[x], x="Months", y="Incidences", barmode="group")
                )
            ]
        )

    return dash_app