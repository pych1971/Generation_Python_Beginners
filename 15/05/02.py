s = input()
s_list = s.split()
s_list_new = []
eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in s_list:
    step = 0
    for j in i:
        if j.isalpha():
            step += 1
    new_world = ''
    for j in i:
        if j.upper() not in eng:
            new_world += j
        else:
            new_idx = eng.find(j.upper()) + step
            if new_idx > 25:
                new_idx -= 26
            elif new_idx < 0:
                new_idx += 26
            if j.islower():
                new_world += eng[new_idx].lower()
            else:
                new_world += eng[new_idx]
    s_list_new.append(new_world)
print(*s_list_new)
