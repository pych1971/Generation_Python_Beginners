s = input()
total_vow = 0
total_con = 0
for i in s:
    if i in 'ауоыиэяюеАУОЫИЭЯЮЕ':
        total_vow += 1
    elif i in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
        total_con += 1
print('Количество гласных букв равно', total_vow)
print('Количество согласных букв равно', total_con)
