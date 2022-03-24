import requests, json
import pandas as pd
from app import oracle_path, mysql_path
from sqlalchemy import create_engine

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
    url = oracle_path + 'kpi1/incvol/'
    data_oracle = requests.get(url).json()['items']
    data_oracle = pd.DataFrame(data_oracle).rename(columns={'month':'Months','priority':'Priority','incidences_number':'Incidences'})  
    return data_oracle

def closed_incidences_month():
    url = oracle_path + 'kpi1/incvol/'
    data_oracle = requests.get(url).json()['items']
    data_oracle = pd.DataFrame(data_oracle).rename(columns={'month':'Months','priority':'Priority','incidences_number':'Incidences'})  
    return data_oracle

def backlog_incidences_month():
    url = oracle_path + 'kpi1/incvol/'
    data_oracle = requests.get(url).json()['items']
    data_oracle = pd.DataFrame(data_oracle).rename(columns={'month':'Months','priority':'Priority','incidences_number':'Incidences'})  
    return data_oracle


def kpi1():
    kpi1_query = f"""    
        
        """
    with engine.connect() as connection:  
        kpi_1 = connection.execute(kpi1_query).fetchall()
    return kpi_1