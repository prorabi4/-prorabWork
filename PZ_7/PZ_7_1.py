#Вар 31
#Даны строки S и So. Найти количество cхождений строки Ѕо в строку Ѕ.
def count1(moin, substring):
    return moin.count(substring)
S = input('Введите ваш любимый анекдот:')
So = input('Введите любое повторяющееся слово из написанного анекдота:')

count = count1(S, So)
print(f"Число в count '{So}' в '{S}' : {count}")