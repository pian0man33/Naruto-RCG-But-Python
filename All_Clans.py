import random

#Cloud Village Portion
def cloud():
    clans = ["Arakami", "Chinoike", "Fuden", "Ginbakku", "Juden", "Kanon", "Kizokunoichi", "Kushinada", "Tenkujin", "Cloud Style Kenjutsu", "Gale Style", "Clanless"]
    origin = random.choice(clans)
#Founding Clans
    if origin in {"Arakami", "Fuden", "Kushinada", "Tenkujin"}:
        print("You are born into the " + origin + " Clan. One of the founding clans of the Cloud")
#Non-Founding Clans
    if origin in {"Chinoike", "Ginbakku","Juden", "Kanon", "Kinzokunoichi"}:
        print("You are born into the " + origin + " Clan.")
#Special Techniques
    if origin in {"Cloud Style Kenjutsu", "Gale Style"}:
        print("You are born with talent in " + origin + ".")
#Clanless
    if origin == "Clanless":
        print("You are not born with any specialties")