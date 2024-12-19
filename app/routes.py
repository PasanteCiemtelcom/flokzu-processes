from flask import jsonify, request

def register_routes(app):
    @app.route("/", methods=["GET"])
    def home():
        print(f"Petición recibida: {request.method} {request.path}")
        return jsonify({"message": "¡Bienvenido a mi API!"})

    @app.route("/items", methods=["GET"])
    def get_items():
        print(f"Petición recibida: {request.method} {request.path}")
        items = [
            {"id": 1, "name": "Manzana", "price": 0.5},
            {"id": 2, "name": "Naranja", "price": 0.75},
        ]
        return jsonify(items)

    @app.route("/items/<int:item_id>", methods=["GET"])
    def get_item(item_id):
        print(f"Petición recibida: {request.method} {request.path} con item_id={item_id}")
        items = [
            {"id": 1, "name": "Manzana", "price": 0.5},
            {"id": 2, "name": "Naranja", "price": 0.75},
        ]
        item = next((item for item in items if item["id"] == item_id), None)
        if item:
            return jsonify(item)
        else:
            return jsonify({"error": "Item no encontrado"}), 404

    @app.route("/items", methods=["POST"])
    def add_item():
        print(f"Petición recibida: {request.method} {request.path} con datos {request.get_json()}")
        data = request.get_json()
        if "name" in data and "price" in data:
            new_item = {
                "id": 3,  # En un caso real, deberías generar el ID dinámicamente.
                "name": data["name"],
                "price": data["price"],
            }
            return jsonify(new_item), 201
        else:
            return jsonify({"error": "Faltan datos en el cuerpo de la solicitud"}), 400
