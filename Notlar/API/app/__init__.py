from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from app.config import Config
from flask_jwt_extended import JWTManager


app = Flask(__name__)

db = SQLAlchemy()
ma = Marshmallow()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    from app.routes import main
    app.register_blueprint(main)
    with app.app_context():
        db.create_all()

    return app