a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if a2 > b1 or a1 > b2:
    print('пустое множество')
elif b1 == a2:
    print(b1)
elif b2 == a1:
    print(b2)
elif a1 >= a2 and b1 <= b2:
    print(a1, b1)
elif a1 < a2 and b1 > b2:
    print(a2, b2)
elif a1 == a2:
    if b1 > b2:
        print(a1, b2)
    else:
        print(a1, b1)
elif b1 == b2:
    if a1 > a2:
        print(a1, b1)
    else:
        print(a2, b1)
elif a1 > a2:
    print(a1, b2)
else:
    print(a2, b1)
