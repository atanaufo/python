
import brazilcep

endereco = brazilcep.get_address_from_cep('37503130')

print(endereco['cep'])