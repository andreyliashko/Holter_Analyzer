import matplotlib.pyplot as plt
import matplotlib.animation as animation

plt.style.use('dark_background')

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

status = 1


def animate(i):
    data = open('stock.txt', 'r').read()
    lines = data.split('\n')
    xs = []
    ys = []

    for line in lines:
        x, y = line.split(',')  # Отделяем дату от цены
        xs.append(x)
        ys.append(float(y))

    ax1.clear()
    ax1.plot(xs, ys)

    plt.xlabel('Time')
    plt.ylabel('Ritm')
    plt.title('Cardioritm')



animate(1)
plt.show()
