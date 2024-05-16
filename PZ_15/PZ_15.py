import sqlite3

# Создать соединение с базой данных
conn = sqlite3.connect('rental.db')
c = conn.cursor()

# Создать таблицу Клиент
c.execute('''CREATE TABLE IF NOT EXISTS Клиент (
    ФИО_клиента TEXT,
    Код_помещения INTEGER,
    Срок_аренды INTEGER,
    Стоимость_аренды REAL
)''')

# Вставить данные в таблицу
c.execute("INSERT INTO Клиент VALUES ('Иванов Иван Иванович', 101, 12, 12000)")
c.execute("INSERT INTO Клиент VALUES ('Петров Петр Петрович', 102, 18, 18000)")
c.execute("INSERT INTO Клиент VALUES ('Сидоров Сидор Сидорович', 103, 24, 24000)")

# Сохранить изменения в базе данных
conn.commit()
# Закрыть соединение с базой данных
conn.close()