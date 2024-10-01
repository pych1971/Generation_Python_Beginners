l = []
for _ in range(int(input())):
    l.append(input())
req = input()
for i in l:
    if req.lower() in i.lower():
        print(i)
