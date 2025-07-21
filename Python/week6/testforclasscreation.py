import CreateClass

movies = ["superman", "black panther", "shazam", "how to train your dragon", "shazam: fury of the gods"]
games = ["devil May Cry 5", "The first berserker Khazan", "Black Myth Wukong", "spiderman Miles Morales","rise of the ronin"]
Nahcollection = CreateClass.Collection(games, movies)

Nahcollection.setfavgame("black Myth Wukong")
Nahcollection.setfavmovie("black panther")

Nahcollection.displayCollection()