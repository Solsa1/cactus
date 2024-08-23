import sqlite3 as lite
from datetime import datetime

#CONEXÃO COM O BANCO DE DADOS
con = lite.connect('cactusbd.bd')

#DEFININDO A FUNÇÃO DE INSERIR DO USUARIO


def inserir_dados_user(i):
    with con:
        cursor = con.cursor()
        comando = 'INSERT INTO usuario(nome, email, senha, foto) VALUES (?,?,?,?)' 
        cursor.execute(comando,i)

#DEFININDO UMA FUNÇÃO PARA VERIFICAÇÃO DE DADO

def verifica(senha, email):
    with con:
        cursor = con.cursor()
        verificacao = "SELECT * FROM usuario WHERE senha = ? and email =?"
        cursor.execute(verificacao, (senha,email, ))
        resultado = cursor.fetchone()
        return resultado

#DEFININDO A FUNÇÃO DE DELETAR DO USUARIO

def deletar_dados_user(i):
    with con:
        cursor = con.cursor()
        comando = 'DELETE FROM usuario WHERE senha =?'
        cursor.execute(comando, (i, ))

#DEFININDO A FUNÇÃO DE ATUALIZAR DO USUARIO

def atualizar_dados_user(i, novo_dado, coluna):
     with con:
        cursor = con.cursor()
        comando = F'UPDATE usuario SET {coluna}=? WHERE senha=?'
        cursor.execute(comando,(novo_dado, i))

#DEFININDO A FUNÇÃO DE VER OS DADOS DO USUÁRIO

def ver_dados_user():
    lista_usuarios = []
    with con:  
        cur = con.cursor()
        cur.execute('SELECT * FROM usuario')
        rows = cur.fetchall()
        for row in rows:
            lista_usuarios.append(row)
        return lista_usuarios