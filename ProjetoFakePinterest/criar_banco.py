# Arquivo para criar o banco de dados se não existir:

from fakepinterest import database, app

# Roda apenas uma vez para poder criar a database:

with app.app_context():
    database.create_all()


