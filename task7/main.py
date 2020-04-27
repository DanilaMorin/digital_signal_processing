import matplotlib.pyplot as plot
import math
import numpy as np
from scipy import signal


def _EXIT_():
    print('Выход..')
    exit(0)


def getResult():
    order_of_the_filter = 50

    signal_1 = np.sin(np.linspace(0, 20, 500))
    b1, a1 = signal.butter(order_of_the_filter, 0.30, analog=False)
    imp_ff_1 = signal.filtfilt(b1, a1, signal_1)

    signal_2 = np.sin(np.linspace(0, 20, 500))
    b2, a2 = signal.butter(2, 0.30, analog=False)
    imp_ff_2 = signal.filtfilt(b2, a2, signal_2)
    for i in range(int(np.log2(order_of_the_filter))):
        imp_ff_2 = signal.filtfilt(b2, a2, imp_ff_2)

    return {'signal1': imp_ff_1, 'signal2': imp_ff_2}



if __name__ == "__main__":
    print('run task7')
    data = getResult()
    plot.subplot(311)
    plot.plot(data['signal1'])
    plot.subplot(312)
    plot.plot(data['signal2'])
    plot.show()