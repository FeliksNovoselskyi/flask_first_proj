import flask

# Blueprint - это способ организации маршрутов, шаблонов и статических файлов для различных частей или модулей приложения Flask
home_app = flask.Blueprint(
    name= 'home_app', # Имя blueprint
    import_name= 'home_app', # Это имя пакета или модуля, который будет ассоциироваться с этим Blueprint
    template_folder='templates', # Папка с шаблонами для home_app
    static_folder='static', # Папка со статическими файлами для home_app
    static_url_path='/home_app/' # Ссылка на страницу
)