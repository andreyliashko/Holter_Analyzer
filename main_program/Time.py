class Time:

    def __init__(self, _hour=0, _minute=0, _sec=0, _milis=0):
        self.__seconds = 0
        self.set_time(_hour, _minute, _sec, _milis)

    def get_seconds(self):
        return self.seconds

    def add_time(self, second):
        self.__seconds = self.seconds + second

    def set_time(self, hours, minutes, seconds, miliseconds):
        self.__seconds = hours * 3600 + minutes * 60 + seconds + miliseconds / 100

    def getSeconds(self):
        return self.__seconds

    def convertSecToTime(self):
        hours = self.__seconds // 3600
        minutes = (self.__seconds - hours * 3600) // 60
        seconds = self.__seconds - hours * 3600 - minutes * 60
        milis = (self.__seconds - hours * 3600 - minutes * 60 - seconds) * 100
        return "Current time: " + str(hours) + "h. " + str(minutes) + "m. " + str(seconds) + "s. " + str(
            milis) + "ms"

    def sec_to_time_short(self):
        hours = int(self.__seconds // 3600)
        minutes = int((self.__seconds - hours * 3600) // 60)
        seconds = int(self.__seconds - hours * 3600 - minutes * 60)
        milis = int((self.__seconds - hours * 3600 - minutes * 60 - seconds) * 100)
        return str(hours) + "h " + str(minutes) + "m " + str(seconds) + "s " + str(milis) + "ms"

    def __str__(self):
        return self.sec_to_time_short()
