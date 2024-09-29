s = str_min = str_max = input()
while s != 'КОНЕЦ':
    str_min = min(s, str_min)
    str_max = max(s, str_max)
    s = input()
print('Минимальная строка ⬇️: ' + str_min)
print('Максимальная строка ⬆️: ' + str_max)
