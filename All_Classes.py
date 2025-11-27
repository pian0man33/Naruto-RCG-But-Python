import random
import Beast_Master
import Puppet_Master
import webbrowser
#All helpers designated to Classes, Branches and other things related to each class.
#Due to how long this code might be... I'm going to make other subsections for puppets and the like, see how that goes

def Beast():
    print("You are a master of Beasts")
    Beast_Master.beast_extras()
    url = "https://homebrewery.naturalcrit.com/share/qHqWecEkSsYk#beast-master"
    webbrowser.open(url)
def Puppets():
    print("You are a puppet master")
    Puppet_Master.puppet_extras()
    url = "https://homebrewery.naturalcrit.com/share/qHqWecEkSsYk#puppet-master" 
    webbrowser.open(url) 
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
    url = "https://homebrewery.naturalcrit.com/share/qHqWecEkSsYk#bukijutsu-specialtist"
    webbrowser.open(url)
def Gen():
    print("You are a Genjutsu Specialist")
    branches = ["Illusionist", "Unseen", "Enchanter"]
    type = random.choice(branches)
    match type:
        case "Illusionist":
            print("Confuse your enemies, make them question what's real, you are an illusionist")
        case "Unseen":
            print("Through subtly and illusions, you have learned to land the killing blow, you are an unseen assassin.")
        case "Enchanter":
            print("Your genjutsu has proven priceless as a supportive took to yourself and allies, you are an enchanter")
    url = "https://homebrewery.naturalcrit.com/share/qHqWecEkSsYk#genjutsu-specialist"
    webbrowser.open(url)
def Nin():
    print("You are a Ninjutsu Specialist")
    branches = ["Perfect", "Chromatic", "Signature"]
    type = random.choice(branches)
    match type:
        case "Perfect":
            print("You aim to perfect your chakra control")
        case "Chromatic":
            print("You prefer to use every nature release you can")
        case "Signature":
            print("You wish to leave your mark by creating a signature technique")
    url = "https://homebrewery.naturalcrit.com/share/qHqWecEkSsYk#ninjutsu-specialist"
    webbrowser.open(url)
def Medical():
    print("You are a Medical Specialist")
    branches = ["Bedside", "Combat", "Poisoner"]
    type = random.choice(branches)
    match type:
        case "Bedside":
            print("You shine when you are given time to provide care, you are a bedisde specialist")
        case "Combat":
            print("Most crach when under the pressure of battle, not you. You are a Combat Medic")
        case "Poisoner":
            print("Not every doctor uses their skills to heal, you are a poisoner.")
    url = "https://homebrewery.naturalcrit.com/share/qHqWecEkSsYk#medical-specialist"
    webbrowser.open(url)
def Ken():
    print("You are a Kenjutsu Specialist")
    branches = ["Samurai", "Swordplay", "Ronin"]
    type = random.choice(branches)
    match type:
        case "Samurai":
            print("You hold honor above else, Wake up Samurai")
        case "Swordplay":
            print("You are a true master who can easily change their fighting style on the fly, you have mastered swordplay.")
        case "Ronin":
            print("You prefer your team to be just you and your blade, A lone Ronin")
    url = "https://homebrewery.naturalcrit.com/share/qHqWecEkSsYk#kenjutsu-specialtist"
    webbrowser.open(url)
def Sensory():
    print("You are a Sensory Specialist")
    branches = ["Vigilant", "Detector", "Scout"]
    type = random.choice(branches)
    match type:
        case "Vigilant":
            print("You prefer to keep an eye out, you are Vigilant")
        case "Detector":
            print("You are able to sense those a mile away, you are a Detector")
        case "Scout":
            print("You scout ahead for your team, eliminating threats in secret, you are a Scout")
    url = "https://homebrewery.naturalcrit.com/share/qHqWecEkSsYk#sensory-specialtist"
    webbrowser.open(url)
def Summoning():
    print("You are a Summoning Specialist")
    branches = ["Kaiju", "Tribe Leader", "Handler"]
    type = random.choice(branches)
    match type:
        case "Kaiju":
            print("You call powerful summons to fight alongside you, you are a Kaiju Summoner")
        case "Tribe Leader":
            print("You organize your summons to battle on a unified front, you are a Tribe Leader")
        case "Handler":
            print("You fight in a coordinated fashion with your summons, you are a Handler")
    url = "https://homebrewery.naturalcrit.com/share/qHqWecEkSsYk#summoning-specialist"
    webbrowser.open(url)
