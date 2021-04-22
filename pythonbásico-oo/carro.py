from veiculo import Veiculo

class Carro(Veiculo):

    # Herança - Herdar Características.
    def __init__(self, cor, rodas, marca, tanque):
        Veiculo.__init__(cor, rodas, marca, tanque)
        
