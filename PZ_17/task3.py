"""
    Задание предполагает, что у студента есть проект с практическими работами (№№ 2-13),
    оформленный согласно требованиям. Все задания выполняются c использованием модуля
    OS:
         перейдите в каталог PZ11. Выведите список всех файлов в этом каталоге. Имена
        вложенных подкаталогов выводить не нужно.
        
         перейти в корень проекта, создать папку с именем test. В ней создать еще одну папку
        test1. В папку test переместить два файла из ПЗ6, а в папку test1 - один файл из ПЗ7.
        Файл из ПЗ7 переименовать в test.txt. Вывести в консоль информацию о размере
        файлов в папке test.
        
         перейти в папку с PZ11, найти там файл с самым коротким именем, имя вывести в
        консоль. Использовать функцию basename () (os.path.basename()).
        
         перейти в любую папку где есть отчет в формате .pdf и «запустите» файл в
        привязанной к нему программе. Использовать функцию os.startfile().
        
         удалить файл test.txt.
"""

import shutil
from os import *


# Задание 1

chdir('../PZ_11')
print("\nЗадание №1\nТекущая дериктория: ", getcwd())

dir_11_list = [files for files in listdir()]

dir_11_list_str = ''
for el in dir_11_list:
    dir_11_list_str += el + ' '

print("Cписок всех файлов: ", dir_11_list_str.replace(' ', ', '))

# Задание 2

chdir('..')
print("\nЗадание №2")
makedirs('test/test1', exist_ok=True)

chdir('./PZ_6')

dir_6_list = [files for files in listdir()]

dir_6_list_str = ''
for el in range(2):
    dir_6_list_str += dir_6_list[el] + ' '
    shutil.move(dir_6_list[el], '../test')

chdir('../PZ_7')

dir_7_list = [files for files in listdir()]

for el in range(1):
    shutil.move(dir_7_list[el], '../PZ_7/test.txt')

for root, dirs, files in walk('./test'):
    for file in files:
        file_path = path.join(root, file)
        file_size = path.getsize(file_path)
        print(f'Файл: {file_path}, Размер файла: {file_size} байт')

# Задание 3

