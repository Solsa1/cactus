import sqlite3 as lite
from datetime import datetime

#CONEXÃO COM O BANCO DE DADOS
con = lite.connect('cactusbd.bd')

#DEFININDO A FUNÇÃO DE INSERIR 

def inserir_dados(i):
    cursor = con.cursor()
    josefina = 'INSERT INTO usuario(id, nome, email, senha, biblioteca, operacoes, carrinho, foto) VALUES (?,?,?,?,?,?,?,?)' 
    cursor.execute(josefina,i)

def 