import random

#Cloud Village Portion
def cloud():
    clans = ["Arakami", "Chinoike", "Fuden", "Ginbakku", "Juden", "Kanon", "Kizokunoici", "Kushinada", "Tenkujin", "Cloud Style Kenjutsu", "Gale Style", "Clanless"]
    origin = random.choice(clans)
    if origin == "Arakami":
        print("You are born into the Arakami Clan. One of the founding clans of the Cloud")
    if origin == "Chinoike":
        print("You are born into the Chinoike Clan")