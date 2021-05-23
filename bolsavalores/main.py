#pip install pandas
#pip install yfinance
#pip install psycopg2-binary
#pip install sqlalchemy

import pandas as pd
import numpy as np
import yfinance as yf
import sqlalchemy

from sqlalchemy import create_engine
    
def get_ibov_info():
            url = "http://bvmf.bmfbovespa.com.br/indices/ResumoCarteiraTeorica.aspx?Indice=IBOV&amp;idioma=pt-br"
            html = pd.read_html(url, decimal=",", thousands=".")[0][:-1]
            df = html.copy()[['Código', 'Ação', 'Tipo']]
            df.rename(columns={
                'Código': 'symbol',
                'Ação': 'name',
                'Tipo': 'type'
            }, inplace=True)
            return df

asset = get_ibov_info()
asset['yf_symbol'] = asset['symbol'] + '.SA'
asset

# Conceito de upsert (update + insert)
# Inserção ou Update dos dados no banco:

insert_initial = """ 
INSERT INTO ASSET (SYMBOL,NAME,TYPE,YF_SYMBOL)
VALUES
"""

values = ",".join([
    "('{}', '{}', '{}', '{}')"
        .format(row["symbol"], row["name"], row["type"], row["yf_symbol"]) 
        for symbol, row in asset.iterrows()
])

insert_end = """
    ON CONFLICT (symbol) DO UPDATE 
    SET
    symbol = EXCLUDED.symbol,
    name = EXCLUDED.name,
    type = EXCLUDED.type,
    yf_symbol = EXCLUDED.yf_symbol;
"""

query = insert_initial + values + insert_end

print(query)

# Estabelecer conexão com o banco de dados remoto:
#engine = create_engine('postgresql+psycopg2://user:password@hostname/database_name')

DB_ADDRESS =  ('postgresql+psycopg2://wrtnysexmrthqb:851a8b938d5acec08a3c65b5ac635884f31abad4e423cf1efc873eef95b676d1@ec2-52-87-107-83.compute-1.amazonaws.com/dcfg4vj1u33rt4')
engine = create_engine(DB_ADDRESS)
engine.execute(query)

# Populando a tabela: asset_portfolio, neste caso iremos utilizar o PANDAS:

asset_sql = pd.read_sql('asset',engine,columns=['id','symbol'])
asset_sql

# Como nosso banco de dados só contém os ativos do IBOV, podemos transformar 
# asset_sql no dataframe contendo os registros da carteira Ibovespa:

portfolio_ibov = asset_sql.copy()[["id"]]
portfolio_ibov.rename(columns={'id': 'asset_id'}, inplace=True)
portfolio_ibov

# O próximo passo é popular a coluna com os IDs das carteiras.
# Faremos isso de forma análoga, importando a tabela portfolio em um dataframe portfolio_sql.

portfolio_sql = pd.read_sql('portfolio', engine)
portfolio_sql

# Como portfolio_ibov contém apenas os ativos que compõem o Ibovespa, 
# vamos estabelecer uma condição para isolar o ID dessa carteira e designá-la à coluna portfolio_id.

portfolio_ibov["portfolio_id"] = int(portfolio_sql.loc[portfolio_sql["name"] == "IBOV", 'id'])
portfolio_ibov

# Prontinho! Nosso dataframe com os IDs relacionados à carteira do Ibovespa está pronto.

# Agora vamos montar uma carteira do QuantBrasil com os 
# seguintes ativos (aleatoriamente escolhidos): "ELET3", "JHSF3", "MGLU3", "PETR4" e "VALE3".

# Criando novo dataframe: portfolio_quantbr

condition = asset_sql["symbol"].isin(["ELET3", "JHSF3", "MGLU3", "PETR4", "VALE3"])

portfolio_quantbr = asset_sql[condition].copy()
portfolio_quantbr.rename(columns={ 'id': 'asset_id'}, inplace=True)
portfolio_quantbr.drop('symbol', axis=1, inplace = True) 
portfolio_quantbr

# Condição para isolar o ID da carteira QuantBrasil e atribuí-la à coluna portfolio_id.

portfolio_quantbr["portfolio_id"] = int(
    portfolio_sql.loc[portfolio_sql["name"] == "QuantBrasil", 'id']
)
portfolio_quantbr

# Finalmente, basta juntar ambos dataframes (portfolio_ibov e portfolio_quantbr) 
# através da função pd.concat() e voilá: nossa tabela asset_portfolio está completa!

asset_portfolio = pd.concat([portfolio_ibov, portfolio_quantbr], ignore_index=False)
asset_portfolio


# O código a seguir segue a mesma estrutura da query upsert que escrevemos anteriormente.

insert_init = """
    INSERT INTO asset_portfolio (asset_id, portfolio_id)
    VALUES
"""

values = ",".join(["('{}', '{}')"
        .format(row["asset_id"], row["portfolio_id"]) 
    for asset_id, row in asset_portfolio.iterrows()
])

insert_end = """
    ON CONFLICT (asset_id, portfolio_id) DO UPDATE 
    SET
    asset_id = EXCLUDED.asset_id,
    portfolio_id = EXCLUDED.portfolio_id;
"""

query = insert_init + values + insert_end

engine.execute(query)
