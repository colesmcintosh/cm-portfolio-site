from flask import Flask, render_template
from datetime import datetime
import calendar

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    today = datetime.today()
    days = calendar.day_name[calendar.weekday(year=today.year, month=today.month, day=today.day)]
    return render_template('index.html', days=days)

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