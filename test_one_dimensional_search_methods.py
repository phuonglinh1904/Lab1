import numpy as np
from dichotomy_search import dichotomy_method
from fibonacci import fibonacci_search
from golden_ratio import golden_ratio_search
import matplotlib.pyplot as plt
import pandas as pd
def test_function_1(x):
    return np.sin(x) - x**3 - 1


def test_function_2(x):
    return np.log2(x) * np.cos(x) + 4


def test_function_3(x):
    return np.sin(x - 1)

precisions = np.linspace(0.00001, 0.1, 50)


def plot_figure(method, color, n_iter=0, label="", func=None):
    if func is None:
        func = test_function_2

    iterations = np.array([])
    for precision in precisions:
        if n_iter == 0:
            func_res = np.array(method(func, -1, 5, precision)[2])
        else:
            func_res = np.array(method(func, -1, 5, precision, n_iter)[2])
        iterations = np.append(iterations, func_res.shape[0])

    plt.plot(precisions, iterations, color=color, label=label)
plt.xlabel("precision")
plt.ylabel("iteration")
#plot_figure(dichotomy_method, "blue", label='dichotomy', func=test_function_2)
#plot_figure(fibonacci_search, "blue",n_iter=40, label='fibonaci', func=test_function_2)
#plot_figure(golden_ratio_search, "blue", label='golden', func=test_function_2)
plt.legend()
plt.show()

def plot_graph(method,func=None) :
    x_min, y_min, iter_data = dichotomy_method(test_function_1,-1,5,0.01)
    x = np.arange(1,7)
    y = test_function_1(x)
    plt.plot(x,y,'b-', x_min, y_min,'go',iter_data[0:len(iter_data):2], iter_data[:len(iter_data):2],'r^')
    plt.xlabel("X label")
    plt.ylabel("Y label")
    plt.show()

plot_graph(dichotomy_method,test_function_1)
