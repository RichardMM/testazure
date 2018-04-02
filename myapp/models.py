from myapp import db

class Users(db.Model):
    user_name = db.Column(db.VARCHAR(30), nullable=False)
    user_password = db.Column(db.VARCHAR(200))
    user_empcode = db.Column(db.NVARCHAR(15), nullable=False, primary_key=True)

class Projects(db.Model):
    proj_id = db.Column(db.Integer(), primary_key=True, autoincrement=True, nullable=False)
    proj_manager = db.Column(db.NVARCHAR(15), nullable=False)
    proj_budget = db.Column(db.Numeric, nullable=False)
    proj_name = db.Column(db.NVARCHAR(10), nullable=False)
    proj_approval = db.Column(db.Boolean, nullable=False)
    proj_deadline = db.Column(db.DateTime)
    proj_hours = db.Column(db.Numeric)
    proj_description = db.Column(db.NVARCHAR(200))
    proj_type = db.Column(db.Integer)
    proj_currency = db.Column(db.Integer)

class Currency(db.Model):
    curr_name = db.Column(db.NVARCHAR(10), nullable=False)
    curr_id = db.Column(db.Integer, primary_key=True)

class ProjectTypes(db.Model):
    type_name = db.Column(db.NVARCHAR(5), nullable=False)
    type_id = db.Column(db.Integer, primary_key=True)

class ProjectManagers(db.Model):
    manager_name = db.Column(db.VARCHAR(30), nullable=False)
    manager_code = db.Column(db.NVARCHAR(15), nullable=False, primary_key=True)


