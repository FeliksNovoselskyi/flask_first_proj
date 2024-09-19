from flask import *
from flask_bcrypt import *
from flask_login import * # current_user, login_user, logout_user
from .models import *
from main.settings import *

# Инициализируем bcrypt для дальнейшей шифровки пароля
bcrypt = Bcrypt()

def auth_view():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        
        if 'leave_btn' in request.form:
            logout_user() 
            flash('Ви вийшли з системи.', 'info')
            return redirect('/')
        
        # Поиск пользователя в базе данных
        user = User.query.filter_by(username=username).first()
        
        if username and password:
            if user and bcrypt.check_password_hash(user.password, password):
                # Успешная авторизация
                login_user(user)
                flash('Вітаємо у вашому акаунті!', 'success')
                return redirect('/')  # Перенаправьте на домашнюю страницу
            else:
                flash("Неправильне ім'я або пароль!", 'danger')
        else:
            flash('Заповніть усі поля!', 'danger')

    return render_template(template_name_or_list='auth_page.html')

def reg_view():
    if request.method == "POST":
        print(request.form)
        
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if username and password and confirm_password:
            if password == confirm_password:
                hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
                
                user = User(
                    username = username,
                    password = hashed_password,
                )
                
                DB.session.add(user)
                DB.session.commit()
            else:
                flash('Паролі не збігаються!', 'danger')
        else:
            flash('Заповніть усі поля!', 'danger')
    
    return render_template(template_name_or_list='reg_page.html')