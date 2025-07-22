import random

from char_attacks import Char_attacks
from character import Character


class Hero(Character):

    def __init__(self, name: str, attack: int, defence: int, health: int):
        super().__init__(name, attack, defence, health)
        self.attacks = [Char_attacks("punch", 15), Char_attacks("kick", 8)]


    def display_char(self):
        return "🦸‍♂️"

    def char_attack(self):
        pointer = random.randint(0, 1)
        return self.attacks[pointer]
