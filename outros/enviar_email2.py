import smtplib

PARA = "atanaufo.ramalho@gmail.com\n"      #e-mail destino
USUARIO= "atanaufo.ramalho@gmail.com\n"      #seu  email no google
SENHA= "##Atanaufo@@1980##Setembro"                  #sua senha no google
 
ASSUNTO= "teste de envio de email via python\n"
TEXTO= "Email enviado através de um programa python\n\n"
 
def envia_mail():
    print("Enviando email")
    smtpserver= smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(USUARIO,SENHA)
    msg= 'To:' + PARA + 'From:' +  USUARIO + 'Subject:' + ASSUNTO + TEXTO
     
    smtpserver.sendmail(USUARIO,PARA,msg)
    smtpserver.quit() 
    print("Email enviado")
 
def main():
    envia_mail()
    return 0
 
if __name__ == '__main__':
    main()