import os
import sys
from main_program.Time import Time
from main_program.autoDeleteGraph import *
from main_program import graph_Manager as gm

if __name__ == "__main__":
    # gm.start_plot()
    autoDelGraph = autoDeleteGraph()
    start = Time()
    finish = Time(2, 0, 0, 0)

    # times period from file can be deleted only once. comment this code after first use
    # start code
    need_to_del = []
    need_to_del.append([Time(_hour=0, _minute=0, _sec=40, _milis=0), Time(_hour=0, _minute=0, _sec=50, _milis=0)])
    need_to_del.append([Time(_hour=0, _minute=0, _sec=0, _milis=0), Time(_hour=0, _minute=0, _sec=10, _milis=0)])
    need_to_del.append([Time(_hour=0, _minute=0, _sec=20, _milis=0), Time(_hour=0, _minute=0, _sec=30, _milis=0)])
    autoDelGraph.deleteData(start, finish, need_to_del)
    # end of code

    autoDelGraph.make_graph(start, finish)