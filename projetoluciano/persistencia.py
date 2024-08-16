import sqlite3

#CRIANDO O BANCO DE DADOS

con = sqlite3.connect('cactusbd.bd')

#CRIAÇÃO DO CURSOR

cur = con.cursor()

cur.execute('''
  CREATE TABLE IF NOT EXISTS usuario(
            id TEXT PRIMARY KEY,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            senha TEXT NOT NULL,
            biblioteca TEXT NOT NULL,
            operacoes TEXT NOT NULL,
            carrinho TEXT NOT NULL,
            foto TEXT NOT NULL      )
''')
