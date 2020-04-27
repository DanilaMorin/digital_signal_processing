import matplotlib.pyplot as plot
import math


def _EXIT_():
    print('Выход..')
    exit(0)


def INPUT():
    global str1
    str1 = input('ВВОД P: ')


def add_value_in_register(summator, value):
    for i in range(len(summator) - 1):
        summator[i] = summator[i + 1]
    summator[len(summator) - 1] = value

def get_summ(summator):
    result = 0
    for value in summator:
        result += value

    return result

def getResult(N, P):
    y_values = []
    x_values = []
    sum_sign = []
    delta_sign = []
    summator = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(0, N):
        y = math.sin(2 * 3.14 * i * P / N)

        add_value_in_register(summator, y)
        sum_sign.append(y + get_summ(summator))
        delta_sign.append(y - summator[-2])
        x_values.append(i)
        y_values.append(y)

    return {'x_values': x_values, 'y_values': y_values, 'sum_sign': sum_sign, 'delta_sign': delta_sign}


def math_expr(*args):
    data_x = []
    data_y = []
    for x in args:
        data_x.append(x)
        data_y.append(x ** 2)

    plot.plot(data_x, data_y)
    plot.ylabel('детское выражение')
    plot.show()


def plotGraf(data, x_label="x_values", y_label='y_values'):
    data_x = data[x_label]
    data_y = data[y_label]
    plot.ylabel('рис 1')
    plot.plot(data_x, data_y)




if __name__ == "__main__":
    N = 100
    print('run task5')
    INPUT()
    P = int(str1)
    data = getResult(N, P)
    plot.subplot(311)
    plotGraf(data)
    plot.subplot(313)
    plotGraf(data, x_label='x_values', y_label="sum_sign")
    plot.subplot(312)
    plotGraf(data, x_label='x_values', y_label="delta_sign")
    plot.show()