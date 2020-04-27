import matplotlib.pyplot as plot
import numpy as np
from scipy import signal


def _EXIT_():
    print('Выход..')
    exit(0)


def getResult():
    mean = 0
    std = 1
    num_samples = 150
    samples = np.random.normal(mean, std, size=num_samples)
    ac_white_noise = np.correlate(samples, samples, mode='full')

    samples = np.sin(np.linspace(0, 50, 150))
    ac_sin = np.correlate(samples, samples, mode='full')

    samples = signal.square(np.linspace(0, 50, 150))
    ac_square = np.correlate(samples, samples, mode='full')

    samples = signal.chirp(np.linspace(0, 50, 150), f0=6, f1=1, t1=10, method='linear')
    samplesq = signal.chirp(np.linspace(0, 15, 800), f0=5, f1=1, t1=10, method='linear')
    ac_lfm = np.correlate(samples, samples, mode='full')

    return {'ac_white_noise': ac_white_noise, 'ac_sin': ac_sin, 'samplesq': samplesq, 'ac_lfm': ac_lfm}



if __name__ == "__main__":
    print('run task14')
    data = getResult()
    plot.subplot(221)
    plot.plot(data['ac_white_noise'])
    plot.subplot(222)
    plot.plot(data['ac_sin'])
    plot.subplot(223)
    plot.plot(data['samplesq'])
    plot.subplot(224)
    plot.plot(data['ac_lfm'])
    plot.show()