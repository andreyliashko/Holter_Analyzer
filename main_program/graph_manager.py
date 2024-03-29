import os
import numpy as np
import pyautogui
import matplotlib.pyplot as plt
import pylab
from matplotlib.widgets import (
    Button,
    Slider,
    CheckButtons
)

import pyedflib

from main_program import (
    static_methods,
    container_manager as cm,
    file_manager as fm,
)
from main_program.Time import Time
from start_module import variables

import matplotlib

matplotlib.use('Qt5Agg')

draw_first_plot = True
draw_second_plot = False
draw_third_plot = False
c = ['black', 'orange', 'red']


class Graph:

    def __init__(self):
        self.delta_time = variables.GraphConstant.delta_time
        self.startTime = 0
        self.finishTime = self.startTime + self.delta_time
        self.signals_in_file = pyedflib.EdfReader(variables.FilesConstant.file_directory).signals_in_file
        self.current_xs = []
        self.current_ys = []
        self.prev_clicked = 1
        for i in range(self.signals_in_file):
            self.current_ys.append([])
        self.lim = 0
        self.on_changed_sign = variables.FilesConstant.current_signal
        self.file_n = ""
        self.min_fin_time: Time = Time(0, 0, 0, 0)
        self.max_fin_time: Time = Time(1, 11, 0, 0)

    def get_current_ys(self, s=variables.FilesConstant.current_signal):
        return self.current_ys[s]

    def file_init(self):
        self.file_n = variables.GraphConstant.gen_files_dir
        if not os.path.isdir(self.file_n):
            os.mkdir(self.file_n)
        mas = str.split(variables.FilesConstant.file_directory, "/")
        n = str(mas[len(mas) - 1])
        n = n[0:len(n) - 4]
        self.file_n = self.file_n + "/" + n
        if not os.path.isdir(self.file_n):
            os.mkdir(self.file_n)

    def start_init(self, inp_xs=None, inp_ys=None):
        if inp_xs and inp_ys:
            self.current_xs = inp_xs
            self.current_ys = inp_ys
            self.startTime = self.current_xs[0]
            self.finishTime = self.startTime + self.delta_time
        else:
            n = cm.Container(variables.FilesConstant.file_directory)
            for i in range(self.signals_in_file - 1):
                n.write_file_to_list(self.current_ys[i], i)

            n.write_file_to_list_and_date(self.current_ys[self.signals_in_file - 1], self.current_xs,
                                          self.signals_in_file - 1)

        limit = (static_methods.prediction_limits(self.get_current_ys(), 8))
        limit[0] = np.abs(limit[0])
        limit[1] = np.abs(limit[1])
        self.lim = np.max(limit)

        self.file_init()

    def init_value(self, x_s, y_s):

        current_position = 0
        while current_position < len(self.current_xs) and self.current_xs[current_position] < self.startTime:
            current_position = current_position + 1
        while current_position < len(self.current_xs) and self.current_xs[current_position] <= self.finishTime:
            x_s.append((self.current_xs[current_position]) - self.startTime)
            y_s.append(self.get_current_ys(self.on_changed_sign)[current_position])
            current_position = current_position + 1

    def init_to_file(self, x_s, yn_s):
        current_position = 0
        while self.current_xs[current_position] < self.startTime:
            current_position = current_position + 1
        while self.current_xs[current_position] <= self.finishTime:
            x_s.append((self.current_xs[current_position]) - self.startTime)
            for i in range(self.signals_in_file):
                yn_s[i].append(self.get_current_ys(i)[current_position])
            current_position = current_position + 1

    def gen_files(self):

        next_path = self.file_n + "/" + str(static_methods.sec_to_time_short(self.startTime))
        if not os.path.isdir(next_path):
            os.mkdir(next_path)
        global sign_slider
        s = self.on_changed_sign
        for i in range(self.signals_in_file):
            self.on_changed_sign = i
            sign_slider.set_val(i)
            self.redraw_figure()
            fig.savefig(next_path + "/" + "signal" + str(
                self.on_changed_sign) + variables.FilesConstant.screen_type)
        self.on_changed_sign = s
        sign_slider.set_val(s)
        x_s0 = []
        y_s_n = []
        for i in range(self.signals_in_file):
            y_s_n.append([])
        self.init_to_file(x_s0, y_s_n)
        start_t = static_methods.sec_to_time_short(self.startTime)
        finish_t = static_methods.sec_to_time_short(self.finishTime)
        for i in range(self.signals_in_file):
            fm.save_input_container(next_path, "signal" + str(i) + ".txt", start_t, finish_t, y_s_n[i])

    def redraw_figure(self):
        x = []
        y = []
        self.init_value(x, y)
        while len(x) <= 0:
            self.startTime += self.delta_time * self.prev_clicked
            self.finishTime += self.delta_time * self.prev_clicked
            self.init_value(x, y)
        self.prev_clicked = 1

        # here i need to make multiple figure from 1
        pos = 1
        ax1.clear()
        global draw_first_plot, draw_second_plot, draw_third_plot, c
        ax1.plot([0, self.delta_time], [0, 0], linewidth=0.5, color='lightblue')
        while pos < len(x):
            while pos < len(x) and x[pos] - x[pos - 1] >= 1:
                pos += 1
            start_pos = pos
            while pos < len(x) and x[pos] - x[pos - 1] < 1:
                pos = pos + 1

            if draw_first_plot:
                ax1.plot(x[start_pos:pos], y[start_pos:pos], linewidth=0.5, color=c[0])
            if draw_second_plot:
                ax1.plot(x[start_pos:pos], static_methods.normalize_zscore(y[start_pos:pos]), linewidth=0.5, color=c[1])
            if draw_third_plot:
                ax1.plot(x[start_pos:pos], static_methods.normalize_mean(y[start_pos:pos]), linewidth=0.5, color=c[2])

        ax1.set_ylim([-self.lim, self.lim])
        add_time(ax1, static_methods.convert_seconds_to_time(self.startTime))
        pylab.draw()

    def change_slider(self):
        hour = self.startTime // 3600
        hour_slider.set_val(hour)
        minute_slider.set_val((self.startTime - hour * 3600) // 60)
        self.redraw_figure()

    def next(self, event):
        if self.finishTime + self.delta_time <= self.current_xs[len(self.current_xs) - 1]:
            self.startTime = self.delta_time + self.startTime
            self.finishTime = self.delta_time + self.finishTime
            self.change_slider()

    def prev(self, event):
        self.prev_clicked = -1
        if self.startTime - self.delta_time >= self.min_fin_time.getSeconds():
            self.startTime = self.startTime - self.delta_time
            self.finishTime = self.finishTime - self.delta_time
            self.redraw_figure()
            self.change_slider()

    def save_to_file(self, event):
        self.gen_files()

    def set_time(self, hour, minute):
        self.startTime = hour * 3600 + minute * 60
        self.finishTime = self.startTime + self.delta_time

    def button_go_to(self, event):
        t: Time = Time(float(hour_slider.val), float(minute_slider.val), 0, 0)
        if t > self.max_fin_time:
            hour_slider.set_val(self.max_fin_time.hours)
            minute_slider.set_val(self.max_fin_time.minutes)
            self.set_time(self.max_fin_time.hours, self.max_fin_time.minutes)
            self.redraw_figure()
            return

        if t < self.min_fin_time:
            hour_slider.set_val(self.min_fin_time.hours)
            minute_slider.set_val(self.min_fin_time.minutes)
            self.set_time(self.min_fin_time.hours, self.min_fin_time.minutes)
            self.redraw_figure()
            return

        self.set_time(t.hours, t.minutes)
        self.redraw_figure()

    def sign_slider(self, event):
        global sign_slider
        self.on_changed_sign = sign_slider.val
        self.redraw_figure()

    def get_element_pos(self, value: int):
        return self.current_xs.index(value)

    def get_signals_amount(self):
        return self.signals_in_file


def add_time(ax, curr_time):
    ax.text(0.5, -0.125, curr_time,
            verticalalignment='bottom', horizontalalignment='center',
            transform=ax1.transAxes,
            color='green', fontsize=15)


def add_plot_menu():
    rax = pylab.axes([0.05, 0.32, 0.2, 0.15])
    global check
    global c
    check = CheckButtons(rax, ('y=x(t)', 'y=(x(t)-x_average)/sqrt(D)', 'y=(x(t)-x_min)/(x_max-x_min)'),
                         (draw_first_plot, draw_second_plot, draw_third_plot))
    [rec.set_color(c[i]) for i, rec in enumerate(check.labels)]


def func(label):
    if label == 'y=x(t)':
        global draw_first_plot
        draw_first_plot = not draw_first_plot
    elif label == 'y=(x(t)-x_average)/sqrt(D)':
        global draw_second_plot
        draw_second_plot = not draw_second_plot
    elif label == 'y=(x(t)-x_min)/(x_max-x_min)':
        global draw_third_plot
        draw_third_plot = not draw_third_plot
    global gr
    gr.redraw_figure()


slider_color_settings = {
    'color': 'Teal',
    'alpha': 0.8
}
button_color_settings = {
    'hovercolor': 'DarkOrange',
    'color': 'Orange'
}


def start_plot(g: Graph = None, st: Time = Time(0, 0, 0, 0), fin: Time = Time(24, 0, 0, 0)):
    global gr
    if g:
        gr = g
    else:
        gr = Graph()
        gr.start_init()

    screen_width, screen_height = pyautogui.size()

    # Розмір вікна, який ми бажаємо встановити
    window_width, window_height = screen_width, screen_height * 0.73
    global fig
    fig = plt.figure(figsize=(window_width / 100, window_height / 100), dpi=100)
    fig.subplots_adjust(0, 0, window_width, window_height)
    global ax1
    ax1 = fig.add_subplot()
    gr.redraw_figure()

    add_time(ax1, static_methods.convert_seconds_to_time(gr.startTime))

    fig.subplots_adjust(left=0.04, right=0.998, top=1.0, bottom=0.3)
    fig.canvas.manager.set_window_title('Holter Analyzer')

    axes_button_add = pylab.axes((0.675, 0.18, 0.3, 0.075))
    axes_button_remove = pylab.axes((0.06, 0.18, 0.3, 0.075))
    axes_button_save_to_file = pylab.axes((0.675, 0.075, 0.3, 0.075))
    axes_slider1 = pylab.axes((0.06, 0.1, 0.3, 0.075))
    axes_slider2 = pylab.axes((0.06, 0.05, 0.3, 0.075))
    axes_button_go_to = pylab.axes((0.4, 0.075, 0.25, 0.08))
    axes_sign_slider = pylab.axes((0.06, 0.0, 0.3, 0.075))

    button_add = Button(axes_button_add, label="Next", **button_color_settings)
    button_remove = Button(axes_button_remove, 'Previous', **button_color_settings)
    button_save_to_file = Button(axes_button_save_to_file, 'Save', **button_color_settings)
    if st != Time(0, 0, 0, 0):
        button_save_to_file = Button(axes_button_save_to_file, 'Save', color=(0, 0, 0, 0))
        button_save_to_file.active = False

    global hour_slider, minute_slider, sign_slider
    hour1, minute1 = st.time_for_sliders()
    hour2, minute2 = fin.time_for_sliders()

    hour_slider = Slider(axes_slider1, "HOURS: ", 0, hour2, 0, valstep=1, **slider_color_settings)
    minute_slider = Slider(axes_slider2, "MINUTES: ", 0, minute2, 0, valstep=1, **slider_color_settings)
    button_go_to = Button(axes_button_go_to, "Go to", **button_color_settings)
    sign_slider = Slider(axes_sign_slider, "SIGNAL: ", 0, gr.get_signals_amount() - 1, 0, valstep=1,
                         **slider_color_settings)
    sign_slider.set_val(variables.FilesConstant.current_signal)
    sign_slider.on_changed(gr.sign_slider)

    button_add.on_clicked(gr.next)
    button_remove.on_clicked(gr.prev)
    button_save_to_file.on_clicked(gr.save_to_file)
    button_go_to.on_clicked(gr.button_go_to)

    add_plot_menu()
    global check
    check.on_clicked(func)
    pylab.show()


if __name__ == "__main__":
    start_plot()
