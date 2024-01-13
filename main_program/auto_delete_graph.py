import os
from typing import List
import re
from main_program.graph_manager import *
from start_module.variables import *
from main_program.static_methods import *
from main_program.Time import Time


# this class helps to generate patient files
class deleteAndFindLabel:
    def __init__(self, start_period: Time, finish_period: Time, patient: str = None):
        self.__start_period = start_period
        self.__finish_period = finish_period
        self.__patient = patient

    def gen_file_name(self):
        return f"""/{self.__patient}#{str(self.__start_period)}#{str(self.__finish_period)}#deleted{FilesConstant.text_type}"""

    def deleted_period_label(self):
        return f"""DELETED FROM Time1:{str(self.__start_period)} TO Time2:{str(self.__finish_period)} PERIOD;\n"""


# this class helps to generate deleted period label
class Dir:
    def __init__(self, patient, start_period: int, finish_period: int):
        self.patient = patient
        self.start_period = start_period
        self.finish_period = finish_period

    def deleted_period(self):
        return f"""DELETED FROM T1:{sec_to_time_short(self.start_period)} TO T2:{sec_to_time_short(self.finish_period)} PERIOD;"""

    def __str__(self):
        return f"""/{self.patient}#{sec_to_time_short(self.start_period)}#{sec_to_time_short(self.finish_period)}#deleted{FilesConstant.text_type}"""


class autoDeleteGraph:
    def __init__(self):
        self.__startTime: int = 0
        self.__finishTime: int = 0
        self.__file_direction = autoDeleteGraphConstant.where_to_save_file_direction
        self.__full_file_name = ""

        self.__graph_constant: Graph = Graph()
        self.__graph_constant.file_init()

        self.__first_init = False
        self.__need_to_delete = []

        if not os.path.exists(self.__file_direction):
            os.mkdir(self.__file_direction)

        self.file_init()

    # check if file with current patient exist
    def file_init(self):

        s: str = self.__file_direction + "/" + self.get_patient_name()
        if not os.path.exists(s):
            os.mkdir(s)
            self.__first_init = True
        self.__file_direction = s

    def get_patient_name(self):
        v: str = self.__graph_constant.file_n
        return v.split("/")[-1]

    # read data from input period if file exist
    def read_data(self, _start: Time, _finish: Time):
        current_path: str = self.__generate_file_name(_start, _finish)

        if not os.path.exists(current_path):
            print(f"[INFO] file does not exist")
            self.__write_data(start, finish)
        x_s = []
        y_s = []
        for i in range(self.__graph_constant.get_signals_amount()):
            y_s.append([])
        with open(current_path, 'r') as f:
            for line in f:
                if not line[0] == 'D':
                    current_line = re.sub(r"\s{2,}", ";", line).replace("\n", "").split(";")
                    if len(current_line) > 1:
                        x_s.append(Time.parseOne(current_line[0]).get_seconds())
                        for j in range(self.__graph_constant.get_signals_amount()):
                            y_s[j].append(float(current_line[j + 1]))
        return [x_s, y_s]

    # read data when file does not exist
    def __write_data(self, start_time: Time = None, finish_time: Time = None):

        if start_time is None:
            self.__startTime = self.__graph_constant.current_xs[0]
        else:
            self.__startTime = start_time.getSeconds()

        if finish_time is None:
            self.__finishTime = self.__graph_constant.current_xs[-1]
        else:
            self.__finishTime = finish_time.getSeconds()
        s = self.__generate_file_name(start_time, finish_time)
        if os.path.exists(s):
            raise Exception(
                f"Forbidden to modify file. It is already exist; Delete file from folder or choose another input time;")
        self.__graph_constant.start_init()
        self.__full_file_name = self.__file_direction + str(
            Dir(self.get_patient_name(), self.__startTime, self.__finishTime))

        with open(self.__full_file_name, 'w') as current_file:
            start_line = f"{'Date':<39}"
            for j in range(self.__graph_constant.get_signals_amount()):
                start_line += f"{'Signal ' + str(j):>30}"
            current_file.write(start_line + "\n")

            st = self.__graph_constant.get_element_pos(self.__startTime)
            for j in self.__need_to_delete:
                fin = self.__graph_constant.get_element_pos(j[0].getSeconds())
                i = st
                while i < fin:
                    current_file.write(self.__generate_one_line(i))
                    i = i + 1
                    st = self.__graph_constant.get_element_pos(j[1].getSeconds()) + 1
                current_file.write("\n" + deleteAndFindLabel(j[0], j[1]).deleted_period_label() + "\n")
            fin = self.__graph_constant.get_element_pos(self.__finishTime)
            i = st
            while i <= fin:
                current_file.write(self.__generate_one_line(i))
                i = i + 1
        print(f"[INFO] file:{self.__generate_file_name(start_time, finish_time)} saved;")
        return True

    # create one line of input file data
    def __generate_one_line(self, i: int):
        current_line = f"{sec_to_time_short(self.__graph_constant.current_xs[i]):<30}"
        for j in range(self.__graph_constant.get_signals_amount()):
            current_line = current_line + f"{self.__graph_constant.get_current_ys(j)[i]:>30}"
        current_line = current_line + "\n"
        return current_line

    def __generate_file_name(self, start_time: Time, finish_time: Time):
        d = deleteAndFindLabel(start_time, finish_time, self.get_patient_name()).gen_file_name()
        return self.__file_direction + "/" + str(d)

    # check if all input info correct and init data, what must be deleted
    def delete_data(self, start_t: Time, finish_t: Time, what_to_delete: List = []):
        if len(what_to_delete) < 1:
            self.__write_data(start_t, finish_t)
            return True
        what_to_delete.sort(key=lambda x: x[0].get_seconds())

        for i in range(len(what_to_delete) - 1):
            if what_to_delete[i][1] > what_to_delete[i + 1][0]:
                raise Exception("Input times period can not contain another input period")

        self.__need_to_delete = what_to_delete
        if self.__need_to_delete[-1][1] > finish_t or self.__need_to_delete[0][0] < start_t:
            raise Exception("general time period must be greater than deleted period;")
        self.__write_data(start_t, finish_t)
        return True

    # function to draw graph
    def make_graph(self, start_time: Time, finish_time: Time):
        xs1, ys1 = self.read_data(start_time, finish_time)
        self.__graph_constant.min_fin_time = start_time
        self.__graph_constant.max_fin_time = Time(finish_time.hours,
                                                  finish_time.minutes - variables.GraphConstant.delta_time / 60,
                                                  finish_time.seconds,
                                                  finish_time.milis)
        self.__graph_constant.start_init(xs1, ys1)
        start_plot(self.__graph_constant, start_time, finish_time)

    def get_current_file_dir(self):
        return self.__file_direction


if __name__ == "__main__":
    autoDelGraph = autoDeleteGraph()
    start = Time(1, 0, 0, 0)
    finish = Time(1, 12, 0, 0)

    # need_to_del = []
    # need_to_del.append([Time(_hour=0, _minute=0, _sec=40, _milis=0), Time(_hour=0, _minute=0, _sec=50, _milis=0)])
    # need_to_del.append([Time(_hour=0, _minute=0, _sec=0, _milis=0), Time(_hour=0, _minute=0, _sec=10, _milis=0)])
    # need_to_del.append([Time(_hour=0, _minute=0, _sec=20, _milis=0), Time(_hour=0, _minute=0, _sec=30, _milis=0)])
    autoDelGraph.delete_data(start, finish)
    autoDelGraph.make_graph(start, finish)
