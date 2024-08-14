# func_py_calculate_cone_surface_area.py
import math

def func_py_calculate_cone_surface_area(radius, slant_height):
    return math.pi * radius * (radius + slant_height)

print(func_py_calculate_cone_surface_area(3, 5))
