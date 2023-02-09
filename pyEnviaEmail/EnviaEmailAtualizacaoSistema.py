
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from email.mime.base import MIMEBase
from email import encoders

# 1 - Configuração da Conta do Servidor SMTP:
host = "smtp.gmail.com"
port = "587"
login = "suporte2@planosmetropax.com.br"
senha = "rpkxtwvboxdlirnz"

server = smtplib.SMTP(host,port)
server.ehlo()
server.starttls()
server.login(login,senha)

# 2 - Construir o email tipo MIME:
numeroVersao = '4.15b299'
emailAssunto = '[Metropax / Cortel] Atualização de Release Sankhya - Ambiente de Teste'
emailDestino = 'atanaufo.ramalho@gmail.com'
emailCorpo = """ <p><strong><span style="font-size:18px">Olá,&nbsp;</span></strong></p>
<p><span style="font-size:18px">Informo que o ambiente de teste foi atualizado para a seguinte vers&atilde;o / release: <b>""" + numeroVersao  + """</b> para que possam realizar valida&ccedil;&otilde;es em suas principais rotinas.</span></p>
<p>&nbsp;</p>
<p><span style="font-size:18px">Aqueles que n&atilde;o possuem acesso ao ambiente de teste Sankhya podem seguir o v&iacute;deo&nbsp;demonstrativo de como configurar em:</span></p>
<p><span style="font-size:18px">https://youtu.be/4FAmX17YqWo.</span></p>
<p>&nbsp;</p>
<p><span style="font-size:18px">Endere&ccedil;o do ambiente de teste, caso seja necess&aacute;rio configurar no seu navegador sankhya:&nbsp; mpsrvv12:8280/mge</span></p>
<p><span style="font-size:18px">Caso tenha esquecido de algu&eacute;m, por favor encaminhar este e-mail.</span></p>
<p>&nbsp;</p>
<p><br />
<span style="font-size:18px">Atenciosamente.</span></p>
<p>&nbsp;</p>   """

email_msg = MIMEMultipart()
email_msg['From'] = login
email_msg['To'] = emailDestino
email_msg['Subject'] = emailAssunto
email_msg.attach(MIMEText(emailCorpo,'html'))

# PARA ATIVAR O ENVIO DE ANEXO, DESCOMENTAR AS LINHAS A SEGUIR:
# Abrimos o arquivo em modo leitura e binary:
#caminhoArquivo = "C:\\Anexos_Gold\\teste.pdf"
#attachment = open(caminhoArquivo, 'rb')

# Leitura do arquivo no modo binário e codificando em base 64:
#att = MIMEBase('application','octet-stream')
#att.set_payload(attachment.read())
#encoders.encode_base64(att)

# Adicionamento do cabeçalho no tipo anexo do email
#att.add_header('Content-Disposition',f'attachment; filename= teste.pdf')
# Fechamos o arquivo
#attachment.close()
# Adicionamos o anexo no corpo do email
#email_msg.attach(att)


# 3 - Enviar o email tipo MIME no SERVIDOR:
server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())
server.quit()
try:
    print('Enviado com sucesso!')
except:
    print('Ocorreu algum erro no envio!')