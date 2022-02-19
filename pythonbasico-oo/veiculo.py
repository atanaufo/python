class Veiculo:

    # Criando método construtor para passagem de argumentos:
    def __init__(self, ArgCor, ArgRodas, ArgMarca, ArgTanque):
        self.cor = ArgCor
        self.rodas = ArgRodas
        self.marca = ArgMarca
        self.tanque = ArgTanque

    def abastecer(self,litros):
        self.tanque += litros

    def consumo(self,litros):
        self.tanque -= litros
