import fileManager as fm

import container_Manager as cm

file_dir = "D:/holter_files/2@1951-01-31.edf"
n = cm.Container(file_dir)

inp_list = []
time_list = []
# n.filling_containers()
n.writeFileToList1(inp_list, time_list, 0)
print(inp_list[0:10])

print(time_list[0:10])

# cm.container_filling(1, 1)
