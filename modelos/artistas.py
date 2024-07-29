class Artista:
  artistas = []
  
  def __init__(self, nome, nacionalidade, idade):
    self._nome = nome
    self._nacionalidade = nacionalidade
    self._idade = idade
    Artista.artistas.append(self)

  def __str__(self):
    return f'Nome: {self._nome}, Nacionalidade: {self._nacionalidade}, Idade: {self._idade}'
    
  @classmethod
  def listar_artistas(cls):
    print('-' * 71)
    print(f'{"Nome".ljust(30)} | {"Nacionalidade".ljust(30)} | Idade')
    print('-' * 71)
    for artista in cls.artistas:
      print(f'{artista._nome.ljust(30)} | {artista._nacionalidade.ljust(30)} | {artista._idade}')
    print('-' * 71)

  @classmethod
  def encontrar_artista(cls, nome):
    for artista in cls.artistas:
      if artista._nome == nome:
        return f'Artista {artista._nome} encontrado!'
    return f'Artista {nome} não cadastrado!'