from math import sqrt
from matplotlib import pyplot as plt


def get_distance(points_x, points_y):
    N = len(points_x)
    return [[sqrt((points_x[i] - points_x[j]) ** 2 + (points_y[i] - points_y[j]) ** 2) for i in range(N)] for j in
            range(N)]


def show(points_x, points_y, result, title=''):
    plt.scatter(points_x, points_y)
    plt.plot([points_x[i] for i in result], [points_y[i] for i in result], linestyle='-', color='blue',
             label='Line')
    if title:
        plt.title(title)
    plt.show()
