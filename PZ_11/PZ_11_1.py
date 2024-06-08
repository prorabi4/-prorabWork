# 1. Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
#последовательности из целых положительных и отрицательных чисел.
#Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
# Элементы первого и второго файлов:
# Количество элементов первого и второго файлов:
# Элементы первой трети:
# Минимальный элемент первой трети:

import random

with open('file1.txt', 'w') as file1:
    numbers1 = [random.randint(-10, 10) for i in range(5)]
    file1.write('\n'.join(map(str, numbers1)))


with open('file2.txt', 'w') as file2:
    numbers2 = [random.randint(-10, 10) for i in range(5)]
    file2.write('\n'.join(map(str, numbers2)))


with open('result.txt', 'w') as result_file:
    with open('file1.txt', 'r') as file1, open('file2.txt', 'r') as file2:
        elements1 = file1.read().splitlines()
        elements2 = file2.read().splitlines()
        result_file.write(f"Элементы первого файла: {', '.join(elements1)}\n")
        result_file.write(f"Элементы второго файла: {', '.join(elements2)}\n")
        result_file.write(f"Количество элементов первого файла: {len(elements1)}\n")
        result_file.write(f"Количество элементов второго файла: {len(elements2)}\n")

        third_of_elements = len(elements1) % 3
        result_file.write(f"Элементы первой трети первого файла: {', '.join(elements1[:third_of_elements])}\n")
        result_file.write(
            f"Минимальный элемент первой трети первого файла: {min(map(int, elements1[:third_of_elements]))}\n")
