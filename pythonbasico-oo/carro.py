from veiculo import Veiculo
# Trabalhando com Herança de Classes e objetos:
class Carro(Veiculo):

    def __init__(self, ArgCor, ArgMarca, ArgTanque):
        Veiculo.__init__(self, ArgCor,4,ArgMarca,ArgTanque)

# No caso da class Carro irá prevalecer o método "abastecer" a seguir:
    def abastecer(self,litros):
        if self.tanque + litros > 50:
            print("Erro: tanque com capacidade inferior !")
        else:
            self.tanque += litros

