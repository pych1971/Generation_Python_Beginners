code = int(input('Шифрование/дешифрование (1/-1): '))
step = int(input('Шаг: ')) * code
s = input('Строка: ')
s_new = ''
eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
for i in s:
    if i.upper() not in (eng + rus):
        s_new += i
    elif i.upper() in eng:
        new_idx = eng.find(i.upper()) + step
        if new_idx > 25:
            new_idx -= 26
        elif new_idx < 0:
            new_idx += 26
        if i.islower():
            s_new += eng[new_idx].lower()
        else:
            s_new += eng[new_idx]
    elif i.upper() in rus:
        new_idx = rus.find(i.upper()) + step
        if new_idx > 31:
            new_idx -= 32
        elif new_idx < 0:
            new_idx += 32
        if i.islower():
            s_new += rus[new_idx].lower()
        else:
            s_new += rus[new_idx]
print(s_new)
