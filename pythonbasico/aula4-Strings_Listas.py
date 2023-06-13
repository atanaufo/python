frase = 'Oi, tudo bem?'
lista_nomes = ['João','Maria','Bernadete','Maria']

# CRUD
lista_nomes.append('Atanaufo')
lista_nomes.append('Lorena')
lista_nomes.remove('João')
lista_nomes.insert(0,'Creosvaldo')
print('----------------------')

# Irá contar quantas maria existe na variável lista_nomes.
contador = lista_nomes.count('Maria')


# Retornar o último nome, porém, irá remover da lista.
#lista_nomes2 = ['Joao','Maria','Guilherme','Diego','Joao','Paulo']
#print(lista_nomes2.pop()) # Função de Pilha - Retornar sempre o último da lista.
#print(lista_nomes2)


# Com intervalo:
print(frase[0:5])
print(lista_nomes[0:3])
print(lista_nomes[-1])
print('----------------------')


# Métodos para tratamentos de textos:
print(lista_nomes)
print(contador)
print(len(frase))
print(frase.lower())
print(frase.upper())
print(frase.capitalize())
print('----------------------')

# Separa a frase em list
frase_separada = frase.split(',')
print(frase_separada)


#inverter a frase:
print(frase[::-1])

print(lista_nomes[-1:-4:-1])
print('----------------------')

