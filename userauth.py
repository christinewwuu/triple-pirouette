import os
from flask import Flask, request, render_template, redirect, session
from werkzeug.security import generate_password_hash
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