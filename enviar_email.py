import smtplib
 
fromaddr = 'atanaufo.ramalho@gmail.com'
toaddrs  = 'atanaufo.ramalho@gmail.com'
msg = 'Corpo da mensagem do e-mail.'
subject = 'Pedido de urnas -- Assunto do e-mail'
message = 'Subject: %s\n\n%s' % (subject, msg)

# Dados da conta utilizada para enviar o email
username = 'atanaufo.ramalho@gmail.com'
password = '##Atanaufo@@1980##Setembro'
 
# Lógica de envio dos dados
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, message)
server.quit()