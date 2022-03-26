import requests
import pandas as pd
import numpy as np
from app import oracle_path, mysql_path
from sqlalchemy import create_engine

oracle_path = 'https://g10e916cba8455f-database1.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/'
engine = create_engine(mysql_path)

def register_user(username, email, hashed_password):
    insert_user = f"""
    INSERT INTO USERS(username, email, password)
    VALUES ('{username}', '{email}', '{hashed_password}')
    """
    with engine.connect() as connection:
        connection.execute(insert_user)

def request_user(username_email):
    login_query = f"""    
        SELECT password
        FROM USERS
        WHERE username='{username_email}' OR email='{username_email}'
        """
    with engine.connect() as connection:  
        user = connection.execute(login_query).fetchone()
    return user

def raised_incidences_month():
    url = oracle_path + 'kpi1/incvol'
    data_oracle = requests.get(url).json()['items']
    return data_oracle

def closed_incidences_month():
    url = oracle_path + 'kpi2/incclosed'
    data_oracle = requests.get(url).json()['items']
    return data_oracle

def backlog_incidences_month():
    url = oracle_path + 'kpi3/incbackl'
    data_oracle = requests.get(url).json()['items']
    return data_oracle

def segmentate_information(data_oracle):
    data_oracle = pd.DataFrame(data_oracle).rename(columns={'month':'Months','priority':'Priority','incidences_number':'Incidences'})
    total = data_oracle.groupby(['Months'])['Incidences'].sum().reset_index()
    critical = data_oracle[data_oracle['Priority']=='Crítica']
    alta = data_oracle[data_oracle['Priority']=='Alta']
    media = data_oracle[data_oracle['Priority']=='Media']
    baja = data_oracle[data_oracle['Priority']=='Baja']
    return total, critical, alta, media, baja

def incidences_type_month():
    url = oracle_path + 'kpi4/inctype'
    data_oracle = requests.get(url).json()['items']
    data_oracle = pd.DataFrame(data_oracle).rename(columns={'month':'Month','incident_type':'Incident Type','cases_raised':'Total Cases','cases_pending':'Pending', 'cases_assigned':'Assigned', 'cases_inprogress':'In Progress', 'cases_closed':'Closed', 'cases_resolved':'Resolved'})
    return data_oracle

def incidences_time_priority():
    url = oracle_path + 'kpi5/sla'
    data_oracle = requests.get(url).json()['items']
    data_oracle = pd.DataFrame(data_oracle)
    data_oracle[['resolution_date','created_date']] = data_oracle[['resolution_date','created_date']].apply(pd.to_datetime)
    data_oracle['time_diff'] = data_oracle['resolution_date'] - data_oracle['created_date']
    total_average_time = data_oracle.groupby(['priority'])['time_diff'].mean().reset_index()
    return data_oracle, total_average_time

def sla_achivement(data):
    incidences_time_priority = data
    low_sla= pd.Timedelta('15 days')
    medium_sla = pd.Timedelta('5 days')
    high_sla = pd.Timedelta('8 hours')
    critical_sla = pd.Timedelta('4 hours')
    
    conditions = [
        (incidences_time_priority['priority'] == 'Baja'),
        (incidences_time_priority['priority'] == 'Media'),
        (incidences_time_priority['priority'] == 'Alta'),
        (incidences_time_priority['priority'] == 'Crítica')
        ]

    # create a list of the values we want to assign for each condition
    values = [low_sla, medium_sla, high_sla, critical_sla]

    # create a new column and use np.select to assign values to it using our lists as arguments
    incidences_time_priority['SLA'] = np.select(conditions, values)
    
    incidences_time_priority['Reached_SLA'] = np.where((incidences_time_priority['time_diff'] < incidences_time_priority['SLA'] ), 1, 0)
    incidences_time_priority['Failed_SLA'] = np.where((incidences_time_priority['time_diff'] > incidences_time_priority['SLA'] ), 1, 0)
    total = incidences_time_priority.groupby(['priority'])[['Reached_SLA', 'Failed_SLA']].sum().reset_index()
    return total