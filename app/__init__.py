from flask import Flask

app = Flask(__name__)

app.config["SECRET_KEY"] = 'jU99sOOSLddk7'

PASSWORD ="7dpi7MxFwuyc2Kwk"
PUBLIC_IP_ADDRESS ="34.77.137.237"
DBNAME ="iberia-database"
PORT="3306"
PROJECT_ID ="iberia-project-344914"
INSTANCE_NAME ="iberia-project"

# app.config["SQLALCHEMY_DATABASE_URI"]= f"mysql + mysqldb://root:{PASSWORD}@{PUBLIC_IP_ADDRESS}/{DBNAME}?unix_socket =/cloudsql/{PROJECT_ID}:{INSTANCE_NAME}"
# configuration
mysql_path = f"mysql+pymysql://root:{PASSWORD}@{PUBLIC_IP_ADDRESS}:{PORT}/{DBNAME}"
oracle_path = 'https://g10e916cba8455f-database1.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/'

from app import public, errors, private, dash_app

dash_app.create_dash_application(app)