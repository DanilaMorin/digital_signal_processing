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
    samples = signal.chirp(np.linspace(0, 50, 150), f0=6, f1=1, t1=10, method='linear') + samples
    ac_acf = np.correlate(samples, samples, mode='full')

    return {'samples': samples, 'ac_acf': ac_acf}



if __name__ == "__main__":
    print('run task15')
    data = getResult()
    plot.subplot(221)
    plot.plot(data['samples'])
    plot.subplot(222)
    plot.plot(data['ac_acf'])
    plot.show()