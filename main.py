#import proper directories and local modules

import All_Clans
import random
#import tkinter as tk

#define dictionaries for random functions here
#villages = ["Cloud", "Grass", "Leaf", "Mist", "Rain", "Sand", "Sky", "Sound", "Steam", "Stone", "Waterfall"]
villages = ["Cloud", "Mist"]
classes = ["Beast_Master", "Bukijutsu", "Genjutsu","Ninjutsu", "Medical", "Puppet_Master", "Kenjutsu", "Sealing", "Sensory", "Summoning", "Tactician"]

#generate initial values
starting_village = random.choice(villages)
ninja_type = random.choice(classes)
    
#determine where character is from and define correct functions
if starting_village == "Cloud":
    All_Clans.cloud()
if starting_village == "Mist":
    print("MIST: No Wite-Ups Available")

    
