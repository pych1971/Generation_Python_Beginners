n = int(input())
s = ''
for i in range(ord('a'), ord('a') + n):
    s += chr(i)
print(list(s))
