import sqlite3
conex = sqlite3.connect("databank.db")

try: 
  conex = sqlite3.connect("databank.db")
  print("Conexão com o banco de dados realizada com sucesso!")
except sqlite3.Error as e:
  print(f'Erro ao conectar ao banco de dados: {e}')
  
try:
  artista = conex.cursor()
  artista.execute('''
    CREATE TABLE IF NOT EXISTS artista (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
    )
  ''')
  print("Tabela artista criada com sucesso!")
except sqlite3.Error as e:
  print(f'Erro ao criar a tabela artista: {e}')