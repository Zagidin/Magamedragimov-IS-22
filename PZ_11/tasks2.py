"""
Из предложенного текстового файла (text18-21.txt) вывести на экран его содержимое,
количество знаков препинания. Сформировать новый файл, в который поместить текст в
стихотворной форме выведя строки в обратном порядке.
"""

with open('PZ_11/text18-21.txt', 'r', encoding='UTF-16') as file:
    content = file.read()
    print(content)
    
    punctuation = sum([1 for char in content if char in '.,:;!?'])
    print(f'Количество знаков препинания: {punctuation}')

lines = content.split('\n')

reversed_lines = '\n'.join(lines[::-1])
with open('PZ_11/Стих.txt', 'w', encoding='utf-8') as new_file:
    new_file.write(reversed_lines)
    