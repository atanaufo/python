'''
Exemplos de funções:

print()
len()

'''

# Criando funções personalizadas: Neste caso iremos criar uma função básica de soma.

def soma(numero1, numero2):
    resp = numero1 + numero2
    return resp

# Chamando a função soma criado anteriormente para isso podemos usar numa variável.
retorno = soma(75, 1289)
print(retorno)

# A função necessáriamente não precisa ter argumentos ou return:
def imprime_oi():
    print("OI")

imprime_oi()

# Criando função booleano:
def tem_set_itens(argumento):
    if len(argumento) == 7:
        return True
    else:
        return False

print(tem_set_itens('Atanaufo'))


