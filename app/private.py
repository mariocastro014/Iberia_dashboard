from flask import render_template, session, redirect, url_for
from app import app

@app.route("/dashboard/raised.html")
def dashboard_raised():
        if "username" not in session:
                return render_template("errors/403.html"), 403 
        else:
                return render_template("dashboard/raised.html")

@app.route("/dashboard/backlog.html")
def dashboard_backlog():
        if "username" not in session:
                return render_template("errors/403.html"), 403 
        else:
                return render_template("dashboard/backlog.html")

@app.route("/logout")
def logout():
    session.pop("username")
    return redirect(url_for("index"))