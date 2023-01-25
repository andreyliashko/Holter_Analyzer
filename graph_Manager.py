from tkinter import font

from numpy import delete

import StaticMethods
import numpy as np
import container_Manager as cm
import matplotlib.pyplot as plt
import pylab
# Импортируем класс кнопки
from matplotlib.widgets import Button


class Graph:
    delta_time = 60
    startTime = 0
    finishTime = startTime + delta_time

    current_xs = []
    current_ys = []
    lim = 0

    def start_init(self):
        file_dir = "D:/holter_files/2@1951-01-31.edf"
        n = cm.Container(file_dir)
        n.writeFileToList1(self.current_ys, self.current_xs, 0)

        limit = (StaticMethods.predictionLimits(self.current_ys, 8))
        limit[0] = np.abs(limit[0])
        limit[1] = np.abs(limit[1])
        self.lim = np.max(limit)

    def init_value(self, x_s, y_s):

        current_position = 0
        while self.current_xs[current_position] < self.startTime:
            current_position = current_position + 1
        while self.current_xs[current_position] <= self.finishTime:
            x_s.append((self.current_xs[current_position]) - self.startTime)
            y_s.append(self.current_ys[current_position])
            current_position = current_position + 1

    def next(self, event):
        if self.finishTime + self.delta_time <= self.current_xs[len(self.current_xs)-1]:
            self.startTime = self.delta_time + self.startTime
            self.finishTime = self.delta_time + self.finishTime
            x = []
            y = []
            self.init_value(x, y)
            global ax1
            ax1.clear()
            ax1.plot(x, y, linewidth=0.5, color="black")

            ax1.set_ylim([-self.lim, self.lim])
            # ax1.set_xlabel('Total debt')
            add_time(ax1, StaticMethods.convertSecondsToTime(self.startTime))
            pylab.draw()

    def prev(self, event):
        if self.startTime - self.delta_time >= 0:
            self.startTime = self.startTime - self.delta_time
            self.finishTime = self.finishTime - self.delta_time
            x = []
            y = []
            self.init_value(x, y)
            global ax1
            ax1.clear()
            ax1.plot(x, y, linewidth=0.5, color="black")
            # ax1.plot([self.startTime, self.finishTime], [500, 500], linewidth=1, color="red", linestyle="--")
            add_time(ax1, StaticMethods.convertSecondsToTime(self.startTime))
            ax1.set_ylim([-self.lim, self.lim])
            pylab.draw()


def add_time(ax, curr_time):
    ax.text(0.5, -0.125, curr_time,
            verticalalignment='bottom', horizontalalignment='center',
            transform=ax1.transAxes,
            color='green', fontsize=15)


def start_plot():
    gr = Graph()
    gr.start_init()
    global fig
    fig = plt.figure(figsize=(15, 8))
    global ax1
    ax1 = fig.add_subplot()
    ax1.set_ylim([-gr.lim, gr.lim])
    ax1.title.set_text('First Plot')
    f1 = []
    f2 = []
    gr.init_value(f1, f2)
    my_line = ax1.plot(f1, f2, linewidth=0.5, color="black")
    # ax1.set_xlabel('Time [s]', fontsize='large', fontweight='bold')
    add_time(ax1, StaticMethods.convertSecondsToTime(gr.startTime))

    # Оставим снизу от графика место для виджетов
    fig.subplots_adjust(left=0.07, right=0.95, top=0.95, bottom=0.2)

    # Создадим ось для кнопки
    axes_button_add = pylab.axes([0.65, 0.08, 0.25, 0.075])
    axes_button_remove = pylab.axes([0.11, 0.08, 0.25, 0.075])

    # Создание кнопки
    button_add = Button(axes_button_add, 'Далі')
    button_remove = Button(axes_button_remove, 'Назад')

    # !!! Подпишемся на событие обработки нажатия кнопки
    button_add.on_clicked(gr.next)
    button_remove.on_clicked(gr.prev)

    # Добавить график
    pylab.show()
