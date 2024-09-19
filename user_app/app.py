import flask

# Blueprint - это способ организации маршрутов, шаблонов и статических файлов для различных частей или модулей приложения Flask
user_app = flask.Blueprint(
    name= 'user_app', # Имя blueprint
    import_name= 'user_app', # Это имя пакета или модуля, который будет ассоциироваться с этим Blueprint
    template_folder='templates', # Папка с шаблонами для user_app
    static_folder='static', # Папка со статическими файлами для user_app
    static_url_path='/user_app/' # Ссылка на страницу
)
