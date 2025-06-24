import pandas as pd
import sqlite3

#CARREGANDO DADOS DO NIVEL PRATA
dadosCompraPrata = pd.read_parquet("compras\\dadosComprasPrata.parquet")

#REALIZANDO TRATAMENTO PARA FACILITAR ANALISES FUTURAS

#mudando o tipo da coluna
dadosCompraPrata['dt_compra'] = pd.to_datetime(dadosCompraPrata['dt_compra'])

#coluna com somente o ano
dadosCompraPrata['ano'] = dadosCompraPrata['dt_compra'].dt.year

#coluna com somente o mes
dadosCompraPrata['mes'] = dadosCompraPrata['dt_compra'].dt.month

print(dadosCompraPrata)