import random
import matplotlib
import math
import tkinter as Tk
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

matplotlib.use('TkAgg')

def getResult(N, P):
    y_values = []
    x_values = []
    for i in range(0, N):
        x_values.append(i)
        y_values.append(math.sin(2 * 3.14 * i * P / N))

    return {'x_values': x_values, 'y_values': y_values}

def update():
    # pos = s_time.val
    # ax.axis([pos, pos + 10, 20, 40])
    # fig.canvas.draw_idle()
    fig.clear()
    ax = fig.add_subplot(111)
    result = getResult(100, 30)
    ax.plot(result.get('x_values'), result.get('y_values'))
    fig.canvas.draw_idle()

root = Tk.Tk()
root.wm_title("Embedding in TK")
fig = plt.Figure()
canvas = FigureCanvasTkAgg(fig, root)
# canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

ax = fig.add_subplot(111)
fig.subplots_adjust(bottom=0.25)

#
button = Tk.Button(root)
button["text"] = "Закрыть"
button["command"] = root.quit
button["font"] = "-*-terminus-*-r-*-*-12-*-*-*-*-*-*-*"
button.pack()
#
button = Tk.Button(root)
button["text"] = "Update"
button["command"] = update
button["font"] = "-*-terminus-*-r-*-*-12-*-*-*-*-*-*-*"
button.pack()
#



#y_values = [random.randrange(20, 40, 1) for _ in range(40)]
#x_values = [i for i in range(40)]

#ax.axis([0, 9, 20, 40])

result = getResult(100, 20)

ax.plot(result.get('x_values'), result.get('y_values'))
fig.canvas.draw_idle()
# ax_time = fig.add_axes([0.12, 0.1, 0.78, 0.03])
# s_time = Slider(ax_time, 'Time', 0, 30, valinit=0)





# s_time.on_changed(update)



Tk.mainloop()
