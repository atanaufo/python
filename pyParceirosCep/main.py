"""
    Código Python que carrega uma tabela CSV, verifica se o campo CEP é válido usando
    a biblioteca pycep-correios e salva os resultados finais em um arquivo XLSX.

    pip install pandas pycep-correios openpyxl

    pip install brazilcep

"""

import pandas as pd
#from pycep_correios import consultar_cep
import brazilcep as consultar_cep
from openpyxl import Workbook

# Carregar o arquivo CSV (substitua 'seu_arquivo.csv' pelo caminho correto)
csv_file = 'C:\\arquivo\\parceiros.csv'
df = pd.read_csv(csv_file)

# Verificar a validade do CEP
def validar_cep(cep):
    try:
        consultar_cep.get_address_from_cep(cep)
        return True
    except:
        return False

# Filtrar os CEPs válidos
df['CEP válido'] = df['CEP'].apply(validar_cep)
ceps_validos = df[df['CEP válido']]

# Salvar os resultados em um arquivo XLSX
#output_file = 'C:\\arquivo\\resultados_ceps.xlsx'
#ceps_validos.to_excel(output_file, index=False)

#print(f"Resultados salvos em {output_file}")
