import numpy as np
import matplotlib.pyplot as plt

def plot(fun, start, end):
    x = np.arange(float(start), float(end), 0.1)
    n_fun = np.vectorize(fun)
    plt.plot(n_fun(x))
    plt.show()

