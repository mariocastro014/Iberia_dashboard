from flask import render_template, request, session, redirect, url_for
from app import app, public, data_requets
from werkzeug.security import generate_password_hash, check_password_hash

@app.route("/dashboard")
def dashboard():
        return render_template("dashboard.html")