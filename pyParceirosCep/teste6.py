import pandas as pd
import brazilcep

# Carregar o arquivo CSV com delimitador de coluna ";"
csv_file = 'C:\\arquivo\\parceiros.csv'  # Substitua pelo caminho do seu arquivo CSV
df = pd.read_csv(csv_file, delimiter=';')

# Converter a coluna "CEP01" para strings (caso não esteja)
df['CEP'] = df['CEP'].astype(str)

# Função para validar o CEP usando a biblioteca brazilcep
def validar_cep(cep):
    try:
        return brazilcep.get_address_from_cep(cep) is not None
    except:
        return False

# Adicionar uma coluna "CEP_valido" com valores booleanos indicando se o CEP é válido
df['CEP_valido'] = df['CEP'].apply(validar_cep)

# Apresentar o DataFrame resultante
print(df)

# Crie um DataFrame com os resultados
#df = pd.DataFrame()

# Salve o DataFrame em um arquivo XLSX
#df.to_excel('C:\\arquivo\\resultados_ceps.xlsx', index=False)

print("ok")
