from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from config import Config
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

# Definimos el modelo para Reservas
class Reserva(db.Model):
    __tablename__ = 'reservas'

    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, nullable=False)
    libro_id = db.Column(db.Integer, nullable=False)
    fecha_reserva = db.Column(db.Date, nullable=False)
    estado = db.Column(db.String(50), nullable=False)

    def __init__(self, cliente_id, libro_id, fecha_reserva, estado):
        self.cliente_id = cliente_id
        self.libro_id = libro_id
        self.fecha_reserva = fecha_reserva
        self.estado = estado

# Creamos la tabla de reservas en la base de datos
with app.app_context():
    db.create_all()

# Obtenemos todas las reservas solicitadas
@app.route('/reservas', methods=['GET'])
def obtener_reservas():
    reservas = Reserva.query.all()
    resultado = []
    for reserva in reservas:
        resultado.append({
            'id': reserva.id,
            'cliente_id': reserva.cliente_id,
            'libro_id': reserva.libro_id,
            'fecha_reserva': reserva.fecha_reserva.strftime('%Y-%m-%d'),
            'estado': reserva.estado
        })
    return jsonify(resultado)

# Creamos una nueva reserva
@app.route('/reservas', methods=['POST'])
def crear_reserva():
    datos = request.get_json()
    nueva_reserva = Reserva(
        cliente_id=datos['cliente_id'],
        libro_id=datos['libro_id'],
        fecha_reserva=datetime.strptime(datos['fecha_reserva'], '%Y-%m-%d'),
        estado=datos['estado']
    )
    db.session.add(nueva_reserva)
    db.session.commit()
    return jsonify({
        'message': 'Reserva creada con éxito.',
        'reserva_id': nueva_reserva.id
    }), 201

if __name__ == '__main__':
    app.run(debug=True)
