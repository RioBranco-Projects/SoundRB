import os
from backend.model.artista import Artista

def exibir_logo():
    print('''
░██████╗░█████╗░██╗░░░██╗███╗░░██╗██████╗░██████╗░██████╗░
██╔════╝██╔══██╗██║░░░██║████╗░██║██╔══██╗██╔══██╗██╔══██╗
╚█████╗░██║░░██║██║░░░██║██╔██╗██║██║░░██║██████╔╝██████╦╝
░╚═══██╗██║░░██║██║░░░██║██║╚████║██║░░██║██╔══██╗██╔══██╗
██████╔╝╚█████╔╝╚██████╔╝██║░╚███║██████╔╝██║░░██║██████╦╝
╚═════╝░░╚════╝░░╚═════╝░╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝╚═════╝░\n''')

def voltar_ao_menu_principal():
    print()
    input('Pressione entre para voltar ao menu principal ')
    main()

def opcao_invalida():
    print('Opção inválida')
    voltar_ao_menu_principal()

def subtitulo(txt):
    os.system('cls' if os.name == 'nt' else 'clear')
    asteriscos = '*' * (len(txt) + 4)
    print(asteriscos)
    print(f'  {txt}  ')
    print(asteriscos)
    print()

def cadastrar_artista():
    subtitulo('Cadastrar Artista')

    nome = str(input('Digite o nome do artista: '))
    idade = str(input(f'Digite a idade do {nome}: '))
    nacionalidade = str(input(f'Digite a nacionalidade do {nome}: '))
    artista = Artista(nome, idade, nacionalidade)
    print(f'Artista {nome} cadastrado com sucesso!')
    
    voltar_ao_menu_principal()

def listar_artistas():
    subtitulo('Listando Artistas')
    Artista.listar_artistas()
    voltar_ao_menu_principal()

def buscar_artista():
    subtitulo('Pesquisar Artista')
    nome = str(input('Digite o nome do artista que deseja pesquisar: '))
    print()
    Artista.encontrar_artista(nome)

    voltar_ao_menu_principal()

def deletar_artista():
    subtitulo('Deletar Artista')
    nome = str(input('Digite o nome do artista que deseja deletar: '))
    print()
    Artista.deletar_artista(nome)

    voltar_ao_menu_principal()

def opcoes_do_menu():
    print('1. Cadastrar artista')
    print('2. Listar artistas cadastrados')
    print('3. Buscar artista')
    print('4. Deletar artista')
    print('5. Sair\n')

def opcao_escolhida_pelo_usuario():
    opcao_escolhida = int(input('Digite a opção escolhida: '))
    try:
        match opcao_escolhida:
            case 1: cadastrar_artista()
            case 2: listar_artistas()
            case 3: buscar_artista()
            case 4: deletar_artista()
            case 5: print('Saindo do aplicativo...')
            case _: opcao_invalida()
    except Exception as e:
        print(f'{e}')

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    exibir_logo()
    opcoes_do_menu()
    opcao_escolhida_pelo_usuario()

if __name__ == '__main__':
    main()
