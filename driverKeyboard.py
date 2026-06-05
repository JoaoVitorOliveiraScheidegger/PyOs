from typing import Any

from pynput import keyboard

class DriverKeyboard:
    def __init__(self):
        self.pressed_keys = set()
        self.listener = None

        self.special_keys.caps_lock = keyboard.Key.caps_lock

    def ligar(self):
        self.listener = keyboard.Listener(on_press=self._on_press, on_release=self._on_release)

        self.listener.start()

    def desligar(self):
        if self.listener:
            self.listener.stop()

    @staticmethod
    def _translate_key(key):
        try:
            return key.char
        except AttributeError:
            return key.name

    def _on_press(self, key: Any) -> None:
        char_key = self._translate_key(key)
        if char_key:
            self.pressed_keys.add(char_key)

    def _on_release(self, key: Any) -> None:
        char_key = self._translate_key(key)
        if char_key:
            self.pressed_keys.discard(char_key)

    def gkey(self, key: str):
        return key in self.pressed_keys

        return None

    def akeys(self):
        return self.pressed_keys