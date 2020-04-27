import matplotlib.pyplot as plot
import numpy as np
from scipy import signal


def _EXIT_():
    print('Выход..')
    exit(0)


def getResult():

    # частота пропускания и частота заграждения
    wp, ws = 0.01, 0.2
    # усиление в полосе пропускания и подавление вне её
    gpass, gstop = 0.1, 50.0

    order_of_the_filter = 24

    b, a = signal.cheby2(11, 50, 0.12, 'low', analog=False)
    w, h = signal.freqz(b, a)

    return {'h': h}


if __name__ == "__main__":
    print('run task19')

    data = getResult()
    plot.subplot(1, 3, 1)
    plot.plot(data['h'])
    plot.title('импульсная характеристика')

    plot.subplot(1, 3, 2)
    plot.plot(10*np.log10(np.abs(data['h'][:200])))
    plot.title('АЧХ')

    plot.subplot(1, 3, 3)
    plot.plot(np.angle(data['h'][:250]))
    plot.title('ФЧХ')
    plot.show()
