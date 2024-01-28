"""
Из заданной строки отобразить только цифры. Использовать библиотеку string.
Строка - TheGreatPyramidofKhufuatGizawasbuiltabout 2700 BC, 755 feet (230metres) longand
481 feet (147 metres) high.
"""

import string

text = "TheGreatPyramidofKhufuatGizawasbuiltabout 2700 BC, 755 feet (230metres) longand 481 feet (147 metres) high"

numbers_text = ""

for el in text:
    if el.isdigit():
        numbers_text += el
    else:
        continue

print(numbers_text)