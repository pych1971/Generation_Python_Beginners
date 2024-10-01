l = []
for _ in range(int(input())):
    l.append(input())
k = int(input())
s = ''
for i in l:
    if len(i) < k:
        continue
    else:
        s += i[k - 1]
print(s)
