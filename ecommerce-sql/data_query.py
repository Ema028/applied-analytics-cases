import pandas as pd
import sqlite3

df_vendas = pd.read_csv("vendas.csv", delimiter=';')
conn = sqlite3.connect(':memory:')
df_vendas.to_sql('vendas', conn, index=False, if_exists='replace')

def run_query(query):
    return pd.read_sql_query(query, conn)

#todos os dados
query = "SELECT * FROM vendas;"
print(run_query(query))

#10 linhas coluna produto
query = "SELECT produto FROM vendas LIMIT 10;"
print(run_query(query))

#média valor da unidade e unidades vendidas
query = ("SELECT AVG(VALOR_UNID) AS MEDIA_VALOR_UNID,"
         "AVG(UNIDADES) AS MEDIA_UNID_POR_VENDA FROM vendas;")
print(run_query(query))

#não temos valor total por compra, mas tem quantidade vendida e valor do produto
#retornar id compra, id cliente e total gasto
query = ("SELECT ID_COMPRA, ID_CLIENTE, "
         "(VALOR_UNID * UNIDADES) AS VALOR_TOTAL_GASTO FROM vendas;")
print(run_query(query))

'''
Python e SQL se complementam, SQL é padrão para manipular bancos de dados relacionaiis, 
usa para extrair dados de bancos e preparar uma base limpa para análise e Python para limpar, analisar, manipular e visualizar esses dados

Os conjuntos de dados que são relacionais têm relações pré-definidas entre eles, da mesma forma,
bancos de dados relacionais armazenam e organizam pontos de dados com relacionamentos definidos para acesso rápido
e bancos de dados não relacionais, são sistemas de armazenamento de dados que não utilizam o modelo tradicional de tabelas, linhas e colunas

Para consultas rápidas, o SQL é muito mais prático e eficiente que o Python, especialmente quando os dados já estão estruturados, porque
no Python você precisa configurar um ambiente, importar bibliotecas, estabelecer uma conexão e carregar os dados para a memória,
mas no SQL você executa uma única instrução que filtra e agrega milhões de linhas diretamente no motor do banco.
'''
