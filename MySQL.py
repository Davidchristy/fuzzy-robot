import time
import os
import pymysql

from warnings import filterwarnings

class MySQL:


    def __init__(self):

        user = "FuzzyRobot"
        host = "127.0.0.1"
        password = "password"
        database = "fuzz"

        filterwarnings('ignore', category = pymysql.Warning)
        self.conn = pymysql.connect(host=host, user=user, passwd=password, db=database)
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)
