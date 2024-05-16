#Вариант 31
#Сгенерировать матрицу, в которой нечетные элементы заменяются на 0.

import random

n = int(input('Размер матрицы: '))
matrix = [[random.randint(1, 10) for j in range(n)] for i in range(n)]
print('\nСгенерированная матрица: ')
[print(row) for row in matrix]
matrix = list(map(lambda x: [0 if elem % 2 != 0 else elem for elem in x], matrix))
print('\nИзмененная матрица: ')
[print(row) for row in matrix]
