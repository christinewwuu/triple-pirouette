import os, mysql.connector
from dotenv import load_dotenv, dotenv_values
from flask import Flask, request, render_template, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash

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

# request data from shelf life API


