import firebase_admin
from firebase_admin import credentials, firestore

# Use a chave privada que você baixou do Firebase
cred = credentials.Certificate('caminho/para/sua/chave-privada-firebase.json')
firebase_admin.initialize_app(cred)

# Obter uma referência ao serviço de banco de dados
db = firestore.client()
