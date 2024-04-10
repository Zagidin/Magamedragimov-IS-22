import sqlite3

db = sqlite3.connect('zagura.db')
cursor = db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
ФИО TEXT,
Работа TEXT,
Сумма INTEGER,
Дата 
)
''')

db.commit()
db.close()

db = sqlite3.connect('zagura.db')
cursor = db.cursor()

fio, work = input("Введите Ваше ФИО: "), input("Введите Вид работы: ")
pay, year = int(input("Введите сумму оплаты: ")), input("Введите срок: ")

cursor.execute("""
INSERT INTO Users (ФИО, Работа, Сумма, Дата) VALUES (?, ?, ?, ?), (fio, work, pay, year)
""")

db.commit()
db.close()

db = sqlite3.connect('zagura.db')
cursor = db.cursor()

cursor.execute("""
SELECT * FROM Users
""")

content_baze = cursor.fetchall()
db.commit()
db.close()

print(content_baze)