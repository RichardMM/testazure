
from os import walk
from pathlib import Path
from functools import wraps
from flask import render_template, request,session,Blueprint, redirect, url_for, current_app, send_file
from myapp import mail,models, db
from flask_mail import Message
from sqlalchemy.exc import OperationalError
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField
from wtforms.validators import Email, InputRequired
from flask_login import login_required, login_manager

projects_mod = Blueprint('projects', import_name=__name__, template_folder='templates')

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])

def check_db_connection(func):
    def wrapper():
        try:
            func()
        except OperationalError:
            return "We could not connect to the database"
    return wrapper  

def check_if_logged_in():
    def decorator(func):
        @wraps(func)
        def login_wrapper(*args, **kwargs):
            if session.get("logged_in", False):
                return func(*args, **kwargs)
            else:
                return redirect(url_for("projects.login"))
        return login_wrapper
    return decorator


@projects_mod.route('/login/', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if request.method=="GET":
        return render_template("projects/login.htm", form=login_form)
    elif request.method=="POST":
        if login_form.validate_on_submit():
            session["username"] = login_form.email.data
            session["password"] = login_form.password.data
            user = models.Users.query.filter_by(user_email=session["username"], user_password=session["password"] ).first()

            if session["password"] is None or session["username"] is None or user is None: 
                session["logged_in"] = False
                return "Unauthorised"
            else:
                session["logged_in"] = True
                session["approval_rights"] = user.user_approver_rights
                session["empcode"] = user.user_empcode
                return redirect(url_for("projects.projects"))
        else:
            return render_template("projects/login.htm", form=login_form)

@projects_mod.route("/", methods=["GET", 'POST'])
def home():
    return render_template('projects/home.html')

@projects_mod.route("/newproject/<int:id>", methods=["GET"])
@projects_mod.route("/newproject", methods=["GET"])
@check_if_logged_in()
def project_details(id=None):
    # query the tables needed for both new and old project
    currencies = models.Currency.query.all()
    proj_types = models.ProjectTypes.query.all()
    managers = models.ProjectManagers.query.all()
    clients = models.Clients.query.all()

    if id is None:
        return render_template('projects/newproject.html', curr=currencies, clients=clients,
                                projects=proj_types, managers=managers,
                                id="None", project_detail=None,  can_approve=False)
    else:
        # Query data needed for an existing project
        project = models.Projects.query.filter_by(proj_id=id).first()
        disbursements = models.ProjectDisbursements.query.filter_by(disb_proj=id).all()
        tasks = models.ProjectTasks.query.filter_by(task_proj=id).all()
        usernames = models.Users.query.with_entities(models.Users.user_empcode, models.Users.user_name).all()

        issues_base = models.ProjectIssues.query.filter_by(issue_proj=id)
        issues = issues_base.all()
        
        response_count = models.IssueResponse.query.filter(models.IssueResponse.issue_id.in_\
                         (issues_base.with_entities(models.ProjectIssues.issue_id).all()))
        for row in response_count:
            print(row)

        session["project_name"] = project.proj_name
        session["project_id"] = project.proj_id

        #check if project has been approved to prevent editing
        readonly=""
        if project.proj_approval:
            readonly="disabled"

        #create directory if doesn't exist
        path = current_app.config["UPLOADED_FILES_DEST"] + session["project_name"]+'/'
        Path(path).mkdir(exist_ok=True, parents=True)
        directory_generator = walk(path)
        return render_template('projects/newproject.html', curr=currencies, 
                                projects=proj_types, managers=managers, project_detail=project,
                                id=session["project_id"], clients=clients, issues=issues,
                                can_approve=, files=directory_generator,
                                tasks=tasks, disb=disbursements, users=usernames, readonly=readonly)


@projects_mod.route("/projects", methods=["GET", 'POST'])
@check_if_logged_in()
def projects():
    projects = models.Projects.query.all()
    return render_template('projects/projects.html', projects=projects)

@projects_mod.route("/pipeline", methods=["GET", 'POST'])
@check_if_logged_in()
def calendar():
    return render_template('projects/calendar.html')
    
@projects_mod.route("/mail")
@check_if_logged_in()
def mailer():
   msg = Message('Hello', recipients = ['richard.macharia@strathmore.edu'])
   msg.body = "This is the email body"
   mail.send(msg)
   return "Sent"

@projects_mod.route("/download/<filename>")
@check_if_logged_in()
def send_files(filename):
    file_directory=current_app.config["UPLOADED_FILES_DEST"] + session["project_name"] + "/" + "filename"
    return send_file(filename_or_fp=file_directory, attachment_filename=filename)
