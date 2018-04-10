TEMPLATES_AUTO_RELOAD = True
SECRET_KEY = '£$%^HJGE97655@~?><XGHWEDI7974'
DEBUG = False

##mails
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = 'rmachaz@gmail.com'
MAIL_DEFAULT_SENDER = 'rmachaz@gmail.com'
MAIL_PASSWORD = '684192684192'

## databases

SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:123456@35.198.11.162/Projects?unix_socket=/cloudsql/primeval-melody-169005:southamerica-east1:project-module'
SQLALCHEMY_TRACK_MODIFICATIONS = False
# SQLALCHEMY_BINDS = {
#     'users':        'mysqldb://localhost/users',
#     'appmeta':      'sqlite:////path/to/appmeta.db'
# }

##files storage
UPLOADED_FILES_DEST = "projectfilesupload/"
