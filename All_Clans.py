import random

#All helpers needed for main.py relating to clans and village placement. REMEMBER TO ADD MORE WHEN WRITE UPS FOR EACH VILLAGE ARE CREATED

#Cloud Village Portion
def cloud():
    print("You are part of the Cloud Village")
    clans = ["Arakami", "Chinoike", "Fuden", "Ginbakku", "Juden", "Kanon", "Kinzokunoichi", "Kushinada", "Tenkujin", "Cloud Style Kenjutsu", "Gale Style", "Clanless"]
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

#Grass Village Portion
def grass():
    print("You are part of the Grass Village")
    clans = ["Kusanoha", "Byakko", "Otakemaru", "Yume", "Inari", "Shimenawa", "Shen", "Kinoko", "Kaiga", "Yosai",]
    origin = random.choice(clans)
#Founding Clans
    if origin in {"Kusanoha", "Shimenawa", "Shen"}:
        print("You are born into the " + origin + " Clan. One of the founding clans of the Grass")
#Non-Founding Clans
    if origin in {"Byakko", "Otakemaru", "Yume", "Inari", "Kinoko", "Kaiga", "Yosai"}:
        print("You are born into the " + origin + " Clan.")

#Rain Village Portion
def rain():
    print("You are part of the Rain Village")
    clans = ["Black Salamander", "Corpse Hydra", "Izumine", "Kagayaki", "Kotobuki", "Koyaki", "Onamazu", "Hattori", "Kenshin", "Flame Salamander",]
    origin = random.choice(clans)
#Clans
    if origin in {"Izumine", "Kagayaki", "Kotobuki", "Koyaki", "Onamazu", "Hattori", "Kenshin"}:
        print("You are born into the " + origin + " Clan.")
#Surgeries
    if origin in {"Black Salamander", "Corpse Hydra", "Flame Salamander"}:
        print("You have received surgery to be more like the " + origin + ".")

#Sand Village Portion
def sand():
    print("You are part of the Sand Village")
    clans = ["Aryura", "Gaikan", "Hoki", "Shirogane", "Kariudo", "Swift Release", "Taiyofu", "Yokisoma", "Heavenly Blade Dance", "Magnet Release", "Seven Heavenly Breaths"]
    origin = random.choice(clans)
#Founding Clans
    if origin in {"Aryura", "Shirogane", "Taiyofu", "Gaiken", "Hoki"}:
        print("You are born into the " + origin + " Clan. One of the founding clans of the Sand")
#Non-founding Clans
    if origin in {"Gaikan", "Kariudo", "Yokisoma"}:
        print("You are born into the " + origin + " Clan.")
#Special Techniques
    if origin in {"Swift Release", "Heavenly Blade Dance", "Magnet Release", "Seven Heavenly Breaths"}:
        print("You are born with talent in " + origin + ".")

#Leaf Village Portion
def leaf():
    print("You are part of the Leaf Village")
    clans = ["Clanless", "Aburame", "Akimichi", "Eight Inner Gates", "Flying Raijin", "Inazuka", "Haruno", "Hatake", "Hyuga", "Nara", "Sarutobi", "Senju", "Super Beast Scroll", "Uchiha", "Yamanaka", "Yuhi"]
    origin = random.choice(clans)
#Founding clans
    if origin in {"Aburame", "Akimichi", "Hyuga", "Uchiha", "Senju"}:
        print("You are born into the " + origin + " clan. One of the founding clans")
#Specialities
    if origin in {"Eight Inner Gates", "Flying Raijin", "Super Beast Scroll"}:
        print("You are born with prowess in the" + origin)
#Non-Founding Clans
    if origin in {"Inazuka", "Haruno", "Hatake", "Nara", "Sarutobi", "Yamanaka", "Yuhi"}:
        print("You are born into the " + origin + " clan")
#Clanless
    if origin == "Clanless":
        print("You are clanless")