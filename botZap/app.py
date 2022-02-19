# 1. Importar bibliotecas necessárias
import pywhatkit
import keyboard
import time
from datetime import datetime

# 2. Definir para quais contatos iremos enviar as msgs

contatos = ['+5531996514243']

# 3. Definir intervalo de envio
while len(contatos) >= 1:
    # enviar mensagens
    pywhatkit.sendwhatmsg(contatos[0],'Olá Marco Antonio eu sou um Robô que ainda está aprendendo caminhar.',datetime.now().hour, datetime.now().minute + 2)
    del contatos[0]
    time.sleep(15)
    
    #    keyboard.press_and_release('ctrl + w')

# 4. Testar

