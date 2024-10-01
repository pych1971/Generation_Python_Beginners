l = []
for _ in range(int(input())):
    l.append(int(input()))
for i in range((len(l))):
    if l[i] == max(l):
        del l[i]
        break
for i in range((len(l))):
    if l[i] == min(l):
        del l[i]
        break
print(*l, sep='\n')
