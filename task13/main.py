import matplotlib.pyplot as plot
import numpy as np
from scipy import signal


def _EXIT_():
    print('Выход..')
    exit(0)


def getResult():

    signal_1 = np.concatenate((np.sin(np.linspace(0, 50, 150)), np.zeros(80)))
    signal_2 = np.sin(np.linspace(0, 50, 150))
    hann_window = signal.barthann(150)
    signal_with_hann_window = signal_2 * hann_window
    signal_with_hann_window = np.concatenate((signal_with_hann_window, np.zeros(80)))


    spectr = np.fft.fft(signal_1)
    spectr_with_spectr_hann = np.fft.fft(signal_with_hann_window)

    return {'signal_1': signal_1, 'spectr': spectr, 'changed_spectr': spectr_with_spectr_hann, 'signal_2': signal_with_hann_window}



if __name__ == "__main__":
    print('run task13')
    data = getResult()
    plot.subplot(221)
    plot.plot(data['signal_1'])
    plot.subplot(222)
    plot.plot(20*np.log10(np.abs(data['spectr'][:150])))
    plot.subplot(223)
    plot.plot(data['signal_2'])
    plot.subplot(224)
    plot.plot(20*np.log10(np.abs(data['changed_spectr'][:150])))
    plot.show()