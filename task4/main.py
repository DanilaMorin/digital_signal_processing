import matplotlib.pyplot as plot
import math
import numpy as np
from scipy import signal


def _EXIT_():
    print('Выход..')
    exit(0)


def INPUT():
    global str1
    str1 = input('ВВОД P: ')


def add_value_in_register(summator, value):
    for i in range(len(summator) - 1):
        summator[i] = summator[i + 1]
    summator[len(summator) - 1] = value

def get_summ(summator):
    result = 0
    for value in summator:
        result += value

    return result

def getResult(N, P):
    k = P / N
    # пустые массивы значений
    X = np.array(0)
    S = np.array(0)
    # частота пропускания и частота заграждения
    wp, ws = 0.2, 0.3
    # усиление в полосе пропускания и подавление вне её
    gpass, gstop = 0.1, 50.0

    b, a = signal.iirdesign(wp, ws, gpass, gstop, analog=False, ftype='butter', output='ba')
    w, h = signal.freqz(b, a)

    x_values = w/np.pi
    y_values = 20*np.log10(abs(h))
    return {'x_values': x_values, 'y_values': y_values}


def plotGraf(data, x_label="x_values", y_label='y_values'):
    data_x = data[x_label]
    data_y = data[y_label]
    plot.ylabel('рис 1')
    plot.plot(data_x, data_y)




if __name__ == "__main__":
    N = 100
    print('run task4')
    #INPUT()
    #P = int(str1)
    P = 15
    data = getResult(N, P)
    plot.subplot(311)
    plotGraf(data)
    plot.show()