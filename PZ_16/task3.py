"""
Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
    сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
    Использовать модуль pickle для сериализации и десериализации объектов Python в
    бинарном формате.
"""

import pickle

from random import randint
from task1 import Calendar


def save_def(data, name_file):
    with open(name_file, 'wb') as file:
        pickle.dump(data, file)


def load_def(name_file):
    with open(name_file, 'rb') as file:
        data = pickle.load(file)

    return data


day1, day2, day3 = (
    Calendar(2024, 5, 20),
    Calendar(2024, 6, 20),
    Calendar(2024, 7, 20)
)

save_def([day1, day2, day3], name_file='file.pkl')

load_file = load_def('file.bat')

for i in load_file:
    print(i)