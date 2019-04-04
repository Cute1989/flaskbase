from flask import Flask,jsonify

def create_app():
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        return "Hello Flask and uWSGI"

    return app