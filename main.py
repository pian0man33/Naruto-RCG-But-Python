#import proper directories and local modules

import All_Clans
import All_Classes
import random
#import tkinter as tk

def main():
    #define dictionaries for random functions here
    #villages = ["Cloud", "Grass", "Leaf", "Mist", "Rain", "Sand", "Sky", "Sound", "Steam", "Stone", "Waterfall"]
    villages = ["Cloud", "Grass", "Rain", "Sand"]
    #classes = ["Beast_Master", "Bukijutsu", "Genjutsu","Ninjutsu", "Medical", "Puppet_Master", "Kenjutsu", "Sealing", "Sensory", "Summoning", "Tactician"]
    classes = ["Beast_Master", "Puppet_Master"]

    #generate initial values
    starting_village = random.choice(villages)
    ninja_type = random.choice(classes)
        
    #determine where character is from and define correct functions
    match starting_village:
        case "Cloud":
            All_Clans.cloud()
        case "Grass":
            All_Clans.grass()
        case "Rain": #The Best One
            All_Clans.rain()
        case "Sand":
            All_Clans.sand()

    #determing character class
    match ninja_type:
        case "Beast_Master":
            All_Classes.Beast()
        case "Puppet_Master":
            All_Classes.Puppets()
