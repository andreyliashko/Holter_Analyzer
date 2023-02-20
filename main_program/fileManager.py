import os.path
import numpy as np
import pyedflib as edfl

from start_module import Variables

ending = "_generated_"


def write_file(dir_name):
    fr = edfl.EdfReader(dir_name)
    n = fr.signals_in_file

    sigbufs = np.zeros((n, fr.getNSamples()[0]))
    for i in np.arange(n):
        sigbufs[i, :] = fr.readSignal(i)

    for i in range(n):
        with open(dir_name + ending + str(i) + Variables.FilesConstant.text_type, 'w') as f:

            f.write("signal=" + str(i) + "; points=" + str(len(sigbufs[i])) + "; duration=" + str(
                fr.getFileDuration()) + "\n")

            for j in range(len(sigbufs[i])):
                f.write(str(sigbufs[i][j]) + "\n")
        print(dir_name + ending + str(i) + Variables.FilesConstant.text_type + " just created")


def createServiceFiles(file_dir):
    if not os.path.isfile(file_dir):
        print("file doesn`t exist")
        return -1
    is_all_created = True
    n = edfl.EdfReader(file_dir).signals_in_file
    for i in range(n):
        check_file = os.path.isfile(file_dir + ending + str(i) + Variables.FilesConstant.text_type)
        if not check_file:
            write_file(file_dir)
            is_all_created = False
    if is_all_created:
        print("files had been created")
    else:
        print("computing!\n" + "please wait")
    return 1


def save_input_container(file_directory, file_name, st_time, fin_time, y_s):
    if not os.path.isdir(file_directory):
        print("incorrect file directory;")
        return 0
    with open(file_directory + "/" + file_name, 'w') as f:
        f.write("START TIME: " + st_time + "\n")
        f.write("FINISH TIME: " + fin_time + "\n")
        for i in y_s:
            f.write(str(i) + "\n")
    path = os.path.join(file_directory + "/" + file_name)
    print("saved to "+path)
