import sqlite3

#CRIANDO O BANCO DE DADOS

con = sqlite3.connect('cactusbd.bd')

#CRIAÇÃO DO CURSOR

cur = con.cursor()

#TABELA DO USUARIO
cur.execute('''
  CREATE TABLE IF NOT EXISTS usuario(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL,
            foto TEXT NOT NULL,
            biblioteca TEXT NULL,
            operacoes TEXT NULL,
            carrinho TEXT NULL    )
''')

#TABELA DA EMPRESA

cur.execute('''
  CREATE TABLE IF NOT EXISTS empresa(
            nome TEXT UNIQUE,
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lucro FLOAT,
            email TEXT NOT NULL,
            senha TEXT NOT NULL,
            devs TEXT,
            jogo TEXT,
            logo TEXT,
            desc TEXT NOT NULL
            )
''')


#TABELA DO DEV

cur.execute('''
  CREATE TABLE IF NOT EXISTS dev(
            nome TEXT NOT NULL,
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_empre INTEGER,
            senha TEXT UNIQUE,
            email TEXT UNIQUE,
            jogos TEXT,
            lucro FLOAT,
            foto TEXT,
            FOREIGN KEY(id_empre) REFERENCES empresa(id)   
  )
''')


#TABELA DOS JOGOS

cur.execute('''
  CREATE TABLE IF NOT EXISTS jogo(
            nome TEXT UNIQUE,
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_empre INTEGER,
            id_dev INTEGER,
            preco FLOAT NOT NULL,
            desc TEXT NOT NULL,
            foto TEXT NOT NULL,
            data_lancamento DATE,
            FOREIGN KEY(id_empre) REFERENCES empresa(id),
            FOREIGN KEY(id_dev) REFERENCES dev(id) 

  )
''')


#TABELA DA BIBLIOTECA

cur.execute('''
  CREATE TABLE IF NOT EXISTS biblioteca(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_jogo INTEGER,
            id_user INTEGER,
            FOREIGN KEY(id_jogo) REFERENCES jogo(id),
            FOREIGN KEY(id_user) REFERENCES usuario(id)
  )
''')


#TABELA DO CARRINHO

cur.execute('''
  CREATE TABLE IF NOT EXISTS carrinho(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_user INTEGER,
            id_jogo INTEGER,
            preco FLOAT NOT NULL,
            FOREIGN KEY(id_jogo) REFERENCES jogo(id),
            FOREIGN KEY(id_user) REFERENCES usuario(id)
  )
''')

#TABELA DE OPERAÇÕES

