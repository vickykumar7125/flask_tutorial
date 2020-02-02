# importing the all components
from flask import Flask, request, render_template, session, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta, time, datetime, date
from admin import admin
from auth import auth
from home import home

# initializing the instance
app = Flask(__name__)

# registering the blueprint
app.register_blueprint(home, url_prefix='/')
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(admin, url_prefix='/admin')

# database configuration
server = '127.0.0.1'
name = 'flask'
user = 'root'
password = 'ASDqwezx71@%'
port = '3306'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + user + ':' + password + '@' + server + ':' + port + '/' + name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# initializing database
database = SQLAlchemy(app)

# database structure


if __name__ == '__main__':
    app.run()
