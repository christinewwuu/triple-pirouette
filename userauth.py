import os
from flask import Flask, request, render_template, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector

app = Flask(__name__)
app.secret_key = os.environ.get('fb_key')

# user sign up/registration
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # validate registration data
        email = request.form.get("email")
        password = request.form.get("password")

        if not (email and password):
            return render_template("register.html", message="All fields are required.")

        # hash password
        hashed_pw = generate_password_hash(password)

        # add email + hashed password to user db
        mydb = mysql.connector.connect(
            host="localhost",
            user=os.environ.get("db_user"),
            password=os.environ.get("db_pass"),
            database="grocerydb"
        )
        mycursor = mydb.cursor()
        mycursor.execute(f"INSERT INTO users (email, password) VALUES ({email}, {hashed_pw})")

        return redirect("/login")

    return render_template("register.html")

# existing user log in
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # look up email in user db
        mydb = mysql.connector.connect(
            host="localhost",
            user=os.environ.get("db_user"),
            password=os.environ.get("db_pass"),
            database="grocerydb"
        )
        mycursor = mydb.cursor()
        mycursor.execute(f"SELECT email, password FROM users WHERE email = {email}")
        userdata = mycursor.fetchall()

        # check if email, password valid
        if userdata:
            if check_password_hash(userdata[0][1], password):
                session["user_id"] = email
                return redirect("/home")
            else:
                return render_template(login.html, mesage="Invalid password.")

        else:
            return render_template(login.html, mesage="No account with that email exists.")

    return render_template("login.html")

# user logout
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

