import os

import fileManager


class Container:

    def filling_containers(self):
        self.current_status = fileManager.createServiceFiles(self.dir)
        print("current status is " + str(self.current_status))

    def __init__(self, directory):
        self.dir = directory
        self.current_status = 0
        self.delta = 5
        self.filling_containers()

    def writeFileToList1(self, output_list=None, file_number=0):

        if output_list is None:
            output_list = []
        if not self.current_status:
            return 0
        reading_path = self.dir + fileManager.ending + str(file_number) + fileManager.file_type
        check_file = os.path.isfile(reading_path)
        if check_file:
            inp_file = open(reading_path)
            j = 0

            for i in inp_file:
                j = j + 1
                if j % self.delta == 0:
                    # print("a"+i.strip()+"a")
                    output_list.append(i.strip())
            inp_file.close()
            print("container successfully filled...")
            return 1
        print("An error occurred")
        return 0

    def writeFileToList(self, out_list2=None, from_index=0, to_index=10, file_number=0):
        if out_list2 is None:
            out_list2 = []
        out_service_list = []
        self.writeFileToList1(out_service_list, file_number)
        copy = out_service_list[from_index:to_index]
        return copy
        # return 0
