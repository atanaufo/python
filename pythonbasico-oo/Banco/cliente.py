class Cliente:
    def __init__(self, ArgNome, ArgCpf, ArgIdade):
        self.nome = ArgNome
        self.cpf = ArgCpf
        self.idade = ArgIdade

    def __str__(self):
        return "Nome: " + self.nome + "\nCPF: " + self.cpf + "\nIdade: " + str(self.idade)
