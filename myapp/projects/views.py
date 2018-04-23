
from flask import render_template, request,session
from flask import Blueprint
from myapp import mail,models, db
from flask_mail import Message
projects_mod = Blueprint('projects', import_name=__name__, template_folder='templates')


@projects_mod.route("/", methods=["GET", 'POST'])
def home():
    return render_template('projects/home.html')

@projects_mod.route("/newproject/<int:id>", methods=["GET"])
@projects_mod.route("/newproject", methods=["GET"])
def project_details(id=None):
    if id is None:
        currencies = models.Currency.query.all()
        proj_types = models.ProjectTypes.query.all()
        managers = models.ProjectManagers.query.all()
        return render_template('projects/newproject.html', curr=currencies, 
                                projects=proj_types, managers=managers)
    else:
        return id


@projects_mod.route("/projects", methods=["GET", 'POST'])
def projects():
    projects = models.Projects.query.all()
    return render_template('projects/projects.html', projects=projects)

@projects_mod.route("/pipeline", methods=["GET", 'POST'])
def calendar():
    return render_template('projects/calendar.html')

@projects_mod.route("/mail")
def mailer():
   msg = Message('Hello', recipients = ['richard.macharia@strathmore.edu'])
   msg.body = "This is the email body"
   mail.send(msg)
   return "Sent"

@projects_mod.route("/management")
def approve():
    session["project_name"] = "Machakos Drill"
    session["project_id"] = 2
    return "Sent"