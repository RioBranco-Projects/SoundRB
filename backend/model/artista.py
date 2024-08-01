import sqlite3

class Artista:
    artistas = []

    def __init__(self, nome, idade, nacionalidade):
        self._nome = nome
        self._idade = idade
        self._nacionalidade = nacionalidade
        self._disponivel = False
        self.artistas.append(self)
        self.salvar_no_banco()

    def salvar_no_banco(self):
        conn = sqlite3.connect("db/artistas.db")
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO Artista (nome, idade, nacionalidade, disponivel)
        VALUES (?, ?, ?, ?)
        ''', (self._nome, self._idade, self._nacionalidade, self._disponivel))
        conn.commit()
        conn.close()

    def __str__(self):
        return f'Nome: {self._nome} | Idade: {self._idade} | Nacionalidade: {self._nacionalidade} | Status: {self.disponivel}'
    
    @property
    def disponivel(self):
        return '✅' if self._disponivel else '❎'

    @classmethod
    def listar_artistas(cls):
        conn = sqlite3.connect('db/artistas.db')
        cursor = conn.cursor()
        cursor.execute('SELECT nome, idade, nacionalidade, disponivel FROM Artista')
        rows = cursor.fetchall()
        conn.close()
        
        print('-' * 75)
        print(f'{"Nome".ljust(25)} | {"Idade".ljust(10)} | {"Nacionalidade".ljust(25)} | Status')
        print('-' * 75)
        for row in rows:
            nome, idade, nacionalidade, disponivel = row
            status = '✅' if disponivel else '❎'
            print(f'{nome.ljust(25)} | {str(idade).ljust(10)} | {nacionalidade.ljust(25)} | {status}')
        print('-' * 75)

    @classmethod
    def encontrar_artista(cls, nome):
        conn = sqlite3.connect('db/artistas.db')
        cursor = conn.cursor()
        cursor.execute('SELECT nome, idade, nacionalidade, disponivel FROM Artista WHERE nome = ?', (nome,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            nome, idade, nacionalidade, disponivel = row
            status = '✅' if disponivel else '❎'
            print(f'Nome: {nome} | Idade: {idade} | Nacionalidade: {nacionalidade} | Status: {status}')
        else:
            print('Artista não encontrado')
    @classmethod
    def deletar_artista(cls, nome):
        conn = sqlite3.connect('db/artistas.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Artista WHERE nome = ?', (nome,))
        conn.commit()
        rows_affected = cursor.rowcount
        conn.close()

        if rows_affected > 0:
            print(f'Artista {nome} deletado com sucesso!')
            # Remover da lista em memória também
            cls.artistas = [artista for artista in cls.artistas if artista._nome != nome]
        else:
            print('Artista não encontrado ou erro ao deletar')
