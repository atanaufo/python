'''
EXERCICIO:
Faça um programa que pergunte a idade, o peso e a altura
de uma pessoa e decide se ela está apta a servir o Exercito

Regras:
Mais de 18 anos,
Pesar mais ou igual 60 Kilos,
Medir mais ou igual 1.70 metros
'''

var_idade = 18
var_peso = 60
var_altura = 1.70

print('Registro no Exército Brasileiro:')
idade = int(input('Digitar sua idade: '))
peso = float(input('Digitar o seu peso: '))
altura = float(input('Digitar a sua altura: '))


if (idade >= var_idade and peso >= var_peso and altura >= var_altura):
    print('Quesitos básicos aprovado! Bem Vindo ao Exército Brasileiro Cadete! ')
else:
    print('Não aprovado nos quesitos básicos!')
