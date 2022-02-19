from veiculo import Veiculo
from carro import Carro

# Criando um objeto:
caminhao_1 = Veiculo('rosa',6,'ford', 10)

# print(caminhao)
# print(type(caminhao))

print("Cor: ", caminhao_1.cor)
print("Marca: ", caminhao_1.marca)
print("Rodas: ", caminhao_1.rodas)
print("Tanque: ", caminhao_1.tanque)

print("#################################")

carro_1 = Veiculo('Azul',4,'Fiat',30)

print("Cor: ", carro_1.cor)
print("Marca: ", carro_1.marca)
print("Rodas: ", carro_1.rodas)
print("Tanque: ", carro_1.tanque)
carro_1.abastecer(35)
print("Tanque Abastecido: ", carro_1.tanque)
carro_1.consumo(5)
print("Nível Atual: ", carro_1.tanque, ' Litros')

print("#################################")

print("Trabalhando com Herança:")

carro_2 = Carro('Azul','Monster Truck',30)

print("Cor: ", carro_2.cor)
print("Marca: ", carro_2.marca)
print("Rodas: ", carro_2.rodas)
print("Tanque: ", carro_2.tanque)
carro_2.abastecer(10)
print("Tanque Atual: ", carro_2.tanque)
carro_2.abastecer(70)
print("Tanque Final: ", carro_2.tanque)

