
import smtplib
import email.message

emailRemetente = "suporte2@planosmetropax.com.br"
emailDestino = "atanaufo.ramalho@gmail.com"
emailAssunto = "[Metropax / Cortel] Atualização de Release Sankhya - Ambiente de Teste"
arquivoAnexo = "C:\Anexos\CONFIRMADO.JPG"
numeroVersao = "4.15b299"

def enviaremail():
    corpo_email = """
    <p><strong><span style="font-size:18px">Prezados,&nbsp;</span></strong></p>

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

<p>&nbsp;</p>   
    """
    # Estrutura do e-mail:
    msg = email.message.Message()
    msg['Subject'] = emailAssunto
    msg['From'] = emailRemetente
    msg['To'] = emailDestino
    password = 'rpkxtwvboxdlirnz'
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
