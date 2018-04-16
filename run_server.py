'''
Module to start and run the app
'''
import logging
import traceback
try:
    from os import environ
    from myapp import app, manager
    if __name__ == '__main__':
        # db.create_all()
        
        HOST = environ.get('SERVER_HOST', 'localhost')
        try:
            PORT = int(environ.get('SERVER_PORT', 'localhost'))
        except ValueError:
            PORT = 8080
        app.jinja_env.auto_reload = True
        #app.run(HOST, PORT)
        manager.run()
except (ModuleNotFoundError, ImportError, ImportWarning) as ex:
    # logging.basicConfig(filename="myapp.log", level=logging.WARNING)
    # logging.exception(ex)
    # log import error in new app
    from flask import Flask
    app = Flask(__name__)
    @app.route('/', methods=['GET'])
    def errohandler():
        var = traceback.format_exc()
        return var
    if __name__ == '__main__':
        # db.create_all()
        HOST = environ.get('SERVER_HOST', 'localhost')
        try:
            PORT = int(environ.get('SERVER_PORT', 'localhost'))
        except ValueError:
            PORT = 8080
        app.jinja_env.auto_reload = True
        app.run(HOST, PORT)

    