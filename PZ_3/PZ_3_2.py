# Вариант 31 задание 2
# Даны три числа. Найти сумму двух наибольших из них.

try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    c = int(input("Введите третье число: "))
    if a >= b and a >= c:
        z = a + max(b, c)
    elif b >= a and b >= c:
        z = b + max(a, c)
    else:
        z = c + max(a, b)
    print('Сумма двух наибольших чисел = ',z)
except:
    print('Введите верное значение!!!')