n = int(input())
n_2 = ''
while n > 0:
    n_2 = str(n % 2) + n_2
    n //= 2
print(n_2)
