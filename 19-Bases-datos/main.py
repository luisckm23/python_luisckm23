import pymysql

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
        )

    self.cursor = self.connection.cursor()

database = DataBase()