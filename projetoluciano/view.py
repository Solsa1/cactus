import sqlite3 as lite
from datetime import datetime

#CONEXÃO COM O BANCO DE DADOS
con = lite.connect('cactusbd.bd')

#DEFININDO A FUNÇÃO DE INSERIR DO USUARIO

def inserir_dados_user(i):
    cursor = con.cursor()
    comando = 'INSERT INTO usuario(id, nome, email, senha, biblioteca, operacoes, carrinho, foto) VALUES (?,?,?,?,?,?,?,?)' 
    cursor.execute(comando,i)

#DEFININDO A FUNÇÃO DE DELETAR DO USUARIO

def deletar_dados_user(i):
    cursor = con.cursor()
    comando = 'DELETE  FROM usuario WHERE id =?'
    cursor.execute(comando, i)

#DEFININDO A FUNÇÃO DE ATUALIZAR DO USUARIO

def atualizar_dados_user(i):
     cursor = con.cursor()
     comando = 'UPDATE usuario SET nome=?, email=?, senha=?, foto=? WHERE id=?'
     cursor.execute(comando,i)

#DEFININDO A FUNÇÃO DE VER OS DADOS DO USUÁRIO

def ver_dados_user(i):
    cursor = con.cursor()
    comando = 'SELECT * FROM usuario WHERE id=?'
    cursor.execute(comando,i)
