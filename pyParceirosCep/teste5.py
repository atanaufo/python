import csv
import json
import pandas as pd
import brazilcep 


# Nome do arquivo CSV de entrada e saída
input_csv_filename = 'C:\\arquivo\\parceiros.csv'
output_xlsx_filename = 'C:\\arquivo\\validacao.xlsx'

# Função para validar o CEP e retornar "válido" ou "inválido"
def validar_cep(cep):
    try:
        brazilcep(cep)
        return "válido"
    except ValueError:
        return "inválido"

# Lê o arquivo CSV delimitado por ';'
with open(input_csv_filename, newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')

    # Cria uma lista para armazenar as linhas com a coluna de validação
    rows_with_validation = []

    for row in reader:
        # Converte a coluna CEP1 para inteiro (se possível)
        try:
            row['CEP'] = int(row['CEP'])
        except ValueError:
            # Se não for possível converter para inteiro, mantém o valor original
            pass

        # Adiciona a coluna de validação
        row['Validação CEP'] = validar_cep(str(row['CEP']))

        # Adiciona a linha à lista
        rows_with_validation.append(row)

# Cria um DataFrame do Pandas com as linhas e colunas
df = pd.DataFrame(rows_with_validation)

print(df)

# Salva o DataFrame em um arquivo XLSX
#df.to_excel(output_xlsx_filename, index=False)

#print(f"Arquivo {output_xlsx_filename} criado com sucesso!")