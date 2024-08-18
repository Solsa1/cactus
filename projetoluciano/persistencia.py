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
            senha TEXT NOT NULL UNIQUE,
            biblioteca TEXT NOT NULL,
            operacoes TEXT NOT NULL,
            carrinho TEXT NOT NULL,
            foto TEXT NOT NULL      )
''')

#TABELA DA EMPRESA

cur.execute('''
  CREATE TABLE IF NOT EXISTS empresa(
            nome TEXT UNIQUE,
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lucro FLOAT,
            senha TEXT NOT NULL UNIQUE,
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
            id INTEGER AUTOINCREMENT,
            id_empre INTEGER,
            PRIMARY KEY(id, id_empre),
            senha TEXT UNIQUE,
            email TEXT UNIQUE,
            jogos TEXT,
            lucro FLOAT,
            FOREIGN KEY(id_empre) REFERENCES empresa(id)   
  )
''')

#TABELA DOS JOGOS

cur.execute('''
  CREATE TABLE IF NOT EXISTS jogo(
            nome TEXT UNIQUE,
            id INTEGER AUTOINCREMENT,
            id_empre INTEGER,
            id_dev INTEGER,
            preco FLOAT NOT NULL,
            desc TEXT NOT NULL,
            foto TEXT NOT NULL,
            data_lancamento DATE,
            PRIMARY KEY(id_empre,id,id_dev),
            FOREIGN KEY(id_empre) REFERENCES empresa(id),
            FOREIGN KEY(id_dev) REFERENCES dev(id) 

  )
''')

#TABELA DA BIBLIOTECA

cur.execute('''
  CREATE TABLE IF NOT EXISTS biblioteca(
            id INTEGER AUTOINCREMENT,
            id_jogo INTEGER,
            id_user INTEGER,
            PRIMARY KEY(id,id_jogo,id_user)
            FOREIGN KEY(id_jogo) REFERENCES jogo(id),
            FOREIGN KEY(id_user) REFERENCES usuario(id)
  )
''')

#TABELA DO CARRINHO

cur.execute('''
  CREATE TABLE IF NOT EXISTS carrinho(
            id INTEGER AUTOINCREMENT,
            id_user INTEGER,
            id_jogo INTEGER,
            preco FLOAT NOT NULL,
            PRIMARY KEY(id,id_user,id_jogo),
            FOREIGN KEY(id_jogo) REFERENCES jogo(id),
            FOREIGN KEY(id_user) REFERENCES usuario(id)
  )
''')

#TABELA DAS OPERAÇÕES

cur.execute('''
  CREATE TABLE IF NOT EXISTS operacoes(
            id INTEGER AUTOINCREMENT, 
            id_user INTEGER,
            id_empre INTEGER,
            preco FLOAT NOT NULL,
            tipo TEXT NOT NULL,
            PRIMARY KEY(id, id_user, id_empre),
            FOREIGN KEY(id_user) REFERENCES usuario(id),
            FOREIGN KEY(id_empre) REFERENCES empresa(id)
  )
''')

