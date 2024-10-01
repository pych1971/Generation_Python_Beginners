n = int(input())
s = []
for _ in range(n):
    s.append(int(input()))
del s[1::2]
print(s)
