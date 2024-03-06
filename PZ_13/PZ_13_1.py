#Вариант 31
#Сгенерировать матрицу, в которой нечетные элементы заменяются на 0.
import random

n = int(input('Размер матрицы: '))
matrix = [[random.randint(1, 10) for j in range(n)] for i in range(n)]
print('Сгенерированная матрица: '), [print(j) for j in matrix]

for i in range(n):
    for j in range(n):
        if matrix[i][j] % 2 != 0:
            matrix[i][j] = 0
print('Матрица с замененными нечетными значениями на 0: '), [print(j) for j in matrix]
