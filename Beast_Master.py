import random

def beast_extras()
#create the dictonaries and random choices
    branches = ["Coordinated Hunter", "Rider", "Watchdog"]
    natures = ["Fire", "Water", "Earth", "Wind", "Lightning", "Yin", "Yang"]
    type = ["Assassin", "Genjutsu", "Medical", "Ninjutsu", "Sensory", "Taijutsu", "Tank"]
#randomly assign values
    trait = random.choice(type)
    chakra = random.choice(natures)
    path = random.choice(branches)
#print out results (change to return so I can use with tkinter later)
#Class Branch
    if path == "Coordinated Hunter":
        print("You and your beast are a perfect team, coordinated hunters.")
    if path == "Rider":
        print("You Rush into combat with your trusty beast, you are a rider.")
    if path == "Watchdog":
        print("Your beast is your closest friend and protector, they are your watchdog.")
#beast type
    if trait == "Assassin":
        print("Your beast is an assassin. Starting with one mythic Agility.")
    if trait == "Genjutsu":
        print("Your beast is a genjutsu beast. Starting with one mythic Agility.")
    if trait == "Medical":
        print("Your beast is a medical beast. Starting with one mythic Toughness.")
    if trait == "Ninjutsu":
        print("Your beast is a ninjutsu specialist. Starting with one mythic Agility.")
    if trait == "Sensory":
        print("Your beast is a sensory beast. Starting with one mythic Agility.")
    if trait == "Taijutsu":
        print("Your beast is a taijutsu beast. Starting with one mythic Strength.")
    if trait == "Tank":
        print("Your beast is a Tank. Starting with one mythic Toughness")
#Beast Chakra Nature
    print("Your beast has a " + chakra + " chakra nature.")