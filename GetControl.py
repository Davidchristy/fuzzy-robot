import time
from MySQL import MySQL

from HeartbeatReaderInstance import HeartbeatReaderInstance
from SleeperInstance import SleeperInstance

class GetControl:

    def phoneOn(self):
        try:
            # print("Phone turned on, at {}".format(time.time()))
            now = time.localtime()
            f = '%Y-%m-%d %H:%M:%S'
            sql = "INSERT INTO fuzz.Phone_Event (type, time) VALUES(0,\"{}\");".format(time.strftime(f, now))
            mysql = MySQL()
            mysql.cur.execute(sql)
            mysql.conn.commit()


            SleeperInstance.getInstance().alseep = False
            SleeperInstance.getInstance().sleepStartTime = None
            if now.tm_hour > 5:
                # It's after 5 in the morning
                if SleeperInstance.getInstance().sleepStartTime:
                    # The sleep timer has been started
                    sleeptime = time.time() - SleeperInstance.getInstance().sleepStartTime
                    if sleeptime > SleeperInstance.getInstance().inactiveRateForSleep:
                        print("Wake up!")
            return "{'result':'success'}"
        except Exception as e:
            raise e
            return {'error':'{}'.format(e)}

    def phoneOff(self):
        try:
            # print("Phone turned off, at {}".format(time.time()))
            now = time.localtime()
            f = '%Y-%m-%d %H:%M:%S'
            sql = "INSERT INTO fuzz.Phone_Event (type, time) VALUES(1,\"{}\");".format(time.strftime(f, now))
            mysql = MySQL()
            mysql.cur.execute(sql)
            mysql.conn.commit()

            if now.tm_hour >= 21 or now.tm_hour < 5:
                # This is between 9pm and 5am 
                SleeperInstance.getInstance().sleepStartTime = time.time()
                SleeperInstance.getInstance().alseep = True

            return "{'result':'success'}"
        except Exception as e:
            raise e
            return {'error':'{}'.format(e)}

    def heartbeat(self):
        try:
            deathTime = HeartbeatReaderInstance.getInstance().heartbeater.deathTime
            timeBeforeBrainDeath = HeartbeatReaderInstance.getInstance().timeBeforeBrainDeath
            if deathTime > timeBeforeBrainDeath:
                HeartbeatReaderInstance.getInstance().heartbeater.alive = True
                now = time.localtime()
                f = '%Y-%m-%d %H:%M:%S'
                sql = "INSERT INTO fuzz.Phone_Event (type, time) VALUES(2,\"{}\");".format(time.strftime(f, now))
                mysql = MySQL()
                mysql.cur.execute(sql)
                mysql.conn.commit()

            HeartbeatReaderInstance.getInstance().lastHeartbeat = time.time()
            return "{'result':'success'}"
        except Exception as e:
            raise e
            return {'error':'{}'.format(e)}
