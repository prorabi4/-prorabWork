#Вар 31
#Дан список А размера П. Сформировать новый список В того же размера по следующему правилу:
# элемент Вк равен среднему арифметическому элементов списка А с номерами от 1 до К.
def ape(input_list):
    result_list = []
    prefix_sum = 0
    for idx, value in enumerate(input_list, start=1):
        prefix_sum += value
        average = prefix_sum / idx
        result_list.append(average)
    return result_list

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = ape(my_list)
print(result)