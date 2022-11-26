import pyodbc

cnxn = pyodbc.connect("DRIVER={SQLite3 ODBC Driver};SERVER=localhost;DATABASE=pythonsqlite.db;Trusted_connection=yes")


class DBPost:
    def __init__(self, tbl, txt, info):
        self.tbl = tbl
        self.txt = txt
        self.info = info
        self.to_db()

    def to_db(self):
        with cnxn.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {self.tbl} where txt = '{self.txt}' and additional_info = '{self.info}' ")
            row = cursor.fetchone()
            if row:
                print('Already posted!')
            else:
                cursor.execute(f"INSERT INTO {self.tbl} VALUES('{self.txt}', '{self.info}')")
                cursor.commit()


tbl = 'Joke'
txt = 'Did you hear about the claustrophobic astronaut?/n He just needed a little space'
info = 'Funny meter – three of ten'
DBPost(tbl, txt, info)



