import re
from datetime import datetime


class Calendar:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def day_of_week(self):
        days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
        day_index = datetime(self.year, self.month, self.day).weekday()
        return days[day_index]

    def is_leap_year(self):
        if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
            return "Является Високостным годом ( True )"
        else:
            return "Не является Високостным годом ( False )"

    def days_month(self):
        if self.month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif self.month in [4, 6, 9, 11]:
            return 30
        else:
            regular = r"\( \w* \)"
            
            text = self.is_leap_year()

            match = re.search(regular, text)
            
            if match:
                a = match.group()
                a = a.replace("(", '')
                a = a.replace(")", '')
            else:
                print("Совпадение не найдено")
            
            if match.group():
                return 29
            else:
                return 28

input_print = ["Напишите год: ", "Напишите месяц: ", "Напишите число: "]
year, month, day = [int(input(input_print[i])) for i in range(3)]

day1 = Calendar(year=year, month=month, day=day)

print(
    f"\nДень недели: {day1.day_of_week()}\n"
    f"Вид года: {day1.is_leap_year()}\n"
    f"Количество дней в месяце: {day1.days_month()}\n"
)
