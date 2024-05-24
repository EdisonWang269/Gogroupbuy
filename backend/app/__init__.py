from flask import Flask
from flask_cors import CORS
from .routes.user_routes import user_bp
from .routes.product_routes import product_bp
from .routes.order_routes import order_bp

from flask_jwt_extended import create_access_token, get_jwt
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)
    
    JWT_SECRET_KEY = 'DXCs7OJoRpgNwitDBlj2pTqjhGj2xvaQtWGkBo6CBpjTvbHsaVSCXIaspQGtGBG60lUqw8YFqapZUdQam4w9jQ'
    app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY
    jwt = JWTManager(app)
    CORS(app)
    
    # Register Blueprints
    app.register_blueprint(user_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(order_bp)



    return app