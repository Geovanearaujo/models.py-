from flask import Blueprint, request, jsonify
from .firebase_db import db

routes = Blueprint('routes', __name__)

@routes.route('/eventos', methods=['GET'])
def listar_eventos():
    eventos_ref = db.collection('eventos')
    docs = eventos_ref.stream()
    eventos = [{doc.id: doc.to_dict()} for doc in docs]
    return jsonify(eventos)

@routes.route('/eventos/<evento_id>', methods=['GET'])
def mostrar_evento(evento_id):
    doc_ref = db.collection('eventos').document(evento_id)
    doc = doc_ref.get()
    if doc.exists:
        evento = doc.to_dict()
        # Aqui você pode adicionar lógica para buscar inscritos se necessário
        return jsonify(evento), 200
    else:
        return jsonify({'mensagem': 'Evento não encontrado'}), 404

@routes.route('/inscritos', methods=['POST'])
def adicionar_inscrito():
    dados = request.json
    # Aqui você deve garantir que 'evento_id' está presente em 'dados' para relacioná-lo ao evento
    result = db.collection('inscritos').add(dados)
    return jsonify({'id': result[1].id}), 201
