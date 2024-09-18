x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
a1 = 'черная'
a2 = 'черная'
if x1 % 2 == y1 % 2:
    a1 = 'белая'
if x2 % 2 == y2 % 2:
    a2 = 'белая'
if a1 == a2:
    print('YES')
else:
    print('NO')
