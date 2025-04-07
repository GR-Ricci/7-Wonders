from art import text2art
import colorama
colorama.init()
from time import sleep

def menu():
    while True:
        titulo = text2art("7 Wonders".center(20), font="digital")
        linhas_validas = []
        for v in titulo.split("\n"):
            if v.strip() != "":
                linhas_validas.append(v)
        titulo = "\n".join(linhas_validas)
        print(colorama.Fore.BLUE + '-' * 40)
        print(colorama.Fore.BLUE + titulo)
        print(colorama.Style.BRIGHT + colorama.Fore.RED + text2art("[1] INICIAR".center(32), font="awesome"))
        print(colorama.Style.BRIGHT + colorama.Fore.RED + text2art("[2] SAIR".center(27), font="awesome"))

        escolha = input(f'{' '*10}{'>>'} ').strip()
        if escolha == '1':
            return True
        elif escolha == '2':
            break
        else:
            print('Erro\nDigite [1] para iniciar ou [2] para sair')
            sleep(1)
            print(colorama.Fore.BLUE + '-'*40)
            sleep(0.5)
            print(colorama.Fore.BLUE + '>> Carregando...'.center(35))
            sleep(2)

def menumapa():
    while True:
        titulo = text2art("MAPAS", font="braced")
        linhas_validas = []
        for v in titulo.split("\n"):
            if v.strip() != "":
                linhas_validas.append(v)
        titulo = "\n".join(linhas_validas)
        print(colorama.Fore.GREEN + "=+"*21)
        print(colorama.Fore.BLUE + titulo)
        print(colorama.Fore.GREEN + "=+" * 21)
        print(colorama.Fore.RED + text2art("ESCOLHA O MODO DE JOGO".center(35), font="awesome"))
        print(colorama.Fore.BLUE + text2art('[1] JOGO COMPLETO'.center(35), font ='awesome'))
        print(colorama.Fore.BLUE + text2art('[2] ESCOLHER MODOS'.center(35), font ='awesome'))

        try:
            modo = input(f'{'>> ':>10}')
            if modo == '1':
                return modo
            elif modo == '2':
                return modo
            else:
                print(colorama.Fore.GREEN + "x" * 40)
                print(f'{'\033[31m>>ERRO<<':>23}\n{'Digite [1] Para o jogo completo':>36}'
                      f'\n{'Digite [2] Para personalizar':>33}')
                sleep(1)
                print('>>Carregando...')
                sleep(2)

        except ValueError:
            print('Erro\nDigite [1] Para o jogo completo\nDigite [2] Para personalizar')
            sleep(1)
            print('Carregando...')
            sleep(1)