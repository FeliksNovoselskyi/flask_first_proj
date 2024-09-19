from .settings import main_project
import home_app
import user_app

home_app.home_app.add_url_rule(rule= '/', view_func= home_app.home_view, methods = ["GET", "POST"])
user_app.user_app.add_url_rule(rule= '/reg/', view_func= user_app.reg_view, methods = ["GET", "POST"])
user_app.user_app.add_url_rule(rule= '/auth/', view_func= user_app.auth_view, methods = ["GET", "POST"])

main_project.register_blueprint(blueprint = home_app.home_app)
main_project.register_blueprint(blueprint = user_app.user_app)