n = int(input())
if (n // 1000 + n % 10 == n % 1000 // 100 - n % 100 // 10):
    print('ДА')
else:
    print('НЕТ')
