# Создайте базовый класс "Транспорт" со свойствами "марка", "модель" и "год выпуска".
# От этого класса унаследуйте класс "Автомобиль" и добавьте в него свойство "тип кузова"

class Transport:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"Марка: {self.brand}, Модель: {self.model}, Год выпуска: {self.year}"


class Car(Transport):
    def __init__(self, brand, model, year, body_type):
        super().__init__(brand, model, year)
        self.body_type = body_type

    def __str__(self):
        return f"{super().__str__()}, Тип кузова: {self.body_type}"


car1 = Car("Toyota", "Camry", 2020, "Седан")
print(car1.__str__())

car2 = Car("Mercedes-Benz", "GLE", 2022, "Кроссовер")
print(car2.__str__())
