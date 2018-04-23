import datetime
from myapp import db

class Users(db.Model):
    user_name = db.Column(db.VARCHAR(30), nullable=False)
    user_password = db.Column(db.VARCHAR(200))
    user_empcode = db.Column(db.NVARCHAR(15), nullable=False, primary_key=True)

class Projects(db.Model):
    __tablename_ = "Projects"
    proj_id = db.Column(db.Integer(), primary_key=True, autoincrement=True, nullable=False)
    proj_manager = db.Column(db.NVARCHAR(20), db.ForeignKey("project_managers.manager_code"), nullable=False)
    proj_budget = db.Column(db.Numeric, nullable=False)
    proj_name = db.Column(db.NVARCHAR(40), nullable=False)
    proj_approval = db.Column(db.Boolean, nullable=False)
    proj_deadline = db.Column(db.DateTime)
    proj_hours = db.Column(db.Numeric)
    proj_client = db.Column(db.NVARCHAR(20), db.ForeignKey("clients.client_id"))
    proj_description = db.Column(db.NVARCHAR(1000))
    proj_type = db.Column(db.Integer, db.ForeignKey("project_types.type_id"))
    proj_currency = db.Column(db.Integer, db.ForeignKey("currency.curr_id"))

class Clients(db.Model):
    __tablename_ = "clients"
    client_id = db.Column(db.NVARCHAR(20), primary_key=True)
    client_name = db.Column(db.NVARCHAR(40), nullable=False)
    project = db.relationship("Projects", backref="client", lazy="dynamic")

class Currency(db.Model):
    __tablename_ = "currency"
    curr_name = db.Column(db.NVARCHAR(10), nullable=False)
    curr_id = db.Column(db.Integer, primary_key=True)
    project = db.relationship(Projects, backref="currency", lazy="dynamic")

class ProjectTypes(db.Model):
    __tablename_ = "project_types"
    type_name = db.Column(db.VARCHAR(30), nullable=False)
    type_id = db.Column(db.Integer, primary_key=True)
    project = db.relationship("Projects", backref="type", lazy="dynamic")

class ProjectManagers(db.Model):
    __tablename_ = "project_managers"
    manager_name = db.Column(db.VARCHAR(30), nullable=False)
    manager_code = db.Column(db.NVARCHAR(20), primary_key=True)
    project = db.relationship("Projects", backref="manager", lazy="dynamic")

class ProjectIssues(db.Model):
    __tablename_ = "project_issues"
    issue_proj =  db.Column(db.Integer)
    issue_id = db.Column(db.Integer, nullable=False, primary_key=True)
    issue_title = db.Column(db.VARCHAR(40), nullable=False)
    issue_descr =  db.Column(db.VARCHAR(10000), nullable=True)
    issue_date = db.Column(db.Date, nullable=False, default=datetime.datetime.utcnow)

class IssueResponse(db.Model):
    __tablename_ = "IssueResponse"
    issue_id = db.Column(db.Integer, nullable=False)
    response_id = db.Column(db.Integer, nullable=False, primary_key=True)
    issue_responder = db.Column(db.NVARCHAR(15), nullable=False)
    issue_response =  db.Column(db.VARCHAR(10000), nullable=True)
    response_date = db.Column(db.Date, default=datetime.datetime.utcnow, nullable=False)



