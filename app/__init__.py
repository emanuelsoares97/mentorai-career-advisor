from flask import Flask
from app.routes.frontend import bp as frontend_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(frontend_bp)
    return app
