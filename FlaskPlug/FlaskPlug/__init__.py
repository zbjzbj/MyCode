from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from FlaskPlug.views.user import userBlue
# from flask_session import Session


def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config.from_object('settings.DevConfig')
    # Session(app)
    app.register_blueprint(userBlue)
    db.init_app(app)
    return app



