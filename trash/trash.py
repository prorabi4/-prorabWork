import re
p = re.compile(r"красн((ая)|(ое)|(ый))")
print("Найдено" if p.search("красная") else "Нет")
# выдаст Найдено
print("Найдено" if p.search("красное") else "Нет")
# выдаст Найдено
print("Найдено" if p.search("красный") else "Нет")
# выдаст Нет