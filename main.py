import StaticMethods
import fileManager as fm

import container_Manager as cm
import graph_Manager as gm

file_dir = "D:/holter_files/2@1951-01-31.edf"
n = cm.Container(file_dir)

inp_list = []
time_list = []
n.writeFileToList1(inp_list, time_list, 0)
gm.animate(time_list, inp_list, 60, 120)

gm.animate(time_list, inp_list, 0, 60)
# cm.container_filling(1, 1)
# print(StaticMethods.MainMethods.predictionLimits(inp_list, 4))
