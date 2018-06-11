from imdb import IMDb

class IMDBMovie():

    def __init__(self):
        # create and instance of the IMDb class
        self.ia = IMDb()

        self.rating = "NO_DATA"
        self.runtimes = "NO_DATA"
        self.genres = "NO_DATA"
        self.plotOutline = "NO_DATA"
        self.director = "NO_DATA"
        self.producer = "NO_DATA"
        self.cast = "NO_DATA"


    def getMovieTitle(self, movieName):
        imdbResult = self.ia.search_movie(movieName)
        # return imdbResult[0]
        return movieName

    def getMovieID(self, movieName):
        imdbResult = self.ia.search_movie(movieName)
        return imdbResult[0].movieID

    def getMovieInfo(self, movieName):
        imdbResult = self.ia.get_movie(movieName)

        self.title = imdbResult.get('title')
        self.year = imdbResult.get('year')
        if(imdbResult.get('rating')): self.rating = imdbResult.get('rating')
        if(imdbResult.get('runtimes')): self.runtimes = imdbResult.get('runtimes')
        if(imdbResult.get('genres')): self.genres = imdbResult.get('genres')
        if(imdbResult.get('plot outline')): self.plotOutline = imdbResult.get('plot outline')
        if(imdbResult.get('director')): self.director = imdbResult.get('director')
        if(imdbResult.get('producer')): self.producer = imdbResult.get('producer')
        if(imdbResult.get('cast')): self.cast = imdbResult.get('cast')

    def printMovieInfo(self):
        print("Title: " + str(self.title))
        print("Year: " + str(self.year))
        print("Rating: " + str(self.rating))
        print("Runtime: " + str(self.runtimes))
        print("Genres: " + str(self.genres))
        print("Plot: " + str(self.plotOutline))
        print("Director: " + str(self.director))
        print("Producer: " + str(self.producer))
        print("Cast: " + str(self.cast))
