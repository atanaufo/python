nomes = ['Atanaufo','Marco Antonio','Tonho','Julia','Teste','Teste2']


# nome = objeto de coleção
for nome in nomes:
    print(nome)

# função range:
lista_numeros = range(5)
for i in lista_numeros:
    print(i)
print('------------------')

# função range de x a y:
lista_numeros = range(1,5)
for i in lista_numeros:
    print(i)
print('-------------------')

# função range de x a y com step:
lista_numeros = range(0, 100, 2)
for i in lista_numeros:
    print(i)

# função range com função len (contador caractere)
for i in range(len(nomes)):
    print(nomes[i])
print('---------------------')

# função range com função len (contador caractere) e append (inclusão)
for i in range(len(nomes)):
    print(nomes[i])
    nomes.append('oiii')
print(nomes)
print('---------------------')

# Usando o for com uma variável:
palavra = 'Atanaufo de Paula Ramalho'

for letra in palavra:
    print(letra)
print('-----------------------')

# Estrutura de laço While (enquanto) para tomada de decisão.

i = 0
while i < 10:
    print('i ainda é menor que 10: ', i)
    i = i + 1 # ou usar i += 1
print('Acabou o while: ', i)
print('--FIM WHILE ---------------------------------')

# Contar lista de frutas com o FOR ou LEN
lista_frutas = ['maca','pera','uva','abacaxi','goiaba']
contador = 0

for fruta in lista_frutas:
    contador += 1
print(contador)
print('--FIM CONTADOR LISTA DE FRUTAS COM FOR ----------------')

print(len(lista_frutas))
print('--FIM CONTADOR LISTA DE FRUTAS COM LEN ------------------')


# Usando o BREAK para parar
numero = 0

while True:
    print(numero)
    if numero == 20:
        break
    numero += 1
print('-- SAIU COM WHILE com Break --------------------------')



