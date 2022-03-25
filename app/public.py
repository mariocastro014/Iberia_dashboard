from app import app, data_requets, private
from flask import render_template, request, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET","POST"])
def handle_login():
    if request.method == 'POST':
        username_email = request.form['username']
        password = request.form['password']
        
        user = data_requets.request_user(username_email)

        if user and check_password_hash(user[0], password):
            session["username"] = username_email
            return redirect(private.url_for("dashboard_raised"))
        
        else:
            
            return render_template("errors/403.html"), 403
    else:
            
        return render_template("errors/403.html"), 403


@app.route("/signup")
def register():
    return render_template("signup.html")


@app.route("/signup", methods=["POST"])
def handle_register():
    username=request.form["username"]
    email=request.form["email"]
    password=request.form["password"]

    hashed_password = generate_password_hash(password)

    data_requets.register_user(username, email, hashed_password)

    return redirect(url_for("index"))