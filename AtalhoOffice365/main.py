'''

Via terminal:

Para instalar o Autogui para comandos de teclas: pip install pyautogui

Para instalar o Cx Freeze: pip install cx-Freeze
    Converter em exe. Executar no terminal: cxfreeze .\main.py

Para criar um setup de compilamento dos objetos e dependências externas.
    Criar um arquivo dentro do seu projeto, chamado por exemplo: setup.py

    No final executar o comando no terminal: python .\setup.py build


'''

import pyautogui

pyautogui.PAUSE = 5

pyautogui.hotkey("alt","win","ctrl","shift")










