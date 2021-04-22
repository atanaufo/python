class Veiculo():

# Método Construtor:
    def __init__(self, cor, rodas, marca, tanque):
        self.cor = cor
        self.marca = marca
        self.rodas = rodas
        self.tanque = tanque

# Método definido pelo usuário:
    def abastecer(self, litros):
        self.tanque += litros

