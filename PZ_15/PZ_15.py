# Вариант 31
#Приложение СДАЧА В АРЕНДУ ТОРГОВЫХ ПЛОЩАДЕЙ для некоторой организации.
#БД должна содержать таблицу Клиент со следующей структурой записи: ФИО клиента, код помещения, срок аренды, стоимость аренды за весь срок.
import sqlite3

connection = sqlite3.connect('pz15.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Client (
        id INTEGER PRIMARY KEY,
        clientFullName TEXT NOT NULL,
        roomCode TEXT NOT NULL,
        rentalPeriod INTEGER NOT NULL,
        rentalCost INTEGER NOT NULL
    )
''')

cursor.execute('DELETE FROM Client')
connection.commit()

clients = [
    (1, 'Иван Иванович Иванов', 'A101', 12, 150000),
    (2, 'Мария Васильевна Кузнецова', 'B202', 6, 60000),
    (3, 'Сергей Владимирович Васильев', 'C303', 24, 480000),
    (4, 'Наталья Петровна Петрова', 'D404', 18, 270000),
    (5, 'Александр Сергеевич Павлов', 'E505', 36, 720000),
    (6, 'Оксана Александровна Федорова', 'F606', 12, 120000),
    (7, 'Михаил Борисович Козлов', 'G707', 6, 90000),
    (8, 'Виктория Викторовна Смирнова', 'H808', 24, 240000),
    (9, 'Владимир Сергеевич Соколов', 'I909', 12, 180000),
    (10, 'Ирина Андреевна Волкова', 'J1010', 36, 540000)
]

cursor.executemany(
    '''
    INSERT INTO Client (id, clientFullName, roomCode, rentalPeriod, rentalCost)
    VALUES (?, ?, ?, ?, ?)
    ''',
    clients
)



cursor.execute('SELECT * FROM Client')
print("Все позиции в таблице:")
for row in cursor.fetchall():
    print(row)

cursor.execute("SELECT * FROM Client WHERE clientFullName = 'Иван Иванович Иванов'")
print("\nКлиент(ы) которых зовут Иван Иванович Иванов:")
for row in cursor.fetchall():
    print(row)

cursor.execute("SELECT * FROM Client WHERE rentalPeriod < 12")
print("\nВсе аренды сроком меньше 12 месяцев:")
for row in cursor.fetchall():
    print(row)

cursor.execute("SELECT * FROM Client WHERE rentalCost > 200000")
print("\nВсе аренды стоимостью более 200000:")
for row in cursor.fetchall():
    print(row)

cursor.execute("UPDATE Client SET rentalCost = 300000 WHERE roomCode = 'A101'")
cursor.execute("UPDATE Client SET rentalCost = 360000 WHERE rentalPeriod = 36")
cursor.execute("UPDATE Client SET roomCode = 'ZZZ' WHERE clientFullName = 'Михаил Борисович Козлов'")
connection.commit()

cursor.execute("DELETE FROM Client WHERE rentalCost = 60000")
cursor.execute("DELETE FROM Client WHERE clientFullName = 'Мария Васильевна Кузнецова'")
cursor.execute("DELETE FROM Client WHERE roomCode LIKE 'J%'")

cursor.execute('SELECT * FROM Client')
print("\nВсе позиции в таблице после удаления:")
for row in cursor.fetchall():
    print(row)


connection.close()
