from flask import jsonify, request

def routes_flokzu(app):
    @app.route("/", methods=["POST"])
    def webhook():
        print(f"Petición recibida: {request.method} {request.path} {request.data}")
        return jsonify({"message": "¡Bienvenido a mi API!"})

    
