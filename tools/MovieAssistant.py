from lister import DirectoryLister
from db_api import DBAPI

movieDirectory = "/media/dsm/DSM-SP/Movies/Movies 1"

dl = DirectoryLister(movieDirectory)
movieList = dl.getMovieList()

dbapi = DBAPI()
dbapi.saveMovieListToDB(movieList)