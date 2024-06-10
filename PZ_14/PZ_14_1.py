# Вариант 31
# Из исходного текстового файла (price.txt) выбрать все цены. Посчитать количество полученных элементов.
import re
with open('price.txt', 'r', encoding='utf-8') as file:
    text = file.read()
findalldigits = re.findall(r'\d+.\w+.', text)
with open('findalldigits.txt', 'w') as file:
    file.write(', '.join(findalldigits))
print('Колличество элементов:',len(findalldigits))
