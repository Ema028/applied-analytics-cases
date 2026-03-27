import sqlite3
import pandas as pd

df_transacoes = pd.read_csv("tb_transacoes.csv", delimiter=';')
df_clientes = pd.read_csv("tb_clientes.csv", delimiter=';')

conn = sqlite3.connect('projeto.db')
df_transacoes.to_sql('transacoes', conn, index=False, if_exists='replace')
df_clientes.to_sql('clientes', conn, index=False, if_exists='replace')

def run_query(query):
    return pd.read_sql_query(query, conn)

'''
left join foi escolhido para não perder nenhuma transação, mesmo se faltar o cadastro do cliente, 
inner cortaria essas vendas e right traria clientes sem compras
'''
query = "SELECT * FROM transacoes LEFT JOIN clientes ON transacoes.id_client = clientes.Id_client"
df = run_query(query)
df = df.drop(columns=['Id_client'])
print(df)

df.to_csv('dados_ecommerce_final.csv', index=False)