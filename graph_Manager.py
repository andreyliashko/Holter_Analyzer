import StaticMethods
import numpy as np
import container_Manager as cm
import matplotlib.pyplot as plt
import pylab
# Импортируем класс кнопки
from matplotlib.widgets import Button

current_xs = []
current_ys = []
file_dir = "D:/holter_files/2@1951-01-31.edf"
n = cm.Container(file_dir)
n.writeFileToList1(current_ys, current_xs, 0)

limit = (StaticMethods.predictionLimits(current_ys, 5))
limit[0] = np.abs(limit[0])
limit[1] = np.abs(limit[1])
lim = np.max(limit)


class Graph:
    startTime = 0
    finishTime = 60

    def init_value(self, x_s, y_s):

        current_position = 0
        while current_xs[current_position] < self.startTime:
            current_position = current_position + 1
        while current_xs[current_position] <= self.finishTime:
            x_s.append(current_xs[current_position])
            y_s.append(current_ys[current_position])
            current_position = current_position + 1

    def next(self, event):

        self.startTime = 60 + self.startTime
        self.finishTime = 60 + self.finishTime
        x = []
        y = []
        self.init_value(x, y)
        global ax1
        ax1.clear()
        ax1.plot(x, y)
        global lim
        ax1.set_ylim([-lim, lim])
        pylab.draw()

    def prev(self, event):
        if self.startTime-60>=0:
            self.startTime = self.startTime - 60
            self.finishTime = 60 + self.finishTime - 60
            x = []
            y = []
            self.init_value(x, y)
            global ax1
            ax1.clear()
            ax1.plot(x, y)
            global lim
            ax1.plot([self.startTime, self.finishTime], [500, 500], linewidth=1, color="red", linestyle="--")

            ax1.set_ylim([-lim, lim])
            pylab.draw()


gr = Graph()
fig = plt.figure(figsize=(15,8))
ax1 = fig.add_subplot()
ax1.set_ylim([-lim, lim])
ax1.title.set_text('First Plot')
f1=[]
f2=[]
gr.init_value(f1,f2)
my_line = ax1.plot(f1, f2)
# Оставим снизу от графика место для виджетов
fig.subplots_adjust(left=0.07, right=0.95, top=0.95, bottom=0.2)

# Создадим ось для кнопки
axes_button_add = pylab.axes([0.65, 0.08, 0.25, 0.075])
axes_button_remove = pylab.axes([0.1, 0.08, 0.25, 0.075])


# Создание кнопки
button_add = Button(axes_button_add, 'Добавить')
button_remove = Button(axes_button_remove, 'Добавить')

# !!! Подпишемся на событие обработки нажатия кнопки
button_add.on_clicked(gr.next)
button_remove.on_clicked(gr.prev)

# Добавить график
# addPlot(graph_axes, current_sigma, current_mu)

pylab.show()
