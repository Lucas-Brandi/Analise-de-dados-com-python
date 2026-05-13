""" 
Analisar as vendas de produtos de uma empresa
utlizar display somente quando for para exibir as tabelas no notebook (funciona melhor com jupyter notebook)
"""
import pandas as pd
from IPython.display import display
tabela = pd.read_excel('vendas_ficticio.xlsx')
faturamento_por_produto = tabela[['ID Loja', 'Produto', 'Valor Final']].groupby(['ID Loja', 'Produto']).sum()['Valor Final']
print(faturamento_por_produto)



