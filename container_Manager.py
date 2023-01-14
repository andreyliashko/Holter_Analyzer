import os

import fileManager


class Container:

    def filling_containers(self):
        self.current_status = fileManager.createServiceFiles(self.dir)
        print("current status is " + str(self.current_status))

    def __init__(self, directory):
        self.dir = directory
        self.current_status = 0
        self.delta = 1
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
        self.points_number = num_list[1]
        self.time_duration = num_list[2]

    @staticmethod
    def getSecondsToTime(time_sec, points_in_sec):
        return str(time_sec / points_in_sec)

    def writeFileToList1(self, output_list, out_date, file_number=0):

        if not self.current_status:
            return 0
        reading_path = self.dir + fileManager.ending + str(file_number) + fileManager.file_type
        check_file = os.path.isfile(reading_path)
        if check_file:
            inp_file = open(reading_path)
            j = 0
            self.fill_input_param(inp_file.readline())
            point_in_second = (self.getPointsAmount() / self.time_duration)
            for i in inp_file:
                j = j + 1
                if j % self.delta == 0:
                    out_date.append(self.getSecondsToTime(j, point_in_second).strip())
                    output_list.append(i.strip())
            inp_file.close()
            print("container successfully filled...")
            return 1
        print("An error occurred")
        return 0

    # def getListFromFile(self, out_list2=None, from_index=0, to_index=10, file_number=0):
    #     if out_list2 is None:
    #         out_list2 = []
    #     out_service_list = []
    #     self.writeFileToList1(out_service_list, file_number)
    #     copy = out_service_list[from_index:to_index]
    #     return copy
    #     # return 0

    def getDuration(self):
        return self.time_duration

    def getPointsAmount(self):
        return self.points_number
