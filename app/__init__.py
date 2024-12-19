from flask import Flask

def create_app():
    app = Flask(__name__)

    # Configuración de la aplicación
    app.config.from_object("config.Config")

    # Registrar las rutas
    with app.app_context():
        from .routes import register_routes
        register_routes(app)

    return app
