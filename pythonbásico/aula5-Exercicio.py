'''
Exercício:
Faça um programa que leia a quantidade de pessoas que serão
convidadas para uma festa.
Após isso o programa irá perguntar o nome de todas as pessoas
e colocar numa lista de convidados.
Após irá imprimir todos os nomes da lista.
'''

numero_de_convidados = input('Digite o número de convidados: ')
lista_de_convidados = []
i = 1

while i <= int(numero_de_convidados):
    nome_do_convidado = input('Digite o nome do convidado #' + str(i) + ': ')
    lista_de_convidados.append(nome_do_convidado)
    i += 1
for convidado in lista_de_convidados:
    print(convidado)

