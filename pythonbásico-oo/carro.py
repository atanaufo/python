from veiculo import Veiculo

class Carro(Veiculo):

    # Herança - Herdar Características.
    def __init__(self, cor, rodas, marca, tanque):
        Veiculo.__init__(self, cor, rodas, marca, tanque)
        
