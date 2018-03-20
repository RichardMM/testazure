from flask import Flask

app = Flask(__name__)
app.secret_key = 'jygdtude6577?>:@897dejk*&qef^&%'

from myapp.projects.views import projects_mod
from myapp.calendar_api.views import calendar_mod

app.register_blueprint(projects_mod)
app.register_blueprint(calendar_mod, url_prefix='calendar')