import curses
from typing import Tuple

class Window:
    def __init__(self, height: int, width: int, x: int, y: int) -> None:
        self.screen = curses.newwin(height, width, x, y)
    def draw(self, draws: list | Tuple) -> None:
        # Instância de Draw: [x, y, str]
        for x, y, string in draws:
            self.screen.addstr(y, x, string)
        self.screen.refresh()
        self.screen.erase()

class DriverVideo:
    def __init__(self):
        self.screen = None

    # Liga a "tela"
    def ligar(self) -> None:
        self.screen = curses.initscr()
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        curses.start_color()
        self.screen.keypad(True)
        self.screen.clear()

    # Volta o terminal para o normal
    def desligar(self) -> None:
        if self.screen:
            self.screen.keypad(False)
            curses.nocbreak()
            curses.echo()
            curses.endwin()

    # Desenha na tela o que o kernel pedir na tela
    def draw(self, draws: list | Tuple) -> None:
        # Instância de Draw: [x, y, str]
        self.screen.clear()
        for x, y, string in draws:
            self.screen.addstr(y, x, string)
        self.screen.refresh()
        self.screen.erase()

