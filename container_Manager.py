import fileManager


class Container:
    def __init__(self, directory):
        self.dir = directory

    def filling_containers(self, inp_container):
        current_status = fileManager.createServiceFiles(self.dir)
        print("current status is " + str(current_status))
