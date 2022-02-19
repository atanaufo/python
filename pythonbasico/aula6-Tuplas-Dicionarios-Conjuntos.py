# Para iniciar sem dados.
minha_lista = []
minha_tupla = ()
meu_dicionario = {}
meu_conjunto = set()
print('--Objetos inicializados vazios !!!')

minha_lista = ['Atanaufo','Paula'] #LISTA [list] = Multável - Aceita append e remove.
minha_tupla = ('Atanaufo','Paula') #TUPLA (tuple) = Fixa - Não aceita append e remove.


meu_dicionario = {'nome':'Atanaufo','idade':39} #DICIONARIO {dict} - Tem uma chave e um valor {KEY:VALUE}.
meu_conjunto = {'Atanaufo','Paula'} #CONJUNTO {set} - Uma lista misturado com dicionário.
                                    # Porém não aceita item repetido e não é ordenado.
                                    # Ou seja, utiliza-se quando não se quiser dados repetidos.

'''
Atenção: 
Quando necessitar pesquisar em uma estrutura de dados muito grande a melhor indicação será utilizar
Dicionário {dict} ou  Conjunto {set}

'''


print(minha_tupla)

for nome in minha_tupla:
    print(nome)
print('--FIM TUPLA -----------------------')

if 'Paula' in minha_tupla:
    print('Encontrado!')
else:
    print('Não encontrado!')
print('--FIM ELIF  ---------------------------')

for valores in meu_dicionario.values():
    print(valores)

# Para pesquisa o dicionário é mais utilizado por ser mais rápido.
# Pesquisará dentro dos valores (values)
if 'Guilherme' in meu_dicionario.values():
    print('Guilherme está no dicionário')
else:
    print('Guilherme não está no dicionário')
print('--FIM PROCURA NO DICIONÁRIO')

# Posso também saber qual o type do meu objeto:
print(type(meu_dicionario))

# Irá substituir o 'Guilherme' no meu dicionário por 'Jonhy'
meu_dicionario['nome'] = 'Jonhy'
# Posso adicionar novas keys.
meu_dicionario['endereco'] = 'Av. João das Neves'
print(meu_dicionario)
print('--FIM MANIPULANDO DICIONÁRIOS ---------------')
# Limpar meu dicionario:
meu_dicionario.clear()
print('--FIM Limpar -------------------------------')
print(meu_dicionario)
print('--Demonstrando que o dict está limpo ------------')

# Adição de dados no conjunto
meu_conjunto.add('Maria')
meu_conjunto.add('Tonho')
meu_conjunto.add('Atanaufo')
print(meu_conjunto)
print('--FIM Adição de dados em Conjunto {set}')
if 'Maria' in meu_conjunto:
    print('Encontrado!')
else:
    print('Não encontrado!')
print('--FIM Pesquisa de dados em Conjunto {set}')

# Permite realizar alinhamento tipos de dados um dentro do outro.
loucura = [(1,2), (3,4), (5,6), ({'João ','Maria'}, {'Gabriel'})]
print(loucura)
print(type(loucura))
print('--FIM Alinhamento -----------------------------------')