import time
from MySQL import MySQL

class GetControl:

    def phoneOn(self):
        try:
            print("Phone turned on, at {}".format(time.time()))
            now = time.localtime()
            f = '%Y-%m-%d %H:%M:%S'
            sql = "INSERT INTO fuzz.Phone_Event (type, time) VALUES(0,\"{}\");".format(time.strftime(f, now))
            mysql = MySQL()
            mysql.cur.execute(sql)
            mysql.conn.commit()
            return "{'result':'success'}"
        except Exception as e:
            raise e
            return {'error':'{}'.format(e)}

    def phoneOff(self):
        try:
            print("Phone turned off, at {}".format(time.time()))
            now = time.localtime()
            f = '%Y-%m-%d %H:%M:%S'
            sql = "INSERT INTO fuzz.Phone_Event (type, time) VALUES(1,\"{}\");".format(time.strftime(f, now))
            mysql = MySQL()
            mysql.cur.execute(sql)
            mysql.conn.commit()

            return "{'result':'success'}"
        except Exception as e:
            raise e
            return {'error':'{}'.format(e)}
