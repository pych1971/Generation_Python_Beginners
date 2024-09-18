x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if x2 > x1:
    x1, x2 = x2, x1
if y2 > y1:
    y1, y2 = y2, y1
if x1 - x2 == y1 - y2:
    print('YES')
else:
    print('NO')
