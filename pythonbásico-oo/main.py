from veiculo import Veiculo
from carro import Carro

caminhao_rosa = Veiculo('rosa',6, 'ford', 10)

print("Cor: ", caminhao_rosa.cor)
print("Marca: ", caminhao_rosa.marca)
print("Tanque: ", caminhao_rosa.tanque)

print("____________________________________")

carro_azul = Veiculo('Azul', 4, 'BMW', 30)

print("Cor: ", carro_azul.cor)
print("Marca: ", carro_azul.marca)
print("Tanque: ", carro_azul.tanque)
carro_azul.abastecer(35)            # Chama o método e recebe o argumento.
print("Tanque :", carro_azul.tanque)

print("____________________________________")

#Herança:
carro_azul = Carro('Preto', 4, 'FORD', 100)

print("Cor: ", carro_azul.cor)
print("Marca: ", carro_azul.marca)
print("Tanque: ", carro_azul.tanque)
