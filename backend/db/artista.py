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
        for artista in cls.artistas:
            print(f'Nome: {artista._nome}') 