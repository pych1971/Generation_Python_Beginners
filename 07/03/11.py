x1 = 1
x2 = 1
for i in range(1, int(input()) + 1):
    print(x1, end=' ')
    x1, x2 = x2, x1 + x2
