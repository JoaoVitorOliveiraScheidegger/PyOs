import curses
import os
from pynput import keyboard as k



teclas = set()
curses.noecho()

def ao_pressionar(tecla):
    try: nome = tecla.char
    except AttributeError: nome = str(tecla)
    if nome: teclas.add(nome)
    print("oi")

def ao_soltar(tecla):
    try: nome = tecla.char
    except AttributeError: nome = str(tecla)
    if nome in teclas: teclas.remove(nome)

# Inicia o monitoramento
ouvinte = k.Listener(on_press=ao_pressionar, on_release=ao_soltar)
ouvinte.start()

#
# def main(tela):
#     tela.clear()
#
#     tela.addstr(5, 10, "Weeeeeeeee")
#     st = ""
#     while True:
#         s = tela.getkey()
#         print(s)
#         tela.addstr(6, 10, st)
#         tela.refresh()

# curses.wrapper(main)


while True:
    print(f"\rTeclas detectadas em paralelo: {list(teclas)}      ", end="", flush=True)
