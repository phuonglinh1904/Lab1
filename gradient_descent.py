import numpy as np
import func1


def grad_desc(x_0, y_0, learning_rate, epsilon):
    interation = 0
    points = np.array([x_0, y_0])
    while True:
        dif_x0 = learning_rate * func1.dif_x(x_0, y_0)
        dif_y0 = learning_rate * func1.dif_y(x_0, y_0)
        x_0 -= dif_x0
        y_0 -= dif_y0
        points = np.append(points, [x_0, y_0])
        interation += 1
        if np.abs(func1.dif_x(x_0, y_0)) <= epsilon and np.abs(func1.dif_y(x_0, y_0)) <= epsilon:
            break

    return points
