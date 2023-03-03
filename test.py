import matplotlib.pyplot as plt
import numpy as np
import func1 as func
import gradient_descent as const_lr

def plot_function(function):
    X, Y = np.meshgrid(np.linspace(-3.0, 3.0, 100),
                       np.linspace(-3.0, 3.0, 100))

    plt.figure(figsize=(16, 10))

    axis = plt.subplot(projection='3d')

    zs = np.array([function(x, y) for [x, y] in zip(np.ravel(X), np.ravel(Y))])
    Z = zs.reshape(X.shape)

    axis.plot_surface(X, Y, Z)
    plt.show()

#plot_function(func1.f)
x = np.linspace(-1, 1, 50)
y = np.linspace(-1, 1, 50)
X, Y = np.meshgrid(x, y)
F = func.f(X, Y)
x_0, y_0 = 1, 1
epsilon = 0.0001
points = const_lr.grad_desc(x_0=x_0, y_0=y_0, learning_rate=0.01, epsilon=epsilon)
#ax = plt.subplots()[1]
horizontal_axis = np.array(points[0:len(points):2])
vertical_axis = np.array(points[1:len(points):2])
plt.scatter(horizontal_axis, vertical_axis, c ="blue")
#ax.plot(x,y)
#ax.contour(X, Y, F, 40)
plt.show()

