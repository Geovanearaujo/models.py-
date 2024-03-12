from flask import Flask
from firebase_db import db  # Esta importação é necessária para inicializar o Firebase
from routes import routes

app = Flask(__name__)

# Registrar as rotas do Blueprint
app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(debug=True)
