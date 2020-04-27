import matplotlib.pyplot as plot
import math

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
        y_values.append(y * y)

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
    plot.ylabel('рис 2')
    plot.show()

if __name__ == "__main__":
    N = 100
    print('run task2')
    INPUT()
    P = int(str1)
    data = getResult(N, P)
    plotGraf(data)
