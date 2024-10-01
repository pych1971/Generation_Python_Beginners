n = int(input())
n_next = int(input())
n_sum = []
for i in range(1, n):
    n_prev, n_next = n_next, int(input())
    n_sum.append(n_prev + n_next)
print(n_sum)
