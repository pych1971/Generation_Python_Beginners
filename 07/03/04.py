total = 0
for i in range(1, int(input()) + 1):
    if i ** 2 % 10 in (2, 5, 8):
        total += i
print(total)
