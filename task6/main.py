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
    wp, ws = 0.01, 0.3
    # усиление в полосе пропускания и подавление вне её
    gpass, gstop = 0.1, 50.0

    order_of_the_filter = 10

    b, a = signal.iirfilter(order_of_the_filter, [wp, ws], gpass, gstop, analog=False, ftype='butter', output='ba')
    w, h = signal.freqz(b, a)

    b2 = signal.firwin(50, [wp, ws], pass_zero=False)
    w2, h2 = signal.freqz(b2)

    x_values_sig1 = w/np.pi
    y_values_sig1 = 20*np.log10(abs(h))

    x_values_sig2 = w2 / np.pi
    y_values_sig2 = 20 * np.log10(abs(h2))

    return {'x_values_sig1': x_values_sig1, 'y_values_sig1': y_values_sig1, 'x_values_sig2': x_values_sig2, 'y_values_sig2': y_values_sig2}


def plotGraf(data, x_label="x_values", y_label='y_values'):
    data_x = data[x_label]
    data_y = data[y_label]
    plot.ylabel('рис 1')
    plot.plot(data_x, data_y)




if __name__ == "__main__":
    N = 100
    print('run task6')
    P = 15
    data = getResult(N, P)
    plot.subplot(311)
    plotGraf(data, 'x_values_sig1', 'y_values_sig1')
    plot.subplot(312)
    plotGraf(data, 'x_values_sig2', 'y_values_sig2')
    plot.show()