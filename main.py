import fileManager as fm

import container_Manager as cm

file_dir = "D:/holter_files/2@1951-01-31.edf"
n = cm.Container(file_dir)

inp_list = []
# n.filling_containers()
inp_list = n.writeFileToList()
for i in inp_list:
    print(i)
# cm.container_filling(1, 1)

