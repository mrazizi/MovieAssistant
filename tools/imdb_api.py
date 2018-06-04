from imdb import IMDb

class IMDBMovie():

    def __init__(self):
        # create and instance of the IMDb class
        self.ia = IMDb()

    def getMovieTitle(self, movieName):
        imdbResult = self.ia.search_movie(movieName)
        # return imdbResult[0]
        return movieName

    def getMovieID(self, movieName):
        imdbResult = self.ia.search_movie(movieName)
        return imdbResult[0].movieID