""""
Дана строка «Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4». Преобразовать
информацию из строки в словарь, найти среднее арифметическое оценок,
результаты вывести на экран.
"""

task_lesson = 'Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4'
task_lesson = task_lesson.split()

STUDENT = {
    
}

STUDENT['last_name'] = task_lesson[0]
STUDENT['name'] = task_lesson[1]
STUDENT['group'] = task_lesson[2]
STUDENT['evaluations'] = list()

for el in task_lesson[3:]:
    STUDENT['evaluations'].append(int(el))

evaluations_list = STUDENT['evaluations']

print(f"Преоб-ная ст-ка в словар -> {STUDENT}")
print("Находим среднее арифметическое оценок студента", STUDENT['name'], "-->", *evaluations_list)
print(f"Итоговый результат: {int(sum(evaluations_list) / len(evaluations_list))}")
