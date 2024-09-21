n = int(input())
result = 'YES'
n_last = n % 10
while n != 0:
    if n % 10 != n_last:
        result = 'NO'
    n //= 10
print(result)
