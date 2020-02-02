from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__, static_folder='static', template_folder='templates/auth')


@auth.route('/')
@auth.route('/login')
def index():
    return render_template('login.html')

