# func_py_calculate_pentagonal_pyramid_volume.py
import math

def func_py_calculate_pentagonal_pyramid_volume(base_edge, height):
    base_area = (5 * base_edge**2) / (4 * math.tan(math.pi / 5))
    return (1 / 3) * base_area * height

print(func_py_calculate_pentagonal_pyramid_volume(6, 10))
