import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bootstrap = Bootstrap()
login_manger = LoginManager()
bcrypt = Bcrypt()
login_manger.login_view='authentication.do_the_login'
login_manger.session_protection='strong'

def create_app(config_type):
    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(),'config', 'prod' + '.py')
    app.config.from_pyfile(configuration)

    db.init_app(app)
    bootstrap.init_app(app)
    login_manger.init_app(app)
    bcrypt.init_app(app)

    from app.catalog import main
    app.register_blueprint(main)

    return app
