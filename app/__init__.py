from flask import Flask, request

def create_app():
    app = Flask(__name__)

    app.config.from_object("config.Config")

    @app.after_request
    def log_arquest():
        print(f"La petición es: {request.method} {request.path} {request.data} {request.args}")
        
    @app.before_request
    def log_brequest():
        print(f"Entró una petición: {request.method} {request.path}")
        

    with app.app_context():
        from .routes.flokzu import routes_flokzu
        routes_flokzu(app)

    return app
