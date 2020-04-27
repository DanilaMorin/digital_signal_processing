import matplotlib.pyplot as plot
import math
import numpy as np
def _EXIT_():
        print('Выход..')
        exit(0)



def INPUT():
        global str1
        str1 = input('ВВОД P: ')

def getResult(N, P):
    y_values = []
    x_values = []
    for i in range(0, N):
        x_values.append(i)
        y = math.sin(2 * 3.14 * i * P / N)
        y_values.append(y)

    return {'x_values': x_values, 'y_values': y_values}

def math_expr(*args):
    data_x = []
    data_y = []
    for x in args:
        data_x.append(x)
        data_y.append(x ** 2)

    plot.plot(data_x, data_y)
    plot.ylabel('детское выражение')
    plot.show()

def plotGraf(data):
    data_x = data["x_values"]
    data_y = data["y_values"]
    plot.plot(data_x, data_y)
    plot.ylabel('рис 3')
    plot.show()

def spectr(data):
    y_sign = data["y_values"]
    x_sign = data["x_values"]

    x_result = []
    y_result = []

    print(x_sign)
    length = len(x_sign)

    for k in range(0, length):
        x_result.append(x_sign[k])
        y = 0
        for n in range(0, length):
            # fi = complex(0, -1*(2*3.14)/length*k*n)
            fi = -2j*math.pi*k*n/length
            y += y_sign[n] * math.exp(fi.imag)
        y_result.append(y)

    return {'x_values': x_result, 'y_values': y_result}

def DFT_slow(x):
    """Compute the discrete Fourier Transform of the 1D array x"""
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)

if __name__ == "__main__":
    N = 100
    print('run task3')
    INPUT()
    P = int(str1)
    data = getResult(N, P)
    plotGraf(data)
    #sp = spectr(data)
    #plotGraf(sp)
    nn = DFT_slow(data['y_values'])
    plot.plot(nn)
    plot.ylabel('детское выражение')
    plot.show()