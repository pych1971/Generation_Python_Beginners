n = int(input())
for i in range(1, n + 1):
    if i <= n // 2 + 1:
        m = i
    else:
        m -= 1
    for j in range(1, m + 1):
        print('*', end='')
    print()
