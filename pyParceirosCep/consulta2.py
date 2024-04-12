
import brazilcep

endereco = brazilcep.get_address_from_cep('35620000')

print(endereco['cep'])