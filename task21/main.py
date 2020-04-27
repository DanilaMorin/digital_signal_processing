import matplotlib.pyplot as plot
import numpy as np
from scipy import signal


def _EXIT_():
    print('Выход..')
    exit(0)


def getResult(P,N):
    k = P / (N * 0.5)

    X1 = np.array(0)
    S1 = np.array(0)
    X2 = np.array(0)
    S2 = np.array(0)
    # частота пропускания и частота заграждения
    wp, ws = 0.01, 0.2
    # усиление в полосе пропускания и подавление вне её
    gpass, gstop = 0.1, 50.0

    order_of_the_filter = 11

    b, a = signal.bessel(6, 0.2, 'low', analog=False)
    w, h = signal.freqz(b, a)

    return {'h': h}


if __name__ == "__main__":
    print('run task21')
    P = 10
    N = 100
    data = getResult(P,N)
    plot.subplot(1, 3, 1)
    plot.plot(data['h'])
    plot.title('импульсная характеристика')

    plot.subplot(1, 3, 2)
    plot.plot(np.abs(data['h'][:200]))
    plot.title('АЧХ')

    plot.subplot(1, 3, 3)
    plot.plot(np.angle(data['h'][:200]))
    plot.title('ФЧХ')
    plot.show()
