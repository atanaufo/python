class Conta:
    def __init__(self, ArgCliente, ArgSaldo):
        self.cliente = ArgCliente
        self.saldo = ArgSaldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print("Foi depositado: ", valor)
        else:
            print("Erro no depósito! ")

    def consulta_saldo(self):
        return  self.saldo

    def sacar(self,valor):
        if self.saldo - valor <= 0:
            print("Saldo Insuficiente! ")
        else:
            self.saldo -= valor
            print("Foi sacado:", valor)




