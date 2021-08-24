import time
import requests
import random

games = {"Call of duty Franchise", "GTA V", "Minecraft", "Fortnite", "Overwatch", "Csgo", "League of legends",
         "Rocket League", "Smash Ultimate", "Roblox", "Among Us", "Rainbow Six Siege"}

platforms = {"PC", "Xbox", "Playstation", "Nintendo"}

issues = {"Addiction", "Energy Drinks", "Money", "Social Life", "Hygiene", "Insomnia & Fatigue", "Headache & Eye Strains",
          "Carpal Tunnel", "Violence in Gaming", "Toxicity", "Raging"}

firstNames = set()
lastNames = set()
useMe = set()

with open("FirstNames.txt", encoding="utf-8") as f:
    broken = f.readlines()
    for line in broken:
        words = line.split()
        firstNames.add(words[1])
        firstNames.add(words[3])

with open("LastNames.txt", encoding="utf-8") as f:
    broken = f.readlines()
    for line in broken:
        words = line.split()
        lastNames.add(words[1])

for name in lastNames:
    useMe.add(name[0] + name[1:].lower())


for i in range(83):
    values = {
                # First Name
                "entry.91109308": random.sample(firstNames, 1)[0],
                #Last Name
                "entry.1374768575" : random.sample(useMe, 1)[0],
                #Game
                "entry.816067948" : random.sample(games, random.randint(1,12)),
                #Platform
                "entry.1282916061" : random.sample(platforms, 1)[0],
                #Issue
                "entry.2082227049": random.sample(issues, 1)[0],
                #Pledge
                "entry.161617302": "Yes"
            }

    try:
        requests.post("https://docs.google.com/forms/d/e/1FAIpQLSfehEY3vJK4PaC5USxxTthkQTs1yxtX1IOaxzlYmkJw_dEi2A/formResponse", data=values)
        print("Form Submitted.")
        time.sleep(5)
    except:
        print("Error Occured!")
