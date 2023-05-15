# Arquivo para criar o banco de dados se não existir:

from fakepinterest import database, app
from fakepinterest.models import Usuario, Foto

# Roda apenas uma vez para poder criar a database:
with app.app_context():
    database.create_all()