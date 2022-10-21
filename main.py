import fileManager as fm

import container_Manager as cm
file_dir = "D:/holter_files/2@1951-01-31.edf"
n=cm.Container(file_dir)
cont=""
n.filling_containers(cont)
# cm.container_filling(1, 1)