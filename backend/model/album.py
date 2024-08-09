from SoundRB.backend.model import artista

class Album(artista.Artista):
    albuns = []
    def __init__(self, nome, lancamento, duracao):
        self._nome = nome
        self._lancamento = lancamento
        self._duracao = duracao #soma da duração das músicas
        self.albuns.append(self)

    def __str__(self):
        return f'Nome: {self._nome} | Lançamento: {self._lancamento} | Duracao: {self._duracao}'
    
    @classmethod
    def listar_albuns(cls):
        print('-' * 75)
        print(f'{"Nome".ljust(25)} | {"Lançamento".ljust(10)} | Duracao')
        print('-' * 75)

        for album in cls.albuns:
            print(album._nome)
    
    @classmethod
    def encontrar_album(cls, nome):
        album_encontrado = False
        for album in cls.albuns:
            if album._nome == nome:
                album_encontrado = True
                print('Album encontrado!')
        
        if not album_encontrado:
            print('Album não encontrado')
            
