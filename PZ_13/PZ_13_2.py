#Вариант 31
#В матрице элементы второго столбца заменить
#элементами из одномерного динамического массива соответствующей размерности.
import random

n = int(input('Размер матрицы: '))
matrix = [[random.randint(1, 10) for j in range(n)] for i in range(n)]
mass = [random.randint(0, 10) for i in range(n)]
print("\nИсходный одномерный массив: ", mass)
print("\nИсходная матрица: "), [print(row) for row in matrix]
for i in range(n):
    matrix[i][1] = mass[i]
print("\nИзмененная матрица: "), [print(row) for row in matrix]
