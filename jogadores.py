from dbm import error
from time import sleep
from art import text2art
import colorama
colorama.init()


def jogador():
    while True:
        try:
            print(colorama.Fore.MAGENTA + "=+" * 21)
            jogadores = int(input('Quantos jogadores irão jogar?: '))
            if jogadores <=1 or jogadores >= 8:
                print('\033[31m>> Erro\nEscolha entre 2 a 7 jogadores \033[m')
                sleep(0.5)
                continue
            elif 1 < jogadores < 8:
                return jogadores
        except ValueError:
                print('\033[31m>> Erro, digite apenas números <<\033[m')
                sleep(0.5)

def quantidade(total):
    jogadores = []
    for i in range(total):

        try :
            cadastro = input(f'{i +1}ª Jogador : ').title().strip()
            while not cadastro:
                print(colorama.Fore.MAGENTA + "=+" * 21)
                sleep(0.5)
                print(f'\033[31m{'>> Erro <<':>13}\n[Adicione um nome]\033[m')
                sleep(1)
                print(colorama.Fore.MAGENTA + "=+" * 21)
                cadastro = input(f'{i + 1}ª Jogador : ').title().strip()
            else:
                jogadores.append(cadastro)

        except ValueError:
            print(f'{'ERRO'}tente novamente')
    return jogadores