import pandas as pd
import random
from datetime import datetime, timedelta

# Função para gerar nomes fictícios
def gerar_nome():
    nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Juliana"]
    sobrenomes = ["Silva", "Souza", "Oliveira", "Pereira", "Lima", "Costa", "Almeida", "Ferreira", "Ribeiro", "Martins"]
    return f"{random.choice(nomes)} {random.choice(sobrenomes)}"

# Geração de dados
num_compras = 5000
itens_por_compra = [1, 2, 3]
compras = []

for id_compra in range(1, num_compras + 1):
    dt = datetime(2024, 1, 1) + timedelta(days=random.randint(0, 180))
    cli
