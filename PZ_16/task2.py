"""
Создайте базовый класс "Животное" со свойствами "вид", "количество лап", "цвет
    шерсти". От этого класса унаследуйте класс "Собака" и добавьте в него свойства
    "кличка" и "порода".
"""


class Animal:
    def __init__(self, species, num_lap, color) -> None:
        self.species = species
        self.num_lap = num_lap
        self.color = color


class Dog(Animal):
    def __init__(self, species, num_lap, color, nickname, vid):
        super().__init__(species, num_lap, color)
        self.nickname = nickname
        self.vid = vid

    def __str__(self):
        return (f"\nВид: {self.species}\n"
                f"Количество Лап: {self.num_lap}\n"
                f"Цвет шерсти: {self.color}\n"
                f"Кличка: {self.nickname}\n"
                f"Порода: {self.vid}\n"
                )


pet = Dog(
    "Собака",
    4,
    "Белый с чёрными ушками",
    "Кутя",
    "Алабай"
)

print(pet)
