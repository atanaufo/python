'''
CleanText

https://towardsdatascience.com/automate-your-text-processing-workflow-in-a-single-line-of-python-code-e276755e45de

Para utilizar a library:
pip install clean-text

CleanText é uma biblioteca Python de código aberto que permite limpar os dados textuais extraídos
da web ou da mídia social. CleanText permite que os desenvolvedores criem uma representação de texto normalizada.
CleanText usa ftfy, unidecode e várias outras regras codificadas, incluindo RegEx para converter um
texto de entrada corrompido ou sujo em um texto limpo, que pode ser processado posteriormente
para treinar um modelo de PNL.

Caso ocorra erro de Unicode:
pip install Unidecode


'''

from unidecode import unidecode
from cleantext import clean

# Unicode:
s1 = "Zürich"
clean(s1, fix_unicode=True)

