import random
#All helpers designated to Classes, Branches and other things related to each class.
#Due to how long this code might be... I'm going to make other subsections for puppets and the like, see how that goes

def Beast():
    print("You are a a master of Beasts")
    branches = ["Coordinated Hunter", "Rider", "Watchdog"]
    path = random.choice(branches)
    if path == "Coordinated Hunter":
        print("You and your beast are a perfect team, coordinated hunters.")
    if path == "Rider":
        print("You Rush into combat with your trusty beast, you are a rider.")
    if path == "Watchdog":
        print("Your beast is your closest friend and protector, they are your watchdog.")