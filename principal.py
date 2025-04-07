from menu import menu, menumapa
from jogadores import jogador, quantidade
from mapas import mapas
from sorteio import sorteio
from art import text2art
import colorama
colorama.init()

inicia = menu()
if inicia:
    total = jogador()
    jogadores =quantidade(total)
    modo = menumapa()
    selecionados = mapas(modo,jogadores)
    sorteio(selecionados,jogadores)