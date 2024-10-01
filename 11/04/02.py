l = []
f = []
for _ in range(int(input())):
    l.append(int(input()))
    f.append(l[-1] ** 2 + 2 * l[-1] + 1)
print(*l, sep='\n')
print()
print(*f, sep='\n')
