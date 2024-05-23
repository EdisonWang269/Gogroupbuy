from flask import Flask
from flask_cors import CORS
from .routes.user_routes import user_bp
from .routes.product_routes import product_bp
from .routes.order_routes import order_bp

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    # Register Blueprints
    app.register_blueprint(user_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(order_bp)

    return app