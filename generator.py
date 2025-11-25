#import proper directories and local modules

import All_Clans
import All_Classes
import random
import Extras

starting_village = "Cloud"


def main(starting_village):



    #"Beast_Master", "Bukijutsu", "Genjutsu","Ninjutsu", "Medical", "Puppet_Master", "Kenjutsu", "Sealing", "Sensory", "Summoning", "Tactician"
    classes = ["Beast_Master", "Puppet_Master", "Buki", "Gen", "Nin", "Medical", "Ken", "Sensory"]

    #generate initial values
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
        case "Leaf":
            All_Clans.leaf()

    #determing character class
    match ninja_type:
        case "Beast_Master":
            All_Classes.Beast()
        case "Puppet_Master":
            All_Classes.Puppets()
        case "Buki":
            All_Classes.Buki()
        case "Gen":
            All_Classes.Gen()
        case "Nin":
            All_Classes.Nin()
        case "Medical":
            All_Classes.Medical()
        case "Ken":
            All_Classes.Ken()
        case "Sensory":
            All_Classes.Sensory()
        case "Summoning":
            All_Classes.Summoning()
        case "Tactician":
            All_Classes.Tactician()
    
    Extras.preferred_weapon()
    Extras.luckpoint()

print("Generator Loaded")


if __name__ == "__generator__":
    pass