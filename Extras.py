import random
from random import randint

def preferred_weapon():
    weapons = ["Unarmed Attacks", "Shuriken", "Kunai", "Explosives", "Striking Weapons", "One-Handed Weapons", "Two-Handed Weapons", "Ranged Weapons"]
    preferred = random.choice(weapons)
    print(f"Your preferred weapon category is: {preferred}")


def luckpoint():
    luck = randint(0,9)
    match luck:
        case 0 | 1 | 2:
            print("You start with 2 Luck Point and 12 extra wounds")
        case 3 | 4 | 5:
            print("You start with 3 Luck Points and 8 extra wounds")
        case 6 | 7:
            print("You start with 4 Luck Points and 4 extra wounds")
        case 8 | 9:
            print("You start with 5 Luck Points and no extra wounds")
