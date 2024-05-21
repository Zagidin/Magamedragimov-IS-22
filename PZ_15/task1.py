"""
    Приложение РАСПРЕДЕЛЕНИЕ ДОПОЛНИТЕЛЬНЫХ ОБЯЗАННОСТЕЙ для
    некоторой организации. БД должна содержать таблицу Обязанности со следующей
    структурой записи: ФИО работника, вид дополнительной работы, сумма оплаты, срок.
"""

import sqlite3 as sp

with sp.connect('PZ_15/zaga.db') as conn:
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS Обязанности (
            id INTEGER PRIMARY KEY,
            ФИО TEXT,
            Работа TEXT,
            Сумма INTEGER,
            Дата DATE
        )
    ''')

with conn:
    cur = conn.cursor()
    cur.executemany("INSERT INTO Обязанности VAlUES(NULL, ?, ?, ?, ?)", [
        ("Магамедрагимов З. Ш.", "Программист", 50000, 12-12-2030),
        ("Прохорукин Я. С.", "Программист", 500300, 12-12-2039),
        ("Ковалёв О. О.", "Программист", 520000, 12-12-2038),
        ("Дремлюга В. А.", "Программист", 505000, 12-12-2037),
        ("Синельников С. Е.", "Программист", 500600, 12-12-2036),
        ("Ткаченко Р. А.", "Программист", 50300, 12-12-2035),
        ("Мороз М. А.", "Программист", 500010, 12-12-2034),
        ("Светличный Н. А.", "Программист", 530000, 12-12-2033),
        ("Дьяченко Л. А.", "Программист", 520000, 12-12-2032),
        ("Магамедрагимов З. Ш.", "Программист", 501000, 12-12-2031),
    ])

with conn:
    cur = conn.cursor()
    print("Определённый человек:", *cur.execute('SELECT * FROM Обязанности WHERE ФИО="Магамедрагимов З. Ш." ORDER BY id DESC').fetchall(), sep='\n', end='\n\n')
    print("Поиск по сумме:", *cur.execute('SELECT * FROM Обязанности WHERE Сумма >= 520000').fetchall(), sep='\n', end='\n\n')
    print("Все Данные:", *cur.execute('SELECT * FROM Обязанности').fetchall(), sep='\n', end='\n\n')

with conn:
    cur = conn.cursor()
    cur.execute('DELETE FROM Обязанности WHERE ФИО = ?', ("Магамедрагимов З. Ш.",))
    cur.execute('DELETE FROM Обязанности WHERE Сумма >= 520000')
    cur.execute('DELETE FROM Обязанности WHERE Сумма <= 500010')
    print("Вывод после удаления:", *cur.execute('SELECT * FROM Обязанности').fetchall(), sep='\n', end='\n\n')


with conn:
    cur = conn.cursor()
    cur.execute('UPDATE Обязанности SET Сумма = 600000 WHERE Сумма = 505000')
    print("Изменили Сумму 50010 на 6000:", *cur.execute('SELECT ФИО, Сумма FROM Обязанности').fetchall(), sep='\n', end='\n\n')
    cur.execute('UPDATE Обязанности SET ФИО = "Белиджи Респ. Дагестан" WHERE ФИО = "Синельников С. Е."')
    print("Изменили ФИО одного человека:", *cur.execute('SELECT ФИО FROM Обязанности').fetchall(), sep='\n', end='\n\n')
    cur.execute('UPDATE Обязанности SET Работа = "Студенты" WHERE Работа = "Программист"')
    print("Обновили Работу Всем:", *cur.execute('SELECT * FROM Обязанности').fetchall(), sep='\n', end='\n\n')
