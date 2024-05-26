import datetime

from flask import Flask
from flask_cors import CORS
from .routes.user_routes import user_bp
from .routes.product_routes import product_bp
from .routes.order_routes import order_bp

from flask_jwt_extended import JWTManager

from flaskext.mysql import MySQL

import configparser

def create_app():
    app = Flask(__name__)

    config_path = '/home/wangpython/Gogroupbuy/backend/config.ini'
    config = configparser.ConfigParser()
    config.read(config_path)

    app.config["JWT_SECRET_KEY"] = config['jwt']['JWT_SECRET_KEY']
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(hours=24)

    app.config['MYSQL_DATABASE_HOST'] = config['db']['host']
    app.config['MYSQL_DATABASE_USER'] = config['db']['username']
    app.config['MYSQL_DATABASE_PASSWORD'] = config['db']['password']
    app.config['MYSQL_DATABASE_DB'] = config['db']['database']

    mysql = MySQL(app)
    jwt = JWTManager(app)
    CORS(app)
    
    # Register Blueprints
    app.register_blueprint(user_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(order_bp)



    return app