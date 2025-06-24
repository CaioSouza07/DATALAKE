import pandas as pd

#CARREGAMENDO DOS DADOS
dadosCompras = pd.read_csv("compras\\dadosCompras.csv", sep = ",", encoding="utf-8")


#INICIANDO TRATAMENTO DOS DADOS

#Retirando possiveis duplicatas
dadosCompras = dadosCompras.drop_duplicates()

#Retirando possíveis vendas <= 0
dadosCompras = dadosCompras[dadosCompras['qtde_vendida'] > 0]


#SALVANDO DADOS NIVEL PRATA
dadosCompras.to_parquet("C:\\Users\\1217007457\\aplicacao_datalake\\DATALAKE\\prata\\compras\\dadosComprasPrata.parquet")

