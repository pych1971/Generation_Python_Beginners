n = int(input())
n_min = n % 10
n_max = n % 10
n //= 10
while n != 0:
    if n % 10 < n_min:
        n_min = n % 10
    elif n % 10 > n_max:
        n_max = n % 10
    n //= 10
print('Максимальная цифра равна', n_max)
print('Минимальная цифра равна', n_min)
