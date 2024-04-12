import pandas as pd
import time
import viacep 

# Função para validar o CEP utilizando a biblioteca viacep
def validar_cep(cep):
    """
    Função para validar o CEP utilizando a biblioteca viacep.
    Retorna True se o CEP for válido, False caso contrário.
    """
    via_cep = ViaCEP(cep)
    try:
        via_cep.fetch_data()
        return True
    except:
        return False

# Carrega o arquivo CSV
nome_arquivo_csv = 'arquivo.csv'
df = pd.read_csv(nome_arquivo_csv, delimiter=';')

# Converte a coluna CEP1 para string
df['CEP1'] = df['CEP1'].astype(str)

# Adiciona a coluna de validação de CEP
df['Validação CEP'] = df['CEP1'].apply(validar_cep)

# Mostra o DataFrame
print(df)

# Aguarda 5 segundos antes de prosseguir para a próxima leitura
print("Aguardando 5 segundos...")
time.sleep(5)
print("Continuando para a próxima leitura...")
