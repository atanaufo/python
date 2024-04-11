import brazilcep

# Suponha que 'cep_cadastrado' seja o CEP lido da coluna 'CEP1'
address = brazilcep.get_address_from_cep('72920000')
print(address)
