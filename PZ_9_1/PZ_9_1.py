slowar = {k: k*k for k in range(7)}
print('Получившийся словарь:', slowar)
keys_remove = [1,2]
for key in keys_remove:
    slowar.pop(key)
print('Очищенный словарь:', slowar)