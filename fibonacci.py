import numpy as np
def get_fibonacci_numbers(n):
    if n in {0, 1}:
        return n
    nums = np.array([0, 1, 1])
    for i in range(2, n):
        nums = np.append(nums, nums[i] + nums[i - 1])
    return nums
def fibonacci_search(func, left_border: float, right_border: float, precision: float, n_iters: int):
    left = left_border
    right = right_border
    fib_nums = get_fibonacci_numbers(n_iters)
    x1 = left + fib_nums[n_iters - 2] / fib_nums[n_iters] * (right - left)
    x2 = left + fib_nums[n_iters - 1] / fib_nums[n_iters] * (right - left)
    y1, y2 = func(x1), func(x2)
    iters_data = np.array([left, right])
    for k in range(1, n_iters - 1):
        if y1 >= y2:
            left = x1
            x1, y1 = x2, y2
            x2 = left + (fib_nums[n_iters - k - 1] / fib_nums[n_iters - k]) * (right - left)
            y2 = func(x2)
        else:
            right = x2
            x2, y2 = x1, y1
            x1 = left + (fib_nums[n_iters - k - 2] / fib_nums[n_iters - k]) * (right - left)
            y1 = func(x1)
        iters_data = np.append(iters_data, [left, right])
        if right - left < precision:
            m = (left + right) / 2
            return m, func(m), iters_data.reshape((iters_data.size) // 2, 2)
    m = (left + right) / 2
    return m, func(m), iters_data.reshape((iters_data.size) // 2, 2)
