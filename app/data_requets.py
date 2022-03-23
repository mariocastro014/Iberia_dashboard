from flask import request, jsonify, make_response
import requests, json
import pandas as pd
from app import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

adb_path = 'https://g10e916cba8455f-database1.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/'

PASSWORD ="7dpi7MxFwuyc2Kwk"
PUBLIC_IP_ADDRESS ="34.77.137.237"
DBNAME ="iberia-database"
PORT="3306"
PROJECT_ID ="iberia-project-344914"
INSTANCE_NAME ="iberia-project"

# configuration
app.config["SECRET_KEY"] = 'jU99sOOSLddk7'
app.config["SQLALCHEMY_DATABASE_URI"]= f"mysql + mysqldb://root:{PASSWORD}@{PUBLIC_IP_ADDRESS}/{DBNAME}?unix_socket =/cloudsql/{PROJECT_ID}:{INSTANCE_NAME}"
db_url = f"mysql+pymysql://root:{PASSWORD}@{PUBLIC_IP_ADDRESS}:{PORT}/{DBNAME}"

engine = create_engine(db_url)

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
    url = adb_path + 'kpi1/incvol/'
    data_oracle = requests.get(url).json()['items']
    data_oracle = pd.DataFrame(data_oracle).rename(columns={'month':'Months','priority':'Priority','incidences_number':'Incidences'})  
    return data_oracle

def closed_incidences_month():
    url = adb_path + 'kpi1/incvol/'
    data_oracle = requests.get(url).json()['items']
    data_oracle = pd.DataFrame(data_oracle).rename(columns={'month':'Months','priority':'Priority','incidences_number':'Incidences'})  
    return data_oracle

def kpi1():
    kpi1_query = f"""    
        
        """
    with engine.connect() as connection:  
        kpi_1 = connection.execute(kpi1_query).fetchall()
    return kpi_1