import random
import Beast_Master
import Puppet_Master
#All helpers designated to Classes, Branches and other things related to each class.
#Due to how long this code might be... I'm going to make other subsections for puppets and the like, see how that goes

def Beast():
    print("You are a master of Beasts")
    Beast_Master.beast_extras()
def Puppets():
    print("You are a puppet master")
    Puppet_Master.puppet_extras()
def Buki():
    print("You are a Bukjutsu Specialist")
    branches = ["Weapons", "Vanguard", "Marksman"]
    type = random.choice(branches)
    match type:
        case "Weapons":
            print("You easily master a weapon within moments of picking it up, you are a Weapons Master")
        case "Vanguard":
            print("You wield heavy weapons and two-handed weapons with ease, you are a Vanguard")
        case "Marksman": 
            print("You eliminate enemies with lethal precision from a distance, you are a Marksman")