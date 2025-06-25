import pandas as pd
import sqlite3

conn = sqlite3.connect('C:\\Users\\Caio de Souza\\FACULDADE\\DBA II\\TRABALHO_DL\\aplicacao_datalake\\DATALAKE\\ouro\\database\\datalake.db')

cursor = conn.cursor()

dataframe = pd.read_excel('C:\\Users\\Caio de Souza\\ARQUIVOS CAIO\\produtos.xlsx')


cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
        cd_produto INTEGER,
        desc_produto TEXT,
        categoria TEXT,
        fornecedor TEXT)
               """)

dataframe.to_sql('produtos', conn, if_exists='replace', index=False)

conn.commit()
conn.close()