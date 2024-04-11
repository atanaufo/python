import pandas as pd

# Especifique o caminho absoluto do arquivo CSV
caminho_absoluto = 'C:\\arquivo\\parceiros.csv'

# Carregue o arquivo CSV
df = pd.read_csv(caminho_absoluto)

# Agora você pode usar o DataFrame 'df' para manipular os dados
print(df.head())  # Exemplo: exibe as primeiras linhas do DataFrame
