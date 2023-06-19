import os
from typing import List

from graph_Manager import Graph
from start_module.Variables import *
from StaticMethods import *
from Time import Time


class deleteLabel:
    def __init__(self, start_period: Time, finish_period: Time):
        self.start_period = start_period
        self.finish_period = finish_period

    def deletedPeriod(self):
        return f"""DELETED FROM Time1:{str(self.start_period)} TO Time2:{str(self.finish_period)} PERIOD;\n"""


class Dir:
    def __init__(self, patient, start_period, finish_period):
        self.patient = patient
        self.start_period = start_period
        self.finish_period = finish_period

    def deletedPeriod(self):
        return f"""DELETED FROM T1:{sec_to_time_short(self.start_period)} TO T2:{sec_to_time_short(self.finish_period)} PERIOD;"""

    def __str__(self):
        return f"""/{self.patient}_{sec_to_time_short(self.start_period)}@{sec_to_time_short(self.finish_period)}_deleted{FilesConstant.text_type}"""


class autoDeleteGraph:
    def __init__(self):
        self.__startTime: int = 0
        self.__finishTime: int = 0
        self.__file_direction = autoDeleteGraphConstant.where_to_save_file_direction
        self.__full_file_name = ""

        self.__graph_constant: Graph = Graph()
        self.__graph_constant.file_init()
        self.__graph_constant.start_init()
        self.__first_init = False
        self.__need_to_delete = []

        if not os.path.exists(self.__file_direction):
            os.mkdir(self.__file_direction)

        self.file_init()

    def file_init(self):

        s: str = self.__file_direction + "/" + self.getPatientName()
        if not os.path.exists(s):
            os.mkdir(s)
            self.__first_init = True
        self.__file_direction = s

    def getPatientName(self):
        v: str = self.__graph_constant.file_n
        return v.split("/")[-1]

    def readData(self, file_dir: str):
        print(f"""[INFO] trying to read file: {self.__file_direction} without data""")

    def writeData(self, start_time: Time = None, finish_time: Time = None):

        if start_time is None:
            self.__startTime = self.__graph_constant.current_xs[0]
        else:
            self.__startTime = start_time.getSeconds()

        if finish_time is None:
            self.__finishTime = self.__graph_constant.current_xs[-1]
        else:
            self.__finishTime = finish_time.getSeconds()

        self.__full_file_name = self.__file_direction + str(
            Dir(self.getPatientName(), self.__startTime, self.__finishTime))
        with open(self.__full_file_name, 'w') as current_file:

            st = self.__graph_constant.getElementPos(self.__startTime)
            for j in self.__need_to_delete:

                fin = self.__graph_constant.getElementPos(j[0].getSeconds())
                i = st
                while i <= fin:
                    current_file.write(self.__generateOneLine(i))
                    i = i + 1
                    st = self.__graph_constant.getElementPos(j[1].getSeconds()) + 1
                current_file.write("\n" + deleteLabel(j[0], j[1]).deletedPeriod() + "\n")
            fin = self.__graph_constant.getElementPos(self.__finishTime)
            i = st
            while i <= fin:
                current_file.write(self.__generateOneLine(i))
                i = i + 1

        return True

    def __generateOneLine(self, i: int):
        current_line = f"{sec_to_time_short(self.__graph_constant.current_xs[i]):<30}"
        for j in range(self.__graph_constant.getSignalsAmount()):
            current_line = current_line + f"{self.__graph_constant.getCurrentYS(j)[i]:<30}"
        current_line = current_line + "\n"
        return current_line

    def deleteData(self, what_to_delete: List = []):
        self.__need_to_delete = what_to_delete
        return True

    def make_graph(self, input_file_name: str):
        pass

    def get_current_file_dir(self):
        return self.__file_direction


if __name__ == "__main__":
    autoDelGraph = autoDeleteGraph()
    start = Time()
    need_to_del = []
    need_to_del.append([Time(0, 0, 2, 0), Time(0, 0, 8, 0)])
    need_to_del.append([Time(0, 0, 9, 0), Time(0, 0, 10, 0)])
    autoDelGraph.deleteData(need_to_del)
    finish = Time(0, 0, 10, 0)
    autoDelGraph.writeData(start, finish)
