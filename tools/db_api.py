import MySQLdb

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

        self.db.close()
