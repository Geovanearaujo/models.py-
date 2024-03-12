# models.py-
# models.py-

Instruções SqlAlchemy:

No projeto sqlalchemy, dentro do arquivo no terminal do vscode, precisa em models.py dar os seguintes comandos:

python3 -m venv venv
source venv/bin/activate
pip install -U Flask-SQLAlchemy

Instruções Firebase:

Substitua 'caminho_para_sua_chave_firebase.json' pelo caminho correto do arquivo JSON que contém sua chave privada do Firebase. Este arquivo é obtido no console do Firebase ao criar uma nova conta de serviço e gerar uma nova chave privada.

Este exemplo assume que você tem duas coleções no Firestore: eventos e inscritos. Você precisa configurar essas coleções no seu Firestore manualmente ou por meio da aplicação, conforme os documentos são adicionados.

Note que a manipulação dos dados no Firestore é feita através de métodos como .collection(), .document(), .get(), e .add(). Esses métodos permitem realizar operações CRUD no Firestore.

Segurança: Certifique-se de configurar as regras de segurança do Firestore adequadamente para proteger seus dados. As regras padrão em um novo banco de dados podem permitir acesso irrestrito, o que não é recomendado para aplicações em produção.

Com essas mudanças, sua aplicação Flask agora está configurada para usar o Firestore como seu banco de dados, permitindo operações de leitura e escrita de documentos no Firestore.
