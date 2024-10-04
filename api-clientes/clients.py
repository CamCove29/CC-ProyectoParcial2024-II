from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Instancia de Flask/SQLAlchemy
clients_api = Flask(__name__)

# Configuración de la base de datos PostgreSQL
clients_api.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:password@localhost:5432/clientes_db"
clients_api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos y CORS
db = SQLAlchemy(clients_api)
CORS(clients_api)

# Modelo de Cliente
class Client(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo_electronico = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(15), nullable=False)

    def __repr__(self):
        return f'<Client {self.id}>'

# Manejo de errores 404
@clients_api.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found.'}), 404

# Manejo de errores 500
@clients_api.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': 'Internal server error.'}), 500

# Endpoint para crear un nuevo cliente
@clients_api.route('/clients', methods=['POST'])
def create_client():
    data = request.get_json()
    new_client = Client(
        nombre=data['nombre'],
        correo_electronico=data['correo_electronico'],
        telefono=data['telefono']
    )
    db.session.add(new_client)
    db.session.commit()
    return jsonify({'message': 'Client created successfully', 'id': new_client.id}), 201

# Endpoint para obtener todos los clientes
@clients_api.route('/clients', methods=['GET'])
def get_clients():
    clients = Client.query.all()
    return jsonify([{
        'id': client.id,
        'nombre': client.nombre,
        'correo_electronico': client.correo_electronico,
        'telefono': client.telefono
    } for client in clients]), 200

# Endpoint para obtener un cliente por ID
@clients_api.route('/clients/<int:id>', methods=['GET'])
def get_client(id):
    client = Client.query.get(id)
    if client is None:
        return not_found(404)
    return jsonify({
        'id': client.id,
        'nombre': client.nombre,
        'correo_electronico': client.correo_electronico,
        'telefono': client.telefono
    }), 200

# Endpoint para actualizar un cliente por ID
@clients_api.route('/clients/<int:id>', methods=['PATCH'])
def update_client(id):
    client = Client.query.get(id)
    if client is None:
        return not_found(404)

    data = request.get_json()
    if 'nombre' in data:
        client.nombre = data['nombre']
    if 'correo_electronico' in data:
        client.correo_electronico = data['correo_electronico']
    if 'telefono' in data:
        client.telefono = data['telefono']
    
    db.session.commit()
    return jsonify({'message': 'Client updated successfully'}), 200

# Endpoint para eliminar un cliente por ID
@clients_api.route('/clients/<int:id>', methods=['DELETE'])
def delete_client(id):
    client = Client.query.get(id)
    if client is None:
        return not_found(404)

    db.session.delete(client)
    db.session.commit()
    return jsonify({'message': 'Client deleted successfully'}), 204


if __name__ == '__main__':
    clients_api.run(host='0.0.0.0', port=8011, debug=True)
