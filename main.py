import os
from backend.db.corpo import *
from backend.db.artista import Artista

def exibir_logo():
    print('''
░██████╗░█████╗░██╗░░░██╗███╗░░██╗██████╗░██████╗░██████╗░
██╔════╝██╔══██╗██║░░░██║████╗░██║██╔══██╗██╔══██╗██╔══██╗
╚█████╗░██║░░██║██║░░░██║██╔██╗██║██║░░██║██████╔╝██████╦╝
░╚═══██╗██║░░██║██║░░░██║██║╚████║██║░░██║██╔══██╗██╔══██╗
██████╔╝╚█████╔╝╚██████╔╝██║░╚███║██████╔╝██║░░██║██████╦╝
╚═════╝░░╚════╝░░╚═════╝░╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝╚═════╝░\n''')

def voltar_ao_menu_principal():
    os.system('cls')
    print()
    input('Pressione entre para voltar ao menu principal ')
    main()

def opcao_invalida():
    print('Opção inválida')
    voltar_ao_menu_principal()

def cadastrar_artista():
    nome = str(input('Digite o nome do artista: '))
    idade = str(input(f'Digite a idade do {nome}: '))
    nacionalidade = str(input(f'Digite a nacionalidade do {nome}: '))
    artista = Artista(nome, idade, nacionalidade)

def listar_artistas():
    Artista.listar_artista()

def opcoes_do_menu():
    print('1. Cadastrar artista')
    print('2. Listar artistas cadastrados')
    print('3. Buscar artista')
    print('4. Sair\n')

def opcao_escolhida_pelo_usuario():
    opcao_escolhida = int(input('Digite a opção escolhida: '))
    try:
        match opcao_escolhida:
            case 1: cadastrar_artista()
            case 2: listar_artistas()
            case 3: print('buscar_artista()')
            case 4: print('sair_do_aplicativo()')
            case _: opcao_invalida()
    except Exception as e:
        print(f'{e}')

# artista1 = Artista('Marco Telles', 35, 'Brasileiro')

def main():
    os.system('cls')
    exibir_logo()
    opcoes_do_menu()
    opcao_escolhida_pelo_usuario()


if __name__ == '__main__':
    main()