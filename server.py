from flask import Flask, render_template, request
from grocery import get_value
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/grocery')
def get_grocery():
    # city = request.args.get('city')
    # grocery_data = get_current_grocery(city)
    return render_template(
        "grocery.html",
        title="New York",
        status="Cloudy",
        temp="15",
        feels_like="12"
    )

if __name__ == "__main__":
    # serve(app, host="0.0.0.0", port=8000)
    app.run(debug=True, host="0.0.0.0", port=8000)