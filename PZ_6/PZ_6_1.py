#Вар 31
#Дан целочисленный список размера N. Увеличить все нечетные числа, содержащиеся в списке,
# на исходное значение последнего нечетного числа. Если нечетные числа в списке отсутствуют,
# то оставить список без изменений.
def odd_numbers(lst):
    odds = [x for x in lst if x % 2 != 0]
    if odds:
        last_odd = odds[-1]
        return [x + last_odd if x % 2 != 0 else x for x in lst]
    else:
        return lst
my_list = [1, 2, 3, 4, 5, 6, 7]
modified_list = odd_numbers(my_list)
print(modified_list)