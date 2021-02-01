import numpy as np
import matplotlib.pyplot as plt


def f(z, c):
    return z**2 + c


def convergence_test(c, n_precision):
    '''By the fact tha z converges if for any |zn| <= 2,
    test that using n_precision iteration returning
    (test result, n for |zn| > 2)'''
    converges = True
    z = 0
    for i in range(n_precision):
        if abs(f(z, c)) > 2:
            converges = False
            return (converges, i)
        z = f(z, c)
    return (converges, None)


def f_sequence(c, n):
    z = 0
    L = []
    L.append(z)
    for i in range(1, n + 1):
        z = f(z, c)
        L.append(z)
    return L



def init_set(real_min, real_max, imag_min, imag_max, delta, convergence_prec):
    L = []
    real = real_min
    imag = imag_min
    while real < real_max:
        while imag < imag_max:
            c = complex(real, imag)
            converges, prec = convergence_test(c, convergence_prec)
            if converges:
                L.append(c)
            imag += delta
        real += delta
        imag = imag_min
    return L

# A simple test run
m_set = init_set(-2, 0.5, -1, 1, 0.01, 50)
real_values = []
imag_values = []
for value in m_set:
    real_values.append(value.real)
    imag_values.append(value.imag)

plt.plot(real_values, imag_values, '.', markersize=0.2)
plt.show()
