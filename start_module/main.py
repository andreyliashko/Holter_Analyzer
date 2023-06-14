import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '../main_program'))
import graph_Manager as gm

if __name__ == "__main__":
    gm.start_plot()
