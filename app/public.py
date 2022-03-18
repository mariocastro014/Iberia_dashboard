from app import app, data_requets, private
from flask import render_template, request, redirect, url_for


app.config["SECRET_KEY"] = 'jU99sOOSLddk7'



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def handle_login():
    return redirect(url_for("dashboard"))

@app.route("/dashboard")
def dashboard1():   
    return render_template("dashboard.html")
        