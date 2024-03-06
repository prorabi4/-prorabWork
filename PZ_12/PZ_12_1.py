# Вариант 31.
# 1. Организовать и вывести последовательность на N произвольных целых элементов,
#сформировать новую последовательность куда поместить квадраты четных элементов, найти их сумму и среднее арифметическое.


# -*- coding: utf8 -*-
from random import randint
subsequence = [randint(0, 20) for i in range(10)]
print(f'Сгенерированная последовательность: {subsequence}')
s_subsequence1 = [num**2 for num in subsequence if num % 2 == 0]
print(f"Возведение четных чисел в квадрат: {s_subsequence1}")
sum_s = sum(s_subsequence1)
print(f"Сумма чисел возведенных в квадрат: {sum_s}")
amount = len(s_subsequence1)
average_of_squares = sum_s / len(s_subsequence1) if s_subsequence1 else 0
print(f"Среднее арифметическое: {average_of_squares}")