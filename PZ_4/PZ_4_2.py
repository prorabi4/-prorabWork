#Дано целое число N (>0). С помощью операций деления нацело и взятия остатка от деления определить,
 #имеются ли в записи числа N нечетные цифры. Если имеются, то вывести TRUE, если нет - вывести FALSE.

numbers = []
first = 1
div = 10
end = False
try:
    number = int(input('Введите любое целое число N, которое больше 0: '))
    if number > 0:
        ost = number % 10
        numbers.append(ost)
        while first != 0:
            first = number // div
            div = div * 10
            ost = first % 10
            numbers.append(ost)
        for i in numbers:
            if i % 2 != 0:
                end = True
                print(end, '- В вашем числе присутствуют нечетные числа!')
                exit()
        print(end, '- В вашем числе отсутствуют нечетные числа!')

    else:
        print('Введены некорректные данные')
except ValueError:
    print('Введены некорректные данные')