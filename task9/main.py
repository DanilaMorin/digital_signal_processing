import matplotlib.pyplot as plot
import math
import numpy as np
from scipy import signal


def _EXIT_():
    print('Выход..')
    exit(0)


def getResult():
    order_of_the_filter = 7

    signal_1 = np.concatenate((np.zeros(30), signal.square(np.linspace(0, 60, 1024))))
    spectr_1 = np.fft.fft(signal_1)

    signal_2 = np.concatenate((np.zeros(30), signal.square(np.linspace(0, 60, 1024))))
    b1, a1 = signal.butter(order_of_the_filter, 0.05, analog=False, btype='lowpass')
    imp_ff_1 = signal.filtfilt(b1, a1, signal_2)
    spectr_2 = np.fft.fft(imp_ff_1)

    return {'spectr_1': spectr_1, 'signal_1': signal_1, 'spectr_2': spectr_2, 'signal_2': imp_ff_1}



if __name__ == "__main__":
    print('run task9')
    data = getResult()
    plot.subplot(221)
    plot.plot(data['signal_1'])
    plot.subplot(222)
    plot.plot(np.abs(data['spectr_1'][:100]))
    plot.subplot(223)
    plot.plot(data['signal_2'])
    plot.subplot(224)
    plot.plot(np.abs(data['spectr_2'][:100]))
    plot.show()