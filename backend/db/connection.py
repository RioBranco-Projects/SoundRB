import sqlite3
import os

# Certifique-se de que a pasta 'db' exista
if not os.path.exists('db'):
    os.makedirs('db')

# Conectar ao banco de dados
try:
    conn = sqlite3.connect("db/artistas.db")
    print('Conexão com o banco de dados realizada com sucesso!')
except sqlite3.Error as e:
    print(f'Erro ao conectar ao banco de dados: {e}')

# Criar a tabela Artista
try:
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Artista (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        nacionalidade TEXT NOT NULL,
        disponivel INTEGER NOT NULL
    )
    ''')
    print('Tabela Artista criada com sucesso!')
except sqlite3.Error as e:
    print(f'Erro ao criar a tabela Artista: {e}')

conn.commit()
conn.close()
