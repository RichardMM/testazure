'''
Module to start and run the app
'''
from os import environ
from myapp import app
if __name__ == '__main__':
    # db.create_all()
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', 'localhost'))
    except ValueError:
        PORT = 8080
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(HOST, PORT, debug=True)

    