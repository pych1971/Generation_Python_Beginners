a, b = int(input()), int(input())
total = 0
for i in range(a, b + 1):
    if i ** 3 % 10 == 4 or i ** 3 % 10 == 9:
        total += 1
print(total)
