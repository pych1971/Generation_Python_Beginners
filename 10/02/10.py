s = input()
count_f = s.count('f')
if count_f == 0:
    print(-2)
elif count_f == 1:
    print(-1)
else:
    print(s.find('f', s.find('f') + 1))
