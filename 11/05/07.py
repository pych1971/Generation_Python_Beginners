l = input().split()
total = 0
for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] == l[j]:
            total += 1
print(total)
