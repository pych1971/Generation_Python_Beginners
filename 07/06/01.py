n = int(input())
min_sep = 1
for i in range(2, n + 1):
    if n % i == 0:
        min_sep = i
        break
print(min_sep)
