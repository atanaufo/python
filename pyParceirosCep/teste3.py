import brazilcep
import brazilcep.exceptions
import pandas as pd

# Substitua 'seu_arquivo.csv' pelo caminho do seu arquivo CSV
arquivo_csv = 'C:\\arquivo\\parceiros.csv'
df = pd.read_csv(arquivo_csv, delimiter=';')

def validar_cep(CEP):
    try:
        address = brazilcep.get_address_from_cep(CEP)
        return True  # O CEP é válido
    except:
   # except brazilcep.exceptions.InvalidCEPError:
        return False  # O CEP é inválido


# Aplicar a função de validação ao DataFrame
df['CEP válido'] = df['CEP'].apply(validar_cep)

print(df)





# Crie um DataFrame com os resultados
#df = pd.DataFrame(resultados)

# Salve o DataFrame em um arquivo XLSX
#df.to_excel('C:\\arquivo\\resultados_ceps.xlsx', index=False)
