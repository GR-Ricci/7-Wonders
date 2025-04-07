import art
from art import text2art
import colorama
colorama.init()
from time import sleep
def mapas(modo,jogadores):
    todososmapas={'1': {'nome':'Básico', 'mapas':
        ['Gizé', 'Babilônia', 'Éfeso', 'Olímpia', 'Halicarnasso', 'Rodes', 'Alexandria']},
        '2': {'nome': 'Lideres', 'mapas': ['COLISEU', 'Abu Simbel']},
        '3': {'nome': 'Edificios', 'mapas': ['Carthage', 'Ur']},
        '4': {'nome': 'Armada', 'mapas': ['Siracusa']},
        '5': {'nome': 'Cidades', 'mapas': ['Petra', 'Bizantium']}}
    #Dicionario manual com subdicionarios, cada chave base tem um dicionario de chaves nome e mapas

    jogadoresquantidade = int(len(jogadores))
    if modo == '1':
        selecionados = ['1','2','3','4','5']
        return selecionados

    if modo == '2':

        selecionados = []
        while True:
            opcoes = {}
            for k, v in todososmapas.items():
                if k not in selecionados:
                    opcoes[k] = v  # o opcoes vai receber todos os mapas que nao esta em selecionados

            linhas_validas = []
            titulo = text2art("MAPAS".center(20), font="braced")
            titulo = titulo.replace('\f', '')
            for v in titulo.split("\n"): #para não comer linha
                if v.strip() != "":
                    linhas_validas.append(v)
            titulo = '\n'.join(linhas_validas)
            print('\n')
            print(colorama.Fore.GREEN + "=+" * 41)
            print(colorama.Fore.BLUE + titulo)
            print(colorama.Fore.GREEN + "=+" * 41)

            for k,v in opcoes.items():
                print(f'\033[34m[{k}] - {v["nome"]} - [\033[31m' +
                        text2art(', '.join(v["mapas"]), font='greek_legends') +
                        '\033[34m]\033[m')
                    # k é a chave inicial, se ela nao estiver em selecionado
                    # o k recebe de todos os mapas, entao printamos a chave e seus dicionarios
            print(f'\033[33m[0] - \033[33mFinalizar\033[m')
            print(colorama.Fore.GREEN + "x" * 82)

            try:
                escolha = input('\033[34mEscolha os mapas: \033[m').strip()

                if escolha in selecionados and escolha not in '0':
                    print(f'\033[31mERRO\nA lista de mapas \033[33m{escolha}\033[31m já foi adicionada')
                    print(colorama.Fore.RED + "=+" * 35)
                    print(f'Carregando...')
                    sleep(1)
                    print('3...', end='')
                    sleep(1)
                    print('2...', end = '')
                    sleep(1)
                    print('1...', end='')
                    sleep(1)
                    continue

                elif escolha not in todososmapas and escolha not in '0':
                    print(colorama.Fore.GREEN + "x" * 82)
                    print('\033[31mERRO\nEscolha os valores atribuidos restantes')
                    print(colorama.Fore.RED + "=+" * 35)
                    print(f'Carregando...')
                    sleep(1)
                    print('3...', end='')
                    sleep(1)
                    print('2...', end='')
                    sleep(1)
                    print('1...', end='')
                    sleep(1)
                    continue

                if not escolha:
                    print(colorama.Fore.GREEN + "x" * 82)
                    print('\033[31mERRO\nEscolha os mapas')
                    print(colorama.Fore.RED + "=+" * 35)
                    print(f'Carregando...')
                    sleep(1)
                    print('3...', end='')
                    sleep(1)
                    print('2...', end='')
                    sleep(1)
                    print('1...', end='')
                    sleep(1)
                    continue

                elif escolha not in selecionados and escolha not in '0':
                    selecionados.append(escolha)

                if not selecionados:
                    print(colorama.Fore.GREEN + "x" * 82)
                    print('\033[31mERRO\nEscolha os mapas')
                    print(colorama.Fore.RED + "=+" * 35)
                    print(f'Carregando...')
                    sleep(1)
                    print('3...', end='')
                    sleep(1)
                    print('2...', end='')
                    sleep(1)
                    print('1...', end='')
                    sleep(1)
                    continue

                if escolha == '0':
                    quantidade = 0
                    for v in selecionados:
                        if '1' in v:
                            quantidade += 7
                        if '2' in v:
                            quantidade += 2
                        if '3' in v:
                            quantidade += 2
                        if '4' in v:
                            quantidade += 1
                        if '5' in v:
                            quantidade += 2

                    if quantidade >= jogadoresquantidade:
                        return selecionados

                    else:
                        print(colorama.Fore.GREEN + "x" * 82)
                        print(f'\033[31mO número de jogadores é maior que a quantidade de mapas\n'
                              f'\033[33m({quantidade}) - mapas // ({jogadoresquantidade}) - jogadores')
                        print(colorama.Fore.RED + "=+" * 35)
                        print(f'Carregando...')
                        sleep(1)
                        print('3...', end='')
                        sleep(1)
                        print('2...', end='')
                        sleep(1)
                        print('1...', end='')
                        sleep(1)

            except ValueError:
                print('Erro')