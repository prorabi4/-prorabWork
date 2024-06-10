#Вариант 31.
#В магазинах имеются следующие товары. Магнит молоко, соль, сахар. Пятерочка - мясо, молоко, сыр.
#Перекресток молоко, творог, сыр, сахар. Определить:
#1. в каких магазинах нельзя приобрести сыр.
#2. в каких магазинах можно приобрести одновременно молоко и сахар.
#3. в каких магазинах можно приобрести соль.

magnit = {"молоко", "соль", "сахар"}
pyaterochka = {"мясо", "молоко", "сыр"}
perekrestok = {"молоко", "творог", "сыр", "сахар"}

if 'сыр' not in magnit:
    print('1. Сыра нет в Магните')
if 'сыр' not in pyaterochka:
    print('1. Сыра нет в Пятерочке')
if 'сыр' not in perekrestok:
    print('1. Сыра нет в Перекрестке')

if 'молоко' in magnit and 'сахар' in magnit:
    print('2. Молоко и сахар есть в Магните')
if 'молоко' in pyaterochka and 'сахар' in pyaterochka:
    print('2. Молоко и сахар есть в Пятерочке')
if 'молоко' in perekrestok and 'сахар' in perekrestok:
    print('2. Молоко и сахар есть в Перекрестке')

if 'соль' in magnit:
    print('3. Соль есть в Магните')
if 'соль' in pyaterochka:
    print('3. Соль есть в Пятерочке')
if 'соль' in perekrestok:
    print('3. Соль есть в Перекрестке')