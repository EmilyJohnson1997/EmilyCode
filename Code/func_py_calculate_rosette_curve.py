# func_py_calculate_rosette_curve.py
import matplotlib.pyplot as plt
import numpy as np

def func_py_calculate_rosette_curve(a, n, points):
    t = np.linspace(0, 2 * np.pi, points)
    r = a * np.cos(n * t)
    x = r * np.cos(t)
    y = r * np.sin(t)
    plt.plot(x, y)
    plt.title("Rosette Curve")
    plt.show()

func_py_calculate_rosette_curve(5, 6, 1000)
