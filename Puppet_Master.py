import random


def puppet_extras():
#Define the dictionaries
    branches = ["Marionette", "Performer", "Manipulator"]
    s_technique = ["Black", "Red", "White", "Green", "Silver", "Gold", "Violet"]
#define the random choices
    path = random.choice(branches)
    type = random.choice(s_technique)
#print results for branch
    match path:
        case "Marionette":
            print("Some puppet masters prefer to work from the shadows, using their puppets like a Marionette")
        case "Performer":
            print("You prefer to put on a show.")
        case "Manipulator":
            print("Somtimes you need to... push your enemies in the right direction with a bit of manipulation")
#secret technique
    match type:
        case "Black":
            B_Puppet = ["Crow", "Ant", "Salamander", "Revenant", "Effigy"]
            puppet = random.choice(B_Puppet)
        case "Red":
            R_Puppet = ["Soldier", "Sniper", "Heavy"]
            puppet = random.choice(R_Puppet)
        case "White":
            W_Puppet = ["Hitokiri", "Oni", "Kensei", "Monk"]
            puppet = random.choice(W_Puppet)
        case "Green":
            G_Puppet = ["Nurse", "Bulwark", "Sparrow",]
            puppet = random.choice(G_Puppet)
        case "Silver":
            S_Puppet = ["Beast", "Goliath", "Colossus"]
            puppet = random.choice(S_Puppet)
        case "Gold":
            Go_Puppet = ["Spider", "Doll", "Angel"]
            puppet = random.choice(Go_Puppet)
        case "Violet":
            print("You are a practitioner of the Violet Secret Technique.")

    if type != "Violet":
        print("You are a practioner of the " + type + " Secret Technique, starting with the " + puppet + " puppet")
        