import os

class DirectoryLister():

    def __init__(self, movieDirectory):
        self.movieDirectory = movieDirectory

    def getMovieList(self):
        x = next(os.walk(self.movieDirectory))

        # delete extra data created by os.walk
        movieList = []
        for i in range(len(x[1])):
            movieList.append(x[1][i])

        return movieList
