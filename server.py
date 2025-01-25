from flask import Flask, render_template, request
from grocery import get_value

app = Flask(__name__)

@app.route('/')
@app.route('/index')

def index():
    return "Hello World"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)