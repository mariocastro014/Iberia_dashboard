from flask import Flask

app = Flask(__name__)


from app import public, errors, private, dash_app

dash_app.create_dash_application(app)