from flask import Flask, request

def create_app():
    app = Flask(__name__)

    # Configuración de la aplicación
    app.config.from_object("config.Config")

    # Middleware para registrar cada solicitud
    @app.before_request
    def log_request():
        print(f"Entró una petición: {request.method} {request.path}")

    # Registrar las rutas
    with app.app_context():
        from .routes import register_routes
        register_routes(app)

    return app
