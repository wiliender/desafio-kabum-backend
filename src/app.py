from flask import Flask
from flask_cors import CORS
from routes import shipping, healthcheck

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    # register routes
    app.register_blueprint(shipping.route)
    app.register_blueprint(healthcheck.route)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(threaded=True, port=5000)   