class Character:

    def __init__(self, name: str, attack: int, defence: int, health: int):
        self.name = name
        self.attack = attack
        self.defence = defence
        self.health = health

    def damage_taken(self, dmg: int):
        self.health = self.health + self.defence - dmg

    def display_char(self):
        pass

    def char_attack(self):
        pass
