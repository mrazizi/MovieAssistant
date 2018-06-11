import MySQLdb
from imdb_api import IMDBMovie

class DBAPI():

    def __init__(self):

        self.db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                                  user="root",         # your username
                                  passwd="password",   # your password
                                  db="movie_assistant")# name of the data base

        self.cur = self.db.cursor()


    def saveMovieListToDB(self, movieList):
        for movieName in movieList:
            sql = """
            INSERT INTO directoryMovie(movieName)
            SELECT * FROM (SELECT ('%s')) AS tmp
            WHERE NOT EXISTS (
            SELECT movieName FROM directoryMovie WHERE movieName = ('%s')
            ) LIMIT 1; """ % (movieName, movieName)

            try:
                self.cur.execute(sql)
                self.db.commit()
            except:
                self.db.rollback()

        # self.db.close()

    def updateMovieIDs(self):
        imdbMovie = IMDBMovie()
        sql = "SELECT movieName FROM directoryMovie"
        results = 0

        try:
            self.cur.execute(sql)
            results = self.cur.fetchall()
            for movieName in results:
                movieID = imdbMovie.getMovieID(movieName[0])

                sql = "UPDATE directoryMovie SET movieID = ('%s') WHERE movieName = ('%s')" %(movieID, movieName[0])

                try:
                    self.cur.execute(sql)
                    self.db.commit()

                    print(movieName[0])
                    print(movieID)
                    print()

                except:
                    self.db.rollback()

        except:
            print("Error: Can't fetch data from database")
