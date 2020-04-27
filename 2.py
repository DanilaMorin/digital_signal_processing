import matplotlib.pyplot as plot


def math_expr(*args):
    data_x = []
    data_y = []
    for x in args:
        data_x.append(x)
        data_y.append(x ** 2)

    plot.plot(data_x, data_y)
    plot.ylabel('детское выражение')
    plot.show()


if __name__ == '__main__':
    math_expr(1, 2, 3, 4, 5)