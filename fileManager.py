import os.path
import numpy as np
import pyedflib as edfl

ending = "_generated_"
file_type = ".txt"


def write_file(dir_name):
    fr = edfl.EdfReader(dir_name)
    n = fr.signals_in_file

    sigbufs = np.zeros((n, fr.getNSamples()[0]))
    for i in np.arange(n):
        sigbufs[i, :] = fr.readSignal(i)

    for i in range(n):
        with open(dir_name + ending + str(i) + file_type, 'w') as f:
            for j in range(len(sigbufs[i])):
                f.write(str(sigbufs[i][j]) + "\n")
        print(dir_name + ending + str(i) + file_type + " just created")


def createServiceFiles(file_dir):
    if not os.path.isfile(file_dir):
        print("file doesn`t exist")
        return -1
    is_all_created = True
    n = edfl.EdfReader(file_dir).signals_in_file
    for i in range(n):
        check_file = os.path.isfile(file_dir + ending + str(i) + file_type)
        if not check_file:
            write_file(file_dir)
            is_all_created = False
    if is_all_created:
        print("files had been created")
    else:
        print("computing!\n" + "please wait")
    return 1
