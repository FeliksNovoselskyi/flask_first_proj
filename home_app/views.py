import flask
from flask_login import current_user

def home_view():
    return flask.render_template(template_name_or_list='home_page.html')