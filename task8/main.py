import matplotlib.pyplot as plot
import math
import numpy as np
from scipy import signal


def _EXIT_():
    print('Выход..')
    exit(0)


def getResult():
    signal_1 = np.concatenate((np.zeros(30), signal.square(np.linspace(0, 60, 1024))))
    spectr = np.fft.fft((signal_1))
    changed_spektr = np.fft.fft(np.real(signal_1))
    changed_spektr[257:765] = 0
    signal_2 = np.fft.ifft(changed_spektr)

    return {'signal_1': signal_1, 'spectr': spectr, 'changed_spektr': changed_spektr, 'signal_2': signal_2}



if __name__ == "__main__":
    print('run task8')
    data = getResult()
    plot.subplot(221)
    plot.plot(data['signal_1'])
    plot.subplot(222)
    plot.plot(np.abs(data['spectr']))
    plot.subplot(223)
    plot.plot(data['signal_2'])
    plot.subplot(224)
    plot.plot(np.abs(data['changed_spektr']))
    plot.show()