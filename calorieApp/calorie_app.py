from flask import Flask
from .database.database_manager import initialize_database
from .blueprint.user_blueprint import user_blueprint
from .blueprint.food_entry_blueprint import food_entry_blueprint
from .admin.admin_manager import add_admin_user, remove_admin_user


class CalorieApp:

    def __init__(self):
        print('calorie app')
        self.flask_app = Flask(__name__)
        self.register_blueprint(user_blueprint)
        self.register_blueprint(food_entry_blueprint)
        initialize_database()

    def register_blueprint(self, blueprint):
        self.flask_app.register_blueprint(blueprint)

    def run(self, host, port):
        self.flask_app.run(host=host, port=port)

    def add_admin(self, admin_id):
        add_admin_user(admin_id)

    def remove_admin(self, admin_id):
        remove_admin_user(admin_id)
