import numpy as np
def golden_ratio_search(func, left_border: float, right_border: float, precision: float):
    phi = (np.sqrt(5) - 1) / 2
    left = left_border
    right = right_border
    x1 = left + phi*(right-left)
    x2= right - phi*(right-left)
    y1 = func(x1)
    y2 = func(x2)
    iters_data = np.array([left, right])
    while abs(right-left) >= precision:
        if y1 < y2:
            right = x2
            x2 = x1
            y2 = y1
            x1 = left + phi*(right-left)
            y1 = func(x1)
        else:
            left = x1
            x1 = x2
            y1 = y2
            x2 = right -phi*(right-left)
            y2 = func(x2)
        iters_data = np.append(iters_data, [left, right])

    m = (right + left)/2
    return m , func(m), iters_data.reshape((iters_data.size)// 2, 2)
