import numpy as np
import matplotlib.pyplot as plt


def init_graph():
    x = np.arange(-10, 10.01, 0.01)
    plt.plot(x, x)
    plt.show()
