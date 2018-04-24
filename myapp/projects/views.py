
from pathlib import Path
from flask import render_template, request,session
from flask import Blueprint
from myapp import mail,models, db
from flask_mail import Message
from sqlalchemy.exc import OperationalError

projects_mod = Blueprint('projects', import_name=__name__, template_folder='templates')

def check_db_connection(func):
    def wrapper():
        try:
            func()
        except OperationalError:
            return "We could not connect to the database"
    return wrapper  

@projects_mod.route("/", methods=["GET", 'POST'])
def home():
    return render_template('projects/home.html')

@projects_mod.route("/newproject/<int:id>", methods=["GET"])
@projects_mod.route("/newproject", methods=["GET"])
def project_details(id=None):
    currencies = models.Currency.query.all()
    proj_types = models.ProjectTypes.query.all()
    managers = models.ProjectManagers.query.all()
    if id is None:
        return render_template('projects/newproject.html', curr=currencies, 
                                projects=proj_types, managers=managers, id="None", project_detail=None)
    else:
        project = models.Projects.query.filter_by(proj_id=id).first()
        session["project_name"] = project.proj_name
        session["project_id"] = project.proj_id
        #create directory if doesn't exist
        Path('./projectfilesupload/' + session["project_name"]+'/').mkdir(exist_ok=True, parents=True)
        return render_template('projects/newproject.html', curr=currencies, 
                                projects=proj_types, managers=managers, project_detail=project, id=id)


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
