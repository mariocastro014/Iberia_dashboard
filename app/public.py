from ensurepip import bootstrap
from app import app
from flask import render_template
from flask_bootstrap import Bootstrap


app.config["SECRET_KEY"] = 'jU99sOOSLddk7'
Bootstrap(app)

app.config["SECRET_KEY"] = "this is not secret, remember, change it!"

@app.route("/")
def index():
    return render_template("index.html")


    