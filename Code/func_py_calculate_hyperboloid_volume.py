# func_py_calculate_hyperboloid_volume.py
import math

def func_py_calculate_hyperboloid_volume(radius1, radius2, height):
    return math.pi * height * (radius1**2 + radius2**2 + radius1 * radius2) / 3

print(func_py_calculate_hyperboloid_volume(3, 4, 7))
