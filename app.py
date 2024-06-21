from flask import Flask
from flask_migrate import Migrate
from dotenv import load_dotenv , dotenv_values
from models import db,User
from controller.main import main
from controller.auth import auth

app = Flask(__name__)
migrate = Migrate()

def create_app():
    config = dotenv_values()
    app.config.from_mapping(config)
    
    db.init_app(app)
    migrate.init_app(app,db,render_as_batch=True)
    
    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app

app = create_app()

app.run(debug=True)