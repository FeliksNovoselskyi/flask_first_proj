import flask

def render_home():
    return flask.render_template(template_name_or_list='home_page.html')