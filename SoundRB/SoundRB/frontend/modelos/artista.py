
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
    print('-' * 50)
    print(f'{"Nome".ljust(30)} | {"Nacionalidade".ljust(30)} | Idade')
    print('-' * 50)
    for artista in cls.artistas:
      print(f'{artista.nome.ljust(30)} | {artista.nacionalidade.ljust(30)} |{artista.idade}')
    print('-' * 50)

  @classmethod
  def encontrar_artista(cls, nome):
    for artista in cls.artistas:
      if artista.nome == nome:
        return f'Artista {artista.nome} encontrado!'
    return f'Artista {nome} não cadastrado!'
    
  @property
  def nome(self):
    return self._nome

  @property
  def nacionalidade(self):
    return self._nacionalidade

  @property
  def idade(self):
    return self._idade