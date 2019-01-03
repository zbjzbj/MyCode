from flask import Blueprint, session


userBlue = Blueprint("userBlue", __name__)


@userBlue.route('/')
def index():
    session['test'] = 'test-flask-session'
    return "index"


@userBlue.route("/user")
def user():
    print(session.get('test'))
    return "user"


