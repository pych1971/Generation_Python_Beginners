a, b = int(input()), int(input())
n_max = a
n_sum = 0
n_sum_max = 0
for i in range(a, b + 1):
    for j in range(1, i + 1):
        if i % j == 0:
            n_sum += j
    if n_sum >= n_sum_max:
        n_sum_max = n_sum
        n_max = i
    n_sum = 0
print(n_max, n_sum_max)
