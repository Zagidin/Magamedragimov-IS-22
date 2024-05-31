# Многопоточность

from time import sleep
from threading import Thread


def main():
    print("Process 1")
    sleep(3)
    print("Process One Good!")


def main2():
    print("Process 2")
    sleep(3)
    print("Process Two Good!")


one_func = Thread(target=main)
one_func.start()
two_func = Thread(target=main2)
two_func.start()

# main()
# main2()

# import pickle
#
# class Animal:
#     def __init__(self, species: str, num_legs: int, fur_color: str):
#         self.species = species
#         self.num_legs = num_legs
#         self.fur_color = fur_color
#
#     def __str__(self):
#         return f"Вид: {self.species}, Количество лап: {self.num_legs}, Цвет шерсти: {self.fur_color}"
#
#
# class Dog(Animal):
#     def __init__(self, species: str, num_legs: int, fur_color: str, nickname: str, breed: str):
#         super().__init__(species, num_legs, fur_color)
#         self.nickname = nickname
#         self.breed = breed
#
#     def __str__(self):
#         return f"{super().__str__()}, Кличка: {self.nickname}, Порода: {self.breed}"
#
#
# def save_def(objects, filename):
#     """Сохраняет список объектов в файл."""
#     with open(filename, 'wb') as file:
#         pickle.dump(objects, file)
#
#
# def load_def(filename):
#     """Загружает список объектов из файла."""
#     with open(filename, 'rb') as file:
#         objects = pickle.load(file)
#     return objects
#
#
# # Создаем экземпляры класса Dog
# dog1 = Dog("Собака", 4, "коричневый", "Бобик", "Лабрадор")
# dog2 = Dog("Собака", 4, "черный", "Шарик", "Пудель")
# dog3 = Dog("Собака", 4, "белый", "Рекс", "Бульдог")
#
# # Сохраняем экземпляры класса Dog в файл
# save_def([dog1, dog2, dog3], 'dogs.pkl')
#
# # Загружаем экземпляры класса Dog из файла
# loaded_dogs = load_def('dogs.pkl')
#
# # Печатаем загруженные экземпляры
# for dog in loaded_dogs:
#     print(dog)


"""
# # Задание 2
# 
# chdir('..')
# print("\nЗадание №2")
# makedirs('test/test1', exist_ok=True)
# 
# chdir('./PZ_6')
# 
# dir_6_list = [files for files in listdir()]
# 
# dir_6_list_str = ''
# for el in range(2):
#     dir_6_list_str += dir_6_list[el] + ' '
#     shutil.move(dir_6_list[el], '../test')
# 
# chdir('../PZ_7')
# 
# dir_7_list = [files for files in listdir()]
# 
# for el in range(1):
#     shutil.move(dir_7_list[el], '../PZ_7/test.txt')
# 
# for root, dirs, files in walk('./test'):
#     for file in files:
#         file_path = path.join(root, file)
#         file_size = path.getsize(file_path)
#         print(f'Файл: {file_path}, Размер файла: {file_size} байт')
# 
# # Задание 3
"""
