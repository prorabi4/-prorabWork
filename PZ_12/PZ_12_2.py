# 2. Из заданной строки отобразить только символы нижнего регистра. Использовать библиотеку string.
# Строка 'In PyCharm, you can specify third-party standalone applications and run them as External Tools'.

import string
# -*- coding: utf8 -*-
main_str = 'In PyCharm, you can specify third-party standalone applications and run them as External Tools'
x = [i for i in main_str if i.islower() or i.isspace()]
print(''.join(x))
