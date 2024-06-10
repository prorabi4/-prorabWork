# 2. Из предложенного текстового файла (text18-31.txt) вывести на экран его содержимое, количество символов,
#принадлежащих к группе букв. Сформировать новый файл, в который поместить строку наименьшей длины.
with open('text18-31.txt', 'r') as file:
    content = file.read()
    letter_count = sum(c.isalpha() for c in content)

print("Содержимое файла:")
print(content)
print(f"Количество букв: {letter_count}")
shortest_line = min(content.splitlines(), key=len)
with open('new_file.txt', 'w') as new_file:
    new_file.write(shortest_line)
