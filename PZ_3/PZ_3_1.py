# Вариант 31 задание 1
# Даны целые числа a, b, c, являющиеся сторонами некоторого треугольника. Проверить истинность высказывания:
# «Треугольник со сторонами а, b, с является равнобедренным».

try:
    a = int(input('Введите сторону "a" = '))
    b = int(input('Введите сторону "b" = '))
    c = int(input('Введите сторону "c" = '))
    if a == b or b == c or c == a:
        print('Треугольник abc равнобедренный')
    else:
        print('Треугольник abc не является равнобедренным')
except:
    print('Введите корректное число!!')