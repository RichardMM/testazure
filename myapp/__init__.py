


from flask import Flask
from flask_mail import Mail
from logging import FileHandler, WARNING
from flask_sqlalchemy import SQLAlchemy


handler = FileHandler("error.txt")
handler.setLevel(level=WARNING)
app = Flask(__name__)

#set logging details

app.logger.addHandler(handler)

app.config.from_pyfile(filename='config.py')

mail = Mail(app=app)
db = SQLAlchemy(app=app)

from myapp.projects.views import projects_mod
from myapp.calendar_api.views import calendar_mod
from myapp import models
db.create_all()

app.register_blueprint(projects_mod)
app.register_blueprint(calendar_mod, url_prefix='calendar')