
from flask import render_template

from flask import Blueprint
from myapp import mail
from flask_mail import Message


projects_mod = Blueprint('projects', import_name=__name__, template_folder='templates')

@projects_mod.route("/", methods=["GET", 'POST'])
def home():
    return render_template('projects/home.html')

@projects_mod.route("/newproject", methods=["GET", 'POST'])
def project_details():
    return render_template('projects/newproject.html')

@projects_mod.route("/projects", methods=["GET", 'POST'])
def projects():
    return render_template('projects/projects.html')

@projects_mod.route("/pipeline", methods=["GET", 'POST'])
def calendar():
    return render_template('projects/calendar.html')

@projects_mod.route("/mail")
def mailer():
   msg = Message('Hello', recipients = ['richard.macharia@strathmore.edu'])
   msg.body = "This is the email body"
   mail.send(msg)
   return "Sent"