import matplotlib.pyplot as plot
import numpy as np
from scipy import signal


def _EXIT_():
    print('Выход..')
    exit(0)


def getResult():

    b, a = signal.cheby1(14, 0.01, 0.22, 'low', analog=False)
    w, h = signal.freqz(b, a)

    return {'h': h}


if __name__ == "__main__":
    print('run task18')

    data = getResult()
    plot.subplot(1, 3, 1)
    plot.plot(data['h'])
    plot.title('импульсная характеристика')

    plot.subplot(1, 3, 2)
    plot.plot(np.abs(data['h'][:200]))
    plot.title('АЧХ')

    plot.subplot(1, 3, 3)
    plot.plot(np.angle(data['h']))
    plot.title('ФЧХ')
    plot.show()
