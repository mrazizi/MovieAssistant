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
                print("LOG: " + movieName + "   saved")
                print()

            except Exception as e:
                print("LOG: " + movieName + "   failed!")
                print()
                print(e)
                self.db.rollback()

        # self.db.close()


    def updateMovieIDs(self):
        imdbMovie = IMDBMovie()
        sql = "SELECT movieName FROM directoryMovie WHERE movieID is NULL"
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
                    print("LOG: " + movieName[0] + "    with ID     " + movieID + "     saved")
                    print()

                except Exception as e:
                    print("ERR: " + movieName[0] + "    with ID     " + movieID + "     failed!")
                    print(e)
                    print()
                    self.db.rollback()

        except Exception as e:
            print("Error: Can't fetch data from database")
            print(e)


    def updateMovieInfo(self):
        imdbMovie = IMDBMovie()

        sql = "SELECT MovieID FROM directoryMovie"
        results = 0

        try:
            self.cur.execute(sql)
            results = self.cur.fetchall()

            for MovieID in results:
                imdbMovie.getMovieInfo(str(MovieID[0]))
                sql = """
                UPDATE directoryMovie
                SET year = ('%s'), rating = ('%s'), runtimes = ('%s'), genre1 = ('%s')
                WHERE MovieID = ('%s')
                """ %(str(imdbMovie.year), str(imdbMovie.rating), str(imdbMovie.runtimes), imdbMovie.genres[0], str(MovieID[0]))
                #
                # sqlEscaped = sql.translate(str.maketrans({"-":  r"\-",
                #                           "]":  r"\]",
                #                           "\\": r"\\",
                #                           "^":  r"\^",
                #                           "$":  r"\$",
                #                           "*":  r"\*",
                #                           ".":  r"\."}))

                try:
                    self.cur.execute(sql)
                    self.db.commit()

                    print(str(imdbMovie.title) + " --- " + str(imdbMovie.rating))
                    print()

                except Exception as f:
                    print("1" + str(f))
                    self.db.rollback()

        except Exception as e:
            print("2" + str(e))
