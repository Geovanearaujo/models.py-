from flask import Blueprint, request, jsonify
from .models import db, Evento, Inscrito

routes = Blueprint('routes', __name__)

@routes.route('/eventos', methods=['GET'])
def listar_eventos():
    eventos = Evento.query.with_entities(Evento.nome, Evento.data_horario).all()
    return jsonify([{'nome': e.nome, 'data_horario': e.data_horario} for e in eventos])

@routes.route('/eventos/<int:evento_id>', methods=['GET'])
def mostrar_evento(evento_id):
    evento = Evento.query.get_or_404(evento_id)
    inscritos = len(evento.inscritos)
    return jsonify({
        'nome': evento.nome,
        'data_horario': evento.data_horario,
        'localizacao': evento.localizacao,
        'imagens': evento.imagens,
        'descricao': evento.descricao,
        'quantidade_inscritos': inscritos
    })

@routes.route('/inscritos', methods=['POST'])
def adicionar_inscrito():
    dados = request.json
    inscrito = Inscrito(nome=dados['nome'], email=dados['email'], telefone=dados['telefone'], evento_id=dados['evento_id'])
    db.session.add(inscrito)
    db.session.commit()
    return jsonify({'mensagem': 'Inscrito adicionado com sucesso!'}), 201
