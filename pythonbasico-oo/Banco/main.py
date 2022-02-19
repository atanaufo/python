'''
EXERCÍCIO: Criar uma solução de gerenciamento bancário.

1 - Criar clientes e contas;
2 - Cada cliente deverá possuir: nome, cpf e idade.
3 - Cada conta deverá possuir um cliente, saldo e limite.
4 - Criar métodos em conta: sacar, depositar e consultar saldo.

'''

from cliente import Cliente
from conta import  Conta

cliente1 = Cliente('Gui','123.456.789-10', 30)

#print(cliente1)

conta_do_gui = Conta(cliente1,10.50)

print('############## CONTA #######################')
print(conta_do_gui.cliente.nome, conta_do_gui.consulta_saldo())
print('############## CONTA: DEPOSITAR #######################')
conta_do_gui.depositar(1000.40)
print('Consulta Saldo: ', conta_do_gui.consulta_saldo())

print('############## CONTA: SACAR #######################')
conta_do_gui.sacar(500)
print('Consulta Saldo: ', conta_do_gui.consulta_saldo())

print('############## CONTA: SACAR #######################')
conta_do_gui.sacar(1000)
print('Consulta Saldo: ', conta_do_gui.consulta_saldo())

