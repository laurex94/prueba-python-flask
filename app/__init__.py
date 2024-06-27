from flask import Flask, jsonify, request
from app.config import Config
from app.extensions import db
# Blueprints
from app.main import bp as main_bp
from app.greeting import bp as greeting_bp

def create_app(config_class=Config, main_bp=main_bp, greeting_bp=greeting_bp):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)

    # Register blueprints here
    app.register_blueprint(main_bp)
    app.register_blueprint(greeting_bp, url_prefix='/saludos')

    with app.app_context():
        db.drop_all()
        db.create_all()
        
    @app.errorhandler(404)
    def page_not_found(error):
        error_message = {
            "error": "This route does not exist, please click on the link below to go back to the main page",
            "url": request.url_root
        }
        response = jsonify(error_message)
        status = 404
        return response, status

    @app.route('/test')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app
