# Червиснкий ИС-25
from random import randint
N = randint(1, 1000)
print('Кол-во чисел:', N)
count = 0
numbers = []
for i in range(N):
    num = randint(1, 10000)
    numbers.append(num)
for i in range(N):
    for j in range(i + 1, N):
        if (numbers[i] * numbers[j]) % 58 == 0:
            count += 1
print('Кол-во пар кратных 58: ',count)