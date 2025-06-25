import pandas as pd
import sqlite3

#CARREGANDO DADOS DO NIVEL PRATA
dadosCompraPrata = pd.read_parquet("C:\\Users\\Caio de Souza\\FACULDADE\\DBA II\\TRABALHO_DL\\aplicacao_datalake\\DATALAKE\\prata\\compras\\dadosComprasPrata.parquet")

#REALIZANDO TRATAMENTO PARA FACILITAR ANALISES FUTURAS

#mudando o tipo da coluna
dadosCompraPrata['dt_compra'] = pd.to_datetime(dadosCompraPrata['dt_compra'])

#coluna com somente o ano
dadosCompraPrata['ano'] = dadosCompraPrata['dt_compra'].dt.year

#coluna com somente o mes
dadosCompraPrata['mes'] = dadosCompraPrata['dt_compra'].dt.month

#adicionando valor de desconto
dadosCompraPrata['vl_desconto'] = dadosCompraPrata['vl_vendido'] * dadosCompraPrata['perc_promocao']
dadosCompraPrata['vl_desconto'] = dadosCompraPrata['vl_desconto'].round(2)

#criando dataframe com dados melhores das vendas
dadosCompraAnalist = dadosCompraPrata.groupby(['ano', 'mes', 'cd_produto']).agg({
    'qtde_vendida' : 'sum',
    'vl_vendido' : 'sum',
    'vl_desconto' : 'sum'
}).reset_index()

print(dadosCompraAnalist)

#colocando os dados obtidos no banco de dados, nivel ouro, em uma tabela especifica
conn = sqlite3.connect('C:\\Users\\Caio de Souza\\FACULDADE\\DBA II\\TRABALHO_DL\\aplicacao_datalake\\DATALAKE\\ouro\\database\\datalake.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS compras (
        ano INTEGER,
        mes INTEGER,
        cd_produto INTEGER,
        qtde_vendida INTEGER,
        vl_vendido REAL,
        vl_desconto REAL
    )
''')

dadosCompraAnalist.to_sql('compras', conn, if_exists='replace', index = False)

