s = str_min = str_max = input()
for _ in range(3):
    s = input()
    str_min = min(s, str_min)
    str_max = max(s, str_max)
print((ord(str_min[-1]) * ord(str_max[-1])) ** 2)
