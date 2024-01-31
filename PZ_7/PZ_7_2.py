#Вар 31
#Дана строка, состоящая из русских слов, разделенных пробелами
#(одним или несколькими). Найти длину самого короткого слова.
def shortest_word_length(string):
    words = string.split()
    shortest = float("inf")

    for word in words:
        length = len(word)
        if length < shortest:
            shortest = length
    return shortest
a = input('Введите ваш любимый анекдот: ')
result = shortest_word_length(a)
print(f"Самое короткое слово в строке: {result} символов")