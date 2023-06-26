import re


class Time:

    def __init__(self, _hour: float = 0, _minute: float = 0, _sec: float = 0, _milis: float = 0):
        self.__hours = _hour
        self.__minutes = _minute
        self.__seconds = _sec
        self.__milis = _milis

    def get_seconds(self):
        return self.__hours * 3600 + self.__minutes * 60 + self.__seconds + self.__milis / 100

    @property
    def hours(self):
        return self.__hours

    @property
    def seconds(self):
        return self.__seconds

    @property
    def milis(self):
        return self.__milis

    @property
    def minutes(self):
        return self.__minutes

    def timeForSliders(self):
        if self.__minutes == 0:
            return self.__hours-1, 59
        return self.__hours, 59

    def add_time(self, second):
        self.__seconds = self.seconds + second

    def getSeconds(self):
        return self.__hours * 3600 + self.__minutes * 60 + self.__seconds + self.__milis / 100

    @staticmethod
    def parseOne(value: str):
        v = re.split(r"h|m|s|ms", value.replace(" ", ""))
        return Time(float(v[0]), float(v[1]), float(v[2]), float(v[3]))

    def convertSecToTime(self):
        return "Current time: " + str(self.__hours) + "h. " + str(self.__minutes) + "m. " + str(
            self.__seconds) + "s. " + str(
            self.__milis) + "ms"

    def sec_to_time_short(self):
        return str(self.__hours) + "h " + str(self.__minutes) + "m " + str(self.__seconds) + "s " + str(
            self.__milis) + "ms"

    def __eq__(self, other):
        return self.get_seconds() == other.get_seconds()

    def __gt__(self, other):
        return self.get_seconds() > other.get_seconds()

    def __lt__(self, other):
        return self.get_seconds() < other.get_seconds()

    def __str__(self):
        return self.sec_to_time_short()
