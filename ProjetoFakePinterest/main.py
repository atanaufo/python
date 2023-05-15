# Rodar no terminal do projeto: pip install flask
# Para utilizar login com criptografia rodar no terminal do projeto: pip install flask-login flask-bcrypt
# Para criar formulário: pip install flask-wtf
# Para validar e-mails: pip install email_validator

from fakepinterest import app

if __name__ == "__main__":
    app.run(debug=True)
