n = int(input())
n_sum = 0
n_last = n_first = n % 10
n_quantity = 0
n_mult = 1
while n != 0:
    n_sum += n % 10
    n_quantity += 1
    n_mult *= n % 10
    n_first = n % 10
    n //= 10
print(n_sum, n_quantity, n_mult, n_sum / n_quantity, n_first, n_last + n_first, sep='\n')
