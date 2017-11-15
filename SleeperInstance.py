import time

class SleeperInstance:
    # Here will be the instance stored.
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method."""
        if SleeperInstance.__instance == None:
            SleeperInstance()
        return SleeperInstance.__instance

    def __init__(self):
        if SleeperInstance.__instance != None:
            raise Exception("This class is a singleton!")
        
        # in seconds
        self.inactiveRateForSleep = 5*60*60
        self.sleepStartTime = None
        self.asleep = False

        SleeperInstance.__instance = self