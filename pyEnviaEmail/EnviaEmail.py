
import smtplib
import email.message

emailRemetente = "infortotalbhz@gmail.com"
emailDestino = "atanaufo.ramalho@gmail.com"
emailAssunto = "Autorização de Pagamento do Fornecedor - Fulano de Tal"
arquivoAnexo = "C:\Anexos\CONFIRMADO.JPG"


def enviaremail():
    corpo_email = """
    <p>Olá teste de envio de e-mail semi automático!</p>
    <p>Usando Python</p>   
    """
    # Estrutura do e-mail:
    msg = email.message.Message()
    msg['Subject'] = emailAssunto
    msg['From'] = emailRemetente
    msg['To'] = emailDestino
    password = 'mhumdjlggqrdfgzi'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)
    #msg.attach(corpo_email)
    # Credenciais de Acesso ao e-mail:
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    s.quit()
try:
    print('\nEmail Enviado.')
    enviaremail()

except:
    print('\nOcorreu um erro no envio.')
