n = int(input())
n_new = 0
while n != 0:
    n_new = n_new * 10 + n % 10
    n //= 10
print(n_new)
