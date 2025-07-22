import random

from hero import Hero
from mage import Mage
from ninja import Ninja
from zombie import Zombie

print("Game starts!!!")
user_name = input("Give a name: ")
user_char = int(input('''
Pick a number to choose a cahracter
1) Zombie
2) Mage
3) Hero
4) Ninja
'''))
if user_char == 1:
    user = Zombie(user_name, 70, 15, 130)
elif user_char == 2:
    user = Mage(user_name, 150, 3, 60)
elif user_char == 3:
    user = Hero(user_name, 100, 10, 100)
else:
    user = Ninja(user_name, 110, 8, 98)

npc_char = random.randint(1,4)
if npc_char == 1:
    npc = Zombie("", 70, 15, 130)
elif npc_char == 2:
    npc = Mage("", 150, 3, 60)
elif npc_char == 3:
    npc = Hero("", 100, 10, 100)
else:
    npc = Ninja("", 110, 8, 98)

print(user.display_char()+ " VS "+ npc.display_char())

while True:
    if npc.health <= 0:
        print("Congrats you won!!!!!!!")
        break;
    elif user.health <= 0:
        print("You lost :(")
        break;

    user_attack_pick = int(input(
        f"Pick an attack 0){user.attacks[0].name}, 1){user.attacks[1].name}"))
    print(user.display_char(), "attacks with ", user.attacks[user_attack_pick].name)
    npc.damage_taken(user.attacks[user_attack_pick].damage)
    print("npcs life is ", npc.health)
    npc_attack = npc.char_attack()
    print(npc.display_char(), "attacks with ", npc_attack.name)
    user.damage_taken(npc_attack.damage)
    print("Your life is ", user.health)
