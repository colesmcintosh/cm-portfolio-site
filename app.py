from flask import Flask, render_template
from datetime import datetime
import calendar

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    today = datetime.today()
    month = calendar.month_name[today.month]
    day = today.day
    if day == 1:
        month = f"<div class='day'>I hope you have a great <b id='day-name'>{month}</b> ahead!</div>"
    else:
        month = f"<div class='day'>I hope you're having a great <b id='day-name'>{month}</b> so far!</div>"

    return render_template('index.html', month=month)

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/edu')
def edu():
    return render_template('edu.html')

@app.route('/certs')
def certs():
    return render_template('certs.html')