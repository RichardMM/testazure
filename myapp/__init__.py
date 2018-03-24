from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config.from_pyfile(filename='config.py')
mail = Mail(app=app)

from myapp.projects.views import projects_mod
from myapp.calendar_api.views import calendar_mod

app.register_blueprint(projects_mod)
app.register_blueprint(calendar_mod, url_prefix='calendar')