#   pip install SpeechRecognition
#   pip install pyttsx3
#   pip install PyAudio
#   pip install wikipedia
#   pip install pywhatkit

import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit


audio = sr.Recognizer()

maquina = pyttsx3.init()

#maquina.say('Ola, eu sou a Tina')
#maquina.say('Como posso ajudar maledito?')
#maquina.runAndWait()

def executa_comando():

    try:
        with sr.Microphone() as source:
            print('Ouvindo ..')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            if 'tina' in comando:
                comando = comando.replace('tina', '')
                maquina.say(comando)
                maquina.runAndWait()
                
    except:
        print('Microfone não funciona.')
    
    return comando

def comando_voz_usuario():
    comando = executa_comando()
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('Agora são' + hora)
        maquina.runAndWait()
    elif 'procure por' in comando:
        procurar = comando.replace('procure por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar,2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
    elif 'toque' in comando:
        musica = comando.replace('toque', '')
        resultado = pywhatkit.playonyt(musica)
        maquina.say('Tocando musica')
        maquina.runAndWait()
    elif 'envia mensagem' in comando:
        mensagem = comando.replace('envia mensagem','')
        resultado = pywhatkit.sendwhatmsg('+5531998542933','Olá é um teste ...', 16, 53)
        maquina.say('Enviando mensagem')
        maquina.runAndWait()
        
comando_voz_usuario()
