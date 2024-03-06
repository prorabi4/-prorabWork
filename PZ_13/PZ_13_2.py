#Вариант 31
#В матрице элементы второго столбца заменить
#элементами из одномерного динамического массива соответствующей размерности.
import random

matrix = [[random.randint(1, 10) for j in range(3)] for i in range(3)]
mass = [random.randint(0, 10) for i in range(3)]
print("Исходный одномерный массив: ", mass)
print("Исходная матрица: "), [print(row) for row in matrix]
for i in range(3):
    matrix[i][1] = mass[i]
print("\nМатрица со вторым столбцом замененным на одномерный массив: "), [print(row) for row in matrix]