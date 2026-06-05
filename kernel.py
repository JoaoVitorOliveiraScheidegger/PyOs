import curses
from time import perf_counter

class Kernel:
    def __init__(self):
        self.hardware = None

    def __enter__(self):
        # Iniciando tela
        self.hardware = curses.initscr()

        # Configurando o terminal
        curses.noecho()
        curses.cbreak()
        self.hardware.keypad(True)
        curses.curs_set(0)

        return self

    def __exit__(self, error_type, value, traceback):
        # Voltar o terminal ao normal
        if self.hardware:
            curses.nocbreak()
            curses.echo()
            self.hardware.keypad(False)
            curses.endwin()

    def start_system(self):
        self.hardware

