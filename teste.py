import curses
from time import sleep, perf_counter

class Kernel:
    def __init__(self, tela):
        self.tela = tela
    def d_key(self):
        return self.tela.getkey()
    def draw(self):



def main():
    curses.noecho()
    curses.cbreak()
    tela.clear()

    tela.addstr(5, 10, "Weeeeeeeee")
    st = ['|', '/', '-', '\\']
    i = 0
    x = y = 0
    while True:
        texto = f"Carregando {st[i]}"

        tela.addstr(x, y, texto)
        i += 1
        if i == 4:
            i = 0
        sleep(0.2)

        tela.refresh()


curses.wrapper(main)