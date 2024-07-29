import os
import sqlite3
from time import sleep
from modelos.album import Album
from modelos.artista import Artista

artista1 = Artista('Marco Telles', 'Brasileira', 45)
artista2 = Artista('Lecrae', 'Americana', 44)
artista3 = Artista('Midian Nascimento', 'Brasileira', 37)

def nome_do_aplicativo():
  print('''
░██████╗░█████╗░██╗░░░██╗███╗░░██╗██████╗░██████╗░██████╗░
██╔════╝██╔══██╗██║░░░██║████╗░██║██╔══██╗██╔══██╗██╔══██╗
╚█████╗░██║░░██║██║░░░██║██╔██╗██║██║░░██║██████╔╝██████╦╝
░╚═══██╗██║░░██║██║░░░██║██║╚████║██║░░██║██╔══██╗██╔══██╗
██████╔╝╚█████╔╝╚██████╔╝██║░╚███║██████╔╝██║░░██║██████╦╝
╚═════╝░░╚════╝░░╚═════╝░╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝╚═════╝░\n''')

def opcao_invalida():
  print('Opção inválida!')
  sleep(2)
  main()

def sair_do_aplicativo():
  print('Bye bye!')

def voltar_ao_menu_principal():
  input('Pressione qualquer tecla para voltar ao inicio: ')
  main()

def cadastrar_artista():
  nome = input('Digite o nome do artista: ')
  nacionalidade = input('Digite a nacionalidade do artista: ')
  idade = int(input('Digite a idade do artista: '))
  dados_artista = Artista(nome, nacionalidade, idade)
  print(f'Artista {nome} cadastrado com sucesso!')
  
  #cadastrar no arquivo de banco de dados
  voltar_ao_menu_principal()

def listar_artistas():
  Artista.listar_artistas()
  voltar_ao_menu_principal()

def encontrar_artista():
  nome = str(input('Digite o nome do artista: '))
  resultado = Artista.encontrar_artista(nome)
  print(resultado)
  voltar_ao_menu_principal()

def opcoes_do_menu():
  print('1 - Cadastrar Artista')
  print('2 - Procurar Artista')
  print('3 - Listar Artistas')
  print('4 - Sair\n')
  
def opcao_escolhida():
  try:
    escolha = int(input('Digite a opção desejada: '))
    match escolha:
      case 1:
        cadastrar_artista()
      case 2: 
        encontrar_artista()
      case 3:
        listar_artistas()
      case 4:
        sair_do_aplicativo()
      case _:
        opcao_invalida()
  except Exception as e:
    print(f'O erro é {e}')

def main():
  os.system('clear')
  nome_do_aplicativo()
  opcoes_do_menu()
  opcao_escolhida()

if __name__ == '__main__':
  main()
