from flask import Flask, flash
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = "unknown jkl"
  app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
  db.init_app(app)

  from .views import views
  from .auth import auth
  from .quiz import quiz

  app.register_blueprint(views, url_prefix='/')
  app.register_blueprint(auth, url_prefix='/')
  app.register_blueprint(quiz, url_prefx='/')

  from .models import User, Note

  create_database(app)

  login_manager = LoginManager()
  login_manager.login_view = 'auth.login'
  login_manager.init_app(app)

  @login_manager.user_loader
  def load_user(identification):
    return User.query.get(int(identification))

  return app


def create_database(app):
  if not path.exists('Flask Website/' + DB_NAME):
    with app.app_context():
      db.create_all()
    print('Created Database!')
