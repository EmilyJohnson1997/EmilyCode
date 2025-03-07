# func_py_generate_barcode.py
import barcode
from barcode.writer import ImageWriter

def func_py_generate_barcode(data, filename="barcode.png"):
    ean = barcode.get_barcode_class("ean13")
    barcode_obj = ean(data, writer=ImageWriter())
    barcode_obj.save(filename)

func_py_generate_barcode("123456789012")
