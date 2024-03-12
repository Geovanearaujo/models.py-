from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Evento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    data_horario = db.Column(db.DateTime, nullable=False)
    localizacao = db.Column(db.String(120), nullable=True)
    imagens = db.Column(db.String(300), nullable=True)
    descricao = db.Column(db.String(500), nullable=True)
    inscritos = db.relationship('Inscrito', backref='evento', lazy=True)

class Inscrito(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    evento_id = db.Column(db.Integer, db.ForeignKey('evento.id'), nullable=False)
