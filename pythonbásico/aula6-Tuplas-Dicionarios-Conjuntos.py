minha_lista = [] # Para iniciar sem dados.
minha_tupla = ()
meu_dicionario = {}
meu_conjunto = set()


minha_lista = ['Atanaufo','Paula'] #LISTA = Multável - Aceita append e remove.
minha_tupla = ('Atanaufo','Paula') #TUPLA = Fixa - Não aceita append e remove.

meu_dicionario = {'nome':'Atanaufo','idade':39} #DICIONARIO (dict)

meu_conjunto = {'Atanaufo','Paula'} #CONJUNTO (set)

print(minha_tupla)

for nome in minha_tupla:
    print(nome)


if 'Paula' in minha_tupla:
    print('Encontrado!')
else:
    print('Não encontrado!')


for valores in meu_dicionario.values():
    print(valores)

#meu_conjunto.add('Maria')
#meu_conjunto.add('Tonho')
#meu_conjunto.add('Atanaufo')
#print(meu_conjunto)

if 'Maria' in meu_conjunto:
    print('Encontrado!')
else:
    print('Não encontrado!')

