"""
    Приложение РАСПРЕДЕЛЕНИЕ ДОПОЛНИТЕЛЬНЫХ ОБЯЗАННОСТЕЙ для
    некоторой организации. БД должна содержать таблицу Обязанности со следующей
    структурой записи: ФИО работника, вид дополнительной работы, сумма оплаты, срок.
"""


import sqlite3

db = sqlite3.connect('PZ_15/zagura.db')
cursor = db.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Обязанности (
        id INTEGER PRIMARY KEY,
        ФИО TEXT,
        Работа TEXT,
        Сумма INTEGER,
        Дата DATE
    )
''')

db.commit()
db.close()

db = sqlite3.connect('PZ_15/zagura.db')
cursor = db.cursor()

input_print = [
    "Введите Ваше ФИО: ", 
    "Введите Вид работы: ", 
    "Введите сумму оплаты: ", 
    "Введите срок: "
]

fio, work, pay, year = [input(input_print[i]) for i in range(4)]

cursor.execute(
    """INSERT INTO Обязанности (ФИО, Работа, Сумма, Дата) VALUES (?, ?, ?, ?)""", 
    (fio, work, int(pay), year,)
)

db.commit()
db.close()

db = sqlite3.connect('PZ_15/zagura.db')
cursor = db.cursor()

cursor.execute("""SELECT * FROM Обязанности""")

content_baze = cursor.fetchall()

db.commit()
db.close()

for el in content_baze:
    print(el)
