import matplotlib.pyplot as plot
import numpy as np
from scipy import signal


def _EXIT_():
    print('Выход..')
    exit(0)


def getResult():
    samples_1 = signal.chirp(np.linspace(0, 11, 150), f0=1, f1=6, t1=10, method='linear')
    ac_a_conv_f_1 = signal.convolve(samples_1, samples_1, mode='full')
    ac_acf_1 = np.correlate(samples_1, samples_1, mode='full')

    samples_2 = signal.chirp(np.linspace(0, 11, 150), f0=6, f1=1, t1=10, method='linear')
    ac_s_conv_f_2 = signal.convolve(samples_2[::-1], samples_2[::-1], mode='full')
    ac_acf_2 = np.correlate(samples_2[::-1], samples_2[::-1], mode='full')

    return {'ac_a_conv_f_1': ac_a_conv_f_1, 'samples_1': samples_1, 'ac_acf_1': ac_acf_1, 'samples_2': samples_2, 'ac_s_conv_f_2': ac_s_conv_f_2, 'ac_acf_2': ac_acf_2 }


if __name__ == "__main__":
    print('run task16')
    P = 15
    N = 100
    data = getResult(P, N)
    plot.subplot(2, 3, 1)
    plot.plot(data['samples_1'])
    plot.title('ac_white_noise')

    plot.subplot(2, 3, 5)
    plot.plot(data['ac_s_conv_f_2'])
    plot.title('ac_sin')

    plot.subplot(2, 3, 2)
    plot.plot(data['ac_acf_1'])
    plot.title('ac_square')

    plot.subplot(2, 3, 3)
    plot.plot(data['ac_a_conv_f_1'])
    plot.title('ac_sin')

    plot.subplot(2, 3, 4)
    plot.plot(data['samples_2'])
    plot.title('ac_square')

    plot.subplot(2, 3, 6)
    plot.plot(data['ac_acf_2'])
    plot.title('ac_lfm')

    plot.show()
