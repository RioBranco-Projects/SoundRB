import sqlite3

# Criando conexão com o banco de dados e verificando a conexão
conex = sqlite3.connect("databank/databank.json")

try: 
  conex = sqlite3.connect("databank/databank.json")
  print("Conexão com o banco de dados realizada com sucesso!")
except sqlite3.Error as e:
  print(f'Erro ao conectar ao banco de dados: {e}')
  
try:
 with conex:
  Artista = conex.cursor()
  Artista.execute('''CREATE TABLE IF NOT EXISTS artista''')
  print('Tabela de clientes criada com sucesso!')
except sqlite3.Error as e:
  print(f'Erro {e}')