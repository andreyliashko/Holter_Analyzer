import os
import sys

from start_module import Variables
from main_program import fileManager


class Container:

    def filling_containers(self):
        self.current_status = fileManager.createServiceFiles(self.dir)
        print("current status is " + str(self.current_status))

    def __init__(self, directory):
        self.dir = directory
        self.current_status = 0
        self.delta = Variables.FilesConstant.get_points_in_one_sec
        self.filling_containers()
        self.points_number = 0
        self.time_duration = 0

    # get operation time and length
    def fill_input_param(self, input_line):

        num_list = []

        num = ''
        for char in input_line:
            if char.isdigit():
                num = num + char
            else:
                if num != '':
                    num_list.append(int(num))
                    num = ''
        if num != '':
            num_list.append(int(num))
        self.n_amount = num_list[0]
        self.points_number = num_list[1]
        self.time_duration = num_list[2]

    @staticmethod
    def getSecondsToTime(time_sec, points_in_sec):
        return str(time_sec / points_in_sec)

    def writeFileToListAndDate(self, output_list0, out_date, file_number):

        if not self.current_status:
            return 0
        reading_path = self.dir + fileManager.ending + str(file_number) + Variables.FilesConstant.text_type
        check_file = os.path.isfile(reading_path)
        if check_file:
            inp_file = open(reading_path)
            j = -1
            self.fill_input_param(inp_file.readline())
            point_in_second = (self.getPointsAmount() / self.time_duration)
            for i in inp_file:
                j = j + 1
                if j % self.delta == 0:
                    out_date.append(float(self.getSecondsToTime(j, point_in_second).strip()))
                    output_list0.append(float(i.strip()))
            inp_file.close()
            print("container " + str(file_number) + " successfully filled...")
            return 1
        print("An error occurred")
        return 0

    def writeFileToList(self, output_list0, file_number):

        if not self.current_status:
            return 0
        reading_path = self.dir + fileManager.ending + str(file_number) + Variables.FilesConstant.text_type
        check_file = os.path.isfile(reading_path)
        if check_file:
            inp_file = open(reading_path)
            j = -1
            self.fill_input_param(inp_file.readline())
            point_in_second = (self.getPointsAmount() / self.time_duration)
            for i in inp_file:
                j = j + 1
                if j % self.delta == 0:
                    output_list0.append(float(i.strip()))
            inp_file.close()
            print("container " + str(file_number) + " successfully filled...")
            return 1
        print("An error occurred")
        return 0

    def getDuration(self):
        return self.time_duration

    def getPointsAmount(self):
        return self.points_number
