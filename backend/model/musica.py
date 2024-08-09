from SoundRB.backend.model import album

class Musica(album.Album):
    musicas = []
    def __init__(self, nome, lancamento, duracao, genero):
        super().__init__(nome, lancamento, duracao)
        self._genero = genero
        self.musicas.append(self)

    def __str__(self):
        return f'Nome: {self._nome} | Lançamento: {self._lancamento} | Duracao: {self._duracao}'
    
    @classmethod
    def listar_albuns(cls):
        print('-' * 75)
        print(f'{"Nome".ljust(25)} | {"Lançamento".ljust(10)} | Duracao')
        print('-' * 75)

        for album in cls.artistas:
            print(album._nome)
    
    @classmethod
    def encontrar_artista(cls, nome):
        album_encontrado = False
        for artista in cls.artistas:
            if artista._nome == nome:
                album_encontrado = True
                print('Album encontrado!')
        
        if not album_encontrado:
            print('Album não encontrado')