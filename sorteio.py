from random import sample, randint
import colorama
from art import text2art

def menusorteio():
    print('\n' * 15)
    print(colorama.Fore.MAGENTA + "=+" * 21)
    titulo = text2art(" Maravilhas", font="tarty2")
    linhas_validas = []
    for v in titulo.split("\n"):
        if v.strip() != "":
            linhas_validas.append(v)
    titulo = "\n".join(linhas_validas)
    print(colorama.Fore.RED + titulo)
    print(colorama.Fore.MAGENTA + "=+" * 21)

def sorteio(selecionados,jogadores):
    listafinal = []
    todososmapas = {'1': {'nome': 'Básico', 'mapas':
        ['Gizé', 'Babilônia', 'Éfeso', 'Olímpia', 'Halicarnasso', 'Rodes', 'Alexandria']},
                    '2': {'nome': 'Lideres', 'mapas': ['COLISEU', 'Abu Simbel']},
                    '3': {'nome': 'Edificios', 'mapas': ['Carthage', 'Ur']},
                    '4': {'nome': 'Armada', 'mapas': ['Siracusa']},
                    '5': {'nome': 'Cidades', 'mapas': ['Petra', 'Bizantium']}}

    for k, v in todososmapas.items():
        if k in selecionados: #se tiver a chave no selecionados ele pega o valor dessa chave
            listafinal.extend(v['mapas'])           #em todososmapas e joga para listafinal

    slistafinal = sample(listafinal, len(jogadores)) ##Fora do loop para n repetir numeros
    navio = sample(range(1, 8), len(jogadores))
    menusorteio()

    if not '4' in selecionados:
        for i, v in enumerate(jogadores):
            sample(listafinal, len(jogadores))
            print(colorama.Fore.YELLOW + f'O jogador {colorama.Fore.RED + v}'
                  , colorama.Fore.YELLOW + f'ficou com {colorama.Fore.CYAN + listafinal[i]}')
            print(colorama.Fore.MAGENTA + "=+" * 21)

    if '4' in selecionados:
        for i, v in enumerate(jogadores):
            print(colorama.Fore.YELLOW + f' O jogador {colorama.Fore.RED + v}'
                  ,colorama.Fore.YELLOW + f'ficou com {colorama.Fore.CYAN + listafinal[i]}\n'
                  ,colorama.Fore.YELLOW +f'E recebeu o',colorama.Fore.CYAN + f'Navio {navio[i]}')
            print(colorama.Fore.MAGENTA + "=+" * 21)