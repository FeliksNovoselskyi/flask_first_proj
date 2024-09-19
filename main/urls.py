from .settings import main_project
import home_app

home_app.home_app.add_url_rule(rule= '/', view_func= home_app.render_home, methods = ["GET", "POST"])
main_project.register_blueprint(blueprint = home_app.home_app)

