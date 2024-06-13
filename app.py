pip install flask

calculator/
├── static/
│   └── styles.css
├── templates/
│   └── index.html
├── app.py

from flask import Flask, render_template, request, jsonify
from datetime import datetime
import math

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form['expression']
    try:
        result = eval(expression, {"__builtins__": None}, {"Math": math})
    except:
        result = "Error"
    return jsonify(result=result)

@app.route('/calculate_age', methods=['POST'])
def calculate_age():
    birthdate_str = request.form['birthdate']
    try:
        birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d')
        today = datetime.today()
        age = today.year - birthdate.year
        month_diff = today.month - birthdate.month
        if month_diff < 0 or (month_diff == 0 and today.day < birthdate.day):
            age -= 1
        days_diff = (today - birthdate).days
        result = f"Your age is: {age} years, {days_diff // 30} months, and {days_diff % 30} days."
    except:
        result = "Invalid date. Please enter a valid birthdate."
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
