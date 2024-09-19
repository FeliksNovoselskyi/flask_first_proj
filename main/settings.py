import flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

main_project = flask.Flask(
    import_name= "main",
    template_folder= "templates"
)

main_project.secret_key = "123456"

DB = SQLAlchemy()

main_project.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Путь к базе данных
main_project.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

DB.init_app(main_project)  # Инициализация базы данных

migrate = Migrate(main_project, DB)  # Инициализация миграций

login_manager = LoginManager()
login_manager.init_app(main_project)
login_manager.login_view = 'auth_view'

@login_manager.user_loader
def load_user(user_id):
    from user_app.models import User  # Импортируйте модель User здесь, чтобы избежать циклических импортов
    return User.query.get(int(user_id))