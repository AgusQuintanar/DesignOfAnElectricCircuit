import numpy as np
import matplotlib.pyplot as plt

def graficar(fun, inicio, fin):
    x = np.arange(float(inicio), float(fin), 0.1)
    n_fun = np.vectorize(fun)
    plt.plot(n_fun(x))
    plt.show()

if __name__ == "__main__":
    fun_que_define_agus = lambda x: x**2 - 1
    graficar(fun_que_define_agus, -5,5)
