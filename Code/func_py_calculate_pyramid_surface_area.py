# func_py_calculate_pyramid_surface_area.py
import math

def func_py_calculate_pyramid_surface_area(base_length, height):
    slant_height = math.sqrt((base_length / 2)**2 + height**2)
    return base_length**2 + 2 * base_length * slant_height

print(func_py_calculate_pyramid_surface_area(4, 6))
