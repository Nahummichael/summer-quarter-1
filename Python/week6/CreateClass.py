#1. make a class to represent a video game/movie collection
#2. create a constructor method __init__()
#3. create a list for the movie library each
#4. create an instance variable for the user's favorite movie and video game
#5. create the following functions for your class
# - a function to display all the movies
# - a function to display all the video games
# - a function to add a new movie/game
# - a function to take away a movie/game
# - a function to select a favorite movie and or game
#6. then create a new tester.py file to test the code

class Collection:

    def __init__(self, movieList, gameList):
        self.movieList = []
        self.gameList = []
        self.favGame = ""
        self.favMovie = ""

        self.movieList = movieList
        self.gameList = gameList

   
    def addgame(self, games):
        if games in self.gameList:
            print("ts alr in ur game collection")
        else:
            self.gameList.append(games)
        
    def removegame(self, game):
        if game in self.gameList:
            self.gameList.remove(game)
        else:
            print("how u not know what is and isn't in yo own list")

    def addmovies(self, movies):
        if movies in self.movieList:
            print("bruh this movie alr in the list")
        else:
            self.movieList.append(movies)

    def removemovie(self, movie):
        if movie in self.movieList:
            self.movieList.remove(movie)
        else:
            print("i cant remove what aint there bucko")

    def displayEntireCollection(self):
       for game in self.gameList:
           print(game)
       for movie in self.movieList:
            print(movie)

    def displaygame(self):
        for game in self.gameList:
            print(game)

    def displaymovie(self):
        for movie in self.movieList:
            print(movie)

    def displayfavgame(self):
        print(f"fav game: {self.favGame}")

    def displayfavmovie(self):
        print(f"fav movie: {self.favMovie}")
    
    def displayCollection(self):
       self.displayEntireCollection()
       self.displayfavgame()
       self.displayfavmovie()
    
    def setfavmovie(self, movie):
        if movie not in self.movieList:
            self.addmovies(movie)
        self.favMovie = movie

        
    def setfavgame(self, game):
        if game not in self.gameList:
            self.addgame(game)
        self.favGame = game
        