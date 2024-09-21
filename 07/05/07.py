n = int(input())
n_last = n % 10
result = 'YES'
while n != 0:
    if n % 10 < n_last:
        result = 'NO'
    n_last = n % 10
    n //= 10
print(result)
