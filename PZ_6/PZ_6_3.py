#Вар 31
#Дан список размера N, все элементы которого, кроме последнего, упорядочены по возрастанию.
#Сделать список упорядоченным, переместив последний элемент на новую позицию.
def reorder_last_element(input_list):
    sort_list = sorted(input_list)
    return sort_list
my_list = [1, 2, 3, 5, 6, 7, 8, 4]
result = reorder_last_element(my_list)
print(result)