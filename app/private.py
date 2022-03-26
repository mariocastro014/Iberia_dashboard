from flask import render_template, session, redirect, url_for
from app import app, data_request

@app.route("/dashboard/raised")
def dashboard_raised():
        if "username" not in session:
                return render_template("errors/403.html"), 403 
        else:
                return render_template("dashboard/raised.html")

@app.route("/dashboard/backlog")
def dashboard_backlog():
        if "username" not in session:
                return render_template("errors/403.html"), 403 
        else:
                return render_template("dashboard/backlog.html")

@app.route("/dashboard/closed")
def dashboard_closed():
        if "username" not in session:
                return render_template("errors/403.html"), 403 
        else:
                return render_template("dashboard/closed.html")

@app.route("/dashboard/sla")
def dashboard_sla():
        if "username" not in session:
                return render_template("errors/403.html"), 403 
        else:
                average_time=data_request.incidences_time_priority()[1].values.tolist()
                average_time
                return render_template("dashboard/sla.html", average_time=average_time) 

@app.route("/dashboard/incident-types")
def dashboard_incidents():
        if "username" not in session:
                return render_template("errors/403.html"), 403 
        else:
                return render_template("dashboard/incident-types.html") 

@app.route("/logout")
def logout():
    session.pop("username")
    return redirect(url_for("index"))