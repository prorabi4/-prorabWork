# Вариант 31
# Сгенерировать словарь вида (0:0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36},
# удалить из него второй и третий элементы. Отобразить исходный и получившийся словарь. Использовать for, range.

                                    slowar = {k: k*k for k in range(7)}
                                    print('Получившийся словарь:', slowar)
                                    keys_remove = [1,2]
                                    for key in keys_remove:
                                        slowar.pop(key)
                                    print('Очищенный словарь:', slowar)
