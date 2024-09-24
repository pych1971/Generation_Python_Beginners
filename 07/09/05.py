n = int(input())
while n >= 10:
    m, n = n, 0
    while m > 0:
        n += m % 10
        m //= 10
print(n)
