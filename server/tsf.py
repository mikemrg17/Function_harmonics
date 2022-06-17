# Serie de Fourier, con n coeficientes
# Ref.Chapra 5ed Ejemplo 19.2 p548/pdf572
from sympy import fourier_series, pi, plot
from sympy.abc import x
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

def compute(signal):
    func = signal.signal
    less = signal.less
    greater = signal.greater
    harmonics = signal.harmonics
    s = fourier_series(func, (x, int(less), int(greater)))
    p = plot(func, (x, less, greater), show=False, legend=True)
    p.show()
    return str(s.scale(1).truncate(n=int(harmonics)))