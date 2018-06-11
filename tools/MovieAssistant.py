from lister import DirectoryLister
from db_api import DBAPI
from imdb_api import IMDBMovie

movieDirectory = "/media/dsm/DSM-SP/Movies/Movies 1"

dl = DirectoryLister(movieDirectory)
# movieList = dl.getMovieList()

dbapi = DBAPI()

# scan movie directory and save all movie names to database
# dbapi.saveMovieListToDB(movieList)

# update all movies saved in database and add their imdb id
# dbapi.updateMovieIDs()

# test getMovieInfo
ia = IMDBMovie()
ia.getMovieInfo("1371111")
ia.printMovieInfo()
