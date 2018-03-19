from myapp import app
from flask import render_template

@app.route("/", methods=["GET", 'POST'])
def home():
    return render_template('home.html')

@app.route("/newproject", methods=["GET", 'POST'])
def project_details():
    return render_template('newproject.html')

@app.route("/projects", methods=["GET", 'POST'])
def projects():
    return render_template('projects.html')

@app.route("/pipeline", methods=["GET", 'POST'])
def calendar():
    return render_template('calendar.html')