import requests
import pandas as pd
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
    data_oracle = pd.DataFrame(data_oracle).rename(columns={'month':'Months','priority':'Priority','incidences_number':'Incidences'})  
    return data_oracle



def closed_incidences_month():
    url = oracle_path + 'kpi2/incclosed'
    data_oracle = requests.get(url).json()['items']
    data_oracle = pd.DataFrame(data_oracle).rename(columns={'month':'Months','priority':'Priority','incidences_number':'Incidences'})  
    print(data_oracle)
    return data_oracle


def backlog_incidences_month():
    url = oracle_path + 'kpi3/incbackl'
    data_oracle = requests.get(url).json()['items']
    data_oracle = pd.DataFrame(data_oracle).rename(columns={'month':'Months','priority':'Priority','incidences_number':'Incidences'})  
    print(data_oracle)
    return data_oracle

def incidences_type_month():
    url = oracle_path + 'kpi4/inctype'
    data_oracle = requests.get(url).json()['items']
    data_oracle = pd.DataFrame(data_oracle)#.rename(columns={'incident_type':'Type Incident','month':'Months','priority':'Priority','incidences_number':'Incidences'})  
    print(data_oracle)
    return data_oracle

