phrases = []
requests = []
for _ in range(int(input())):
    phrases.append(input())
for _ in range(int(input())):
    requests.append(input())
for i in phrases:
    for j in requests:
        if j.lower() not in i.lower():
            break
    else:
        print(i)
