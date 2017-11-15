import time
import threading

from MySQL import MySQL

class HeartbeatThread(threading.Thread):
    def __init__(self,parent):
        threading.Thread.__init__(self)
        self.parent = parent
        self.deathTime = 0
        self.alive = True
    def run(self):
        while True:
            self.deathTime = time.time()-self.parent.lastHeartbeat

            # print ("seconds since last beat: {}".format(round(self.deathTime,1)))
            if self.alive and self.deathTime >self.parent.timeBeforeBrainDeath:
                # This means away from house or at least not connected to wifi
                self.alive = False
                try:
                    now = time.localtime()
                    f = '%Y-%m-%d %H:%M:%S'
                    sql = "INSERT INTO fuzz.Phone_Event (type, time) VALUES(3,\"{}\");".format(time.strftime(f, now))
                    mysql = MySQL()
                    mysql.cur.execute(sql)
                    mysql.conn.commit()
                except Exception as e:
                    print(e)
                    pass

            time.sleep(30)



class HeartbeatReaderInstance:
    # Here will be the instance stored.
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method."""
        if HeartbeatReaderInstance.__instance == None:
            HeartbeatReaderInstance()
        return HeartbeatReaderInstance.__instance

    def __init__(self):
        if HeartbeatReaderInstance.__instance != None:
            raise Exception("This class is a singleton!")
        

        self.lastHeartbeat = time.time()
        self.timeBeforeBrainDeath = 180 
        self.heartbeater = HeartbeatThread(self)
        self.heartbeater.daemon = True
        self.heartbeater.start()


        HeartbeatReaderInstance.__instance = self