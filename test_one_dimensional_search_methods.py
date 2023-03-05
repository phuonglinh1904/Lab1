import numpy as np
from dichotomy_search import dichotomy_method
from fibonacci import fibonacci_search
from golden_ratio import golden_ratio_search
import matplotlib.pyplot as plt
import pandas as pd
def function_1(x):
    return np.sin(x) - x**3 - 1


def function_2(x):
    return np.log2(x) * np.cos(x) + 4


def function_3(x):
    return np.sin(x - 1)


borders = [[-1000, 1000], [-10, 100000], [-1000, 1]]
precisions = np.linspace(0.00001, 0.1, 50)

def plot_figure(method, color, n_iter=0, label="", func=None):
    if func is None:
        func = function_1

    iterations = np.array([])
    for precision in precisions:
        if n_iter == 0:
            func_res = np.array(method(func, 1, 10, precision)[2])
        else:
            func_res = np.array(method(func, 1, 10, precision, n_iter)[2])
        iterations = np.append(iterations, func_res.shape[0])
    plt.xlabel("precision")
    plt.ylabel("iteration")
    plt.plot(precisions, iterations, color=color, label=label)
    plt.legend()
    plt.show()
#plot_figure(dichotomy_method, "blue", label='dichotomy', func=function_2)
#plot_figure(fibonacci_search, "blue",n_iter=40, label='fibonaci', func=function_2)
#plot_figure(golden_ratio_search, "blue", label='golden', func=function_2)







