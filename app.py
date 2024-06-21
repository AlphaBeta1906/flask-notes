from flask import Flask
from flask_migrate import Migrate
from dotenv import load_dotenv , dotenv_values
from models import db,User
from controller.main import main
from controller.auth import auth
import os

app = Flask(__name__)
migrate = Migrate()

def create_app():
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    db.init_app(app)
    migrate.init_app(app,db,render_as_batch=True)

    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app

app = create_app()

app.run(debug=True)