import numpy as np
def dichotomy_method(func, left_border: float, right_border: float, precision: float):
    l = left_border
    r = right_border
    delta = precision / 2
    d = abs(r-l)
    iters_data = np.array([l,r])
    middle_x = (l + r)/2
    while d > precision:
        x1 = (l + r - delta) / 2
        x2 = (l + r + delta) / 2
        y1 = func(x1)
        y2 = func(x2)
        if y1 > y2:
            l = x1

        elif y1 < y2:
            r = x2
        else:
            l = x1
            r = x2
        d = abs(r-l)
        middle_x = (l + r) / 2
        iters_data = np.append(iters_data, [l, r])

    return middle_x, func(middle_x), iters_data.reshape((iters_data.size // 2, 2))

