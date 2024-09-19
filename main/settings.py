import flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Главное приложение
main_project = flask.Flask(
    import_name= "main",
    template_folder= "templates"
)

# Секретный ключ
main_project.secret_key = "123456"

# Создаём экземпляр базы данных
DB = SQLAlchemy()

main_project.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Путь к базе данных
main_project.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

DB.init_app(main_project)  # Инициализация базы данных

migrate = Migrate(main_project, DB)  # Инициализация миграций

# Создание экземпляра LoginManager для управления аутентификацией пользователей
login_manager = LoginManager()
login_manager.init_app(main_project)
login_manager.login_view = 'auth_view'

# Функция для загрузки пользователя по его айдишнику
@login_manager.user_loader
def load_user(user_id):
    from user_app.models import User
    return User.query.get(int(user_id))