from main.settings import *  # Импортируем DB из main
from flask_login import UserMixin

# Модель пользователя наследующая модель UserMixin 
# для того чтобы можно было создать нормальный функционал сохранения сессии
class User(UserMixin, DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    username = DB.Column(DB.String(150), unique=True, nullable=False)
    password = DB.Column(DB.String(150), nullable=False)
