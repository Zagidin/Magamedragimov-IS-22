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

import os
import time

# Задание 1

os.chdir('../PZ_11')
print("\nЗадание №1\nТекущая дериктория: ", os.getcwd())

dir_11_list = [files for files in os.listdir()]

dir_11_list_str = ''
for el in dir_11_list:
    dir_11_list_str += el + ' '

print("Cписок всех файлов: ", dir_11_list_str.replace(' ', ', '))


# Задание 2

print("\nЗадание №2")
os.chdir('..')
os.makedirs("test/test1", exist_ok=True)
os.chdir('./PZ_6')

os.replace('list.py', '../test/list.py')
os.replace('list2.py', '../test/list2.py')

os.chdir('../PZ_7')
os.replace('main.py', '../test/test1/test.txt')
os.chdir('../test')
print("Размер первого файла:", os.stat("list.py").st_size)
print("Размер второго файла:", os.stat("list2.py").st_size)

# Задание 3

print("Задание №3")
os.chdir('../PZ_11')
files = os.listdir('.')
shortest_name_file = min(files, key=lambda x: len(os.path.basename(x)))
print(f'\nФайл с самым коротким названием из папки PZ_11: {os.path.basename(shortest_name_file)}')

# Задание 4

print("Задание №4")
os.chdir('../reports/PZ_17')
pdf_file = 'PZ_17.pdf'
os.startfile(pdf_file)

# Задание 5

time.sleep(0.10)
print("Задание №5")
os.remove("../test/test1/test.txt")
