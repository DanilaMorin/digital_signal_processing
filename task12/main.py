import matplotlib.pyplot as plot
import numpy as np
from scipy import signal


def _EXIT_():
    print('Выход..')
    exit(0)


def getResult():
    increment = 2
    signal_1 = signal.sawtooth(np.linspace(0, 60, 1024))
    spectr = np.fft.fft((signal_1))
    signal_2 = signal_1
    for i in range(0, len(signal_2) * increment, increment):
        signal_2 = np.insert(signal_2, i, 0)
    changed_spectr = np.fft.fft(signal_2)

    return {'signal_1': signal_1, 'spectr': spectr, 'changed_spectr': changed_spectr, 'signal_2': signal_2}



if __name__ == "__main__":
    print('run task12')
    data = getResult()
    plot.subplot(221)
    plot.plot(data['signal_1'])
    plot.subplot(222)
    plot.plot(np.abs(data['spectr']))
    plot.subplot(223)
    plot.plot(data['signal_2'])
    plot.subplot(224)
    plot.plot(np.abs(data['changed_spectr']))
    plot.show()