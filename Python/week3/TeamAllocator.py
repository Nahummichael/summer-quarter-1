# This program will allocate teams randomly from a list of names

import random

players = ["Nahum", "Darren", "Braylen",
           "Xavier", "Walter", "Kauri",
            "Isaiah", "Taymur","Avery",
            "Taqari", "Kenlon","Marshawn",
            "Kamari", "Kristopher", "Joseph",
            "Carl", "Jeffrey", "Nishad",
            "Maximus", "JaDen", "Joaquin",
            "Jarmauri", "EJ", "Semaj"]

def PickTeams(players):
    random.shuffle(players)
    team1 = players[:len(players) // 2]
    teamCaptain1 = team1[random.randrange(0,12)]

    print("TEAM 1")
    print("team 1 Captain: " + teamCaptain1)
    for player in team1:
        print(player) 

    team2 = players [len(players) // 2:]
    teamCaptain2 = team2[random.randrange(0,12)]

    print("\nTEAM 2:")
    print("team 2 Captain: " + teamCaptain2)
    for player in team2:
        print(player) 

PickTeams(players)

