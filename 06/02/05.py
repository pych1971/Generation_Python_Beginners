a, b, c = len(input()), len(input()), len(input())
if max(a, b, c) - (a + b + c - max(a, b, c) - min(a, b, c)) == a + b + c - max(a, b, c) - min(a, b, c) - min(a, b, c):
    print('YES')
else:
    print('NO')
