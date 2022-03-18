import requests

def login(username,password):
    url=''

    users=[]
    passwords = []
    if username in users and password in passwords:
        return True
    return False

def kpi_1():
    url = ''
    data_json = requests