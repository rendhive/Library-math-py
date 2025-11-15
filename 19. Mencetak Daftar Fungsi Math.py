import math

functions = [math.sin, math.cos, math.tan, math.sqrt, math.log]
for func in functions:
    print(f"Fungsi: {func.__name__}, Doc: {func.__doc__}")
# Fungsi: Mencetak nama dan dokumentasi fungsi dari modul math.
# Kondisi: Ketika Anda ingin menjelajahi fungsi yang tersedia dalam modul.
