n = int(input())
n_second = n % 10
while n >= 9:
    n_second = n % 10
    n //= 10
print(n_second)
