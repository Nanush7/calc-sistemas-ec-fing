"""
Copyright (c) 2022 Nanush7. MIT license, see LICENSE file.
"""
from colorama import init, Fore

class Output:
    """
    Print with message level prefix (colors are optional).
    """
    def __init__(self, color: bool = True):
        self.color = color
        if self.color:
            init(autoreset=True)
            self.colors = {
                'red': Fore.LIGHTRED_EX,
                'green': Fore.LIGHTGREEN_EX,
                'white': Fore.LIGHTWHITE_EX,
                'yellow': Fore.YELLOW
            }
        else:
            self.colors = {
                'red': '',
                'green': '',
                'white': '',
                'yellow': ''
            }

    def info(self, msg: str) -> None:
        print(self.colors['white'] + 'INFO: ' + msg)

    def success(self, msg: str) -> None:
        print(self.colors['green'] + msg)

    def warning(self, msg: str) -> None:
        print(self.colors['yellow'] + 'WARNING: ' + msg)

    def error(self, msg: str) -> None:
        print(self.colors['red'] + 'ERROR: ' + msg)
