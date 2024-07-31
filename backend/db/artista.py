class Artista:
    artistas = []
    def __init__(self, nome, idade, nacionalidade):
        self._nome = nome
        self._idade = idade
        self._nacionalidade = nacionalidade
        self._disponivel = False
        self.artistas.append(self)

    def __str__(self):
        return f'Nome: {self._nome} | Idade: {self._idade} | Nacionalidade: {self._nacionalidade} | Status: {self.disponivel}'
    
    @property
    def disponivel(self):
        return '✅' if self._disponivel else '❎'

    @classmethod
    def listar_artista(cls):
        print('-' * 75)
        print(f'{"Nome".ljust(25)} | {"Idade".ljust(10)} | {"Nacionalidade".ljust(25)} | Status')
        print('-' * 75)
        for artista in cls.artistas:
            print(f'{artista._nome.ljust(25)} | {str(artista._idade).ljust(10)} | {artista._nacionalidade.ljust(25)} | {artista.disponivel}')
        print('-' * 75)