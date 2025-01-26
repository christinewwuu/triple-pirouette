import os, mysql.connector
from dotenv import load_dotenv, dotenv_values
from flask import Flask, request, render_template, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash

# load environment vars from .env file
load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

HOST=os.getenv("MYSQL_HOST")
USER=os.getenv("MYSQL_USER")
PASSWORD=os.getenv("MYSQL_PASSWORD")
DATABASE=os.getenv("MYSQL_DATABASE")

def db_connection():
    db = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )
    return db


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
        try:
            reg_query = "INSERT INTO users (email, password) VALUES (%s, %s)"
            mycursor.execute(reg_query, (email, hashed_pw))
            mydb.commit()

        except mysql.connector.errors.IntegrityError as err:
            # Handle integrity errors like duplicate key
            if '1062' in str(err):  # Duplicate entry error code
                return render_template("register.html", message="Email already exists. Please try another one.")
            else:
                return render_template("register.html", message=f"An error occurred: {err}")

        finally:
            mycursor.close()
            mydb.close()

        return redirect("/login")

    return render_template("register.html")

# existing user log in
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # look up email in user db
        mydb = db_connection()
        mycursor = mydb.cursor()
        login_query = "SELECT email, password FROM users WHERE email = %s"
        mycursor.execute(login_query, (email,))
        userdata = mycursor.fetchall()
        mydb.close()

        # check if email, password valid
        if userdata:
            if check_password_hash(userdata[0][1], password):
                session["user_id"] = email
                return redirect("/home")
            else:
                return render_template("login.html", message="Invalid password.")

        else:
            return render_template("login.html", message="No account with that email exists.")

    return render_template("login.html")

# user logout
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

