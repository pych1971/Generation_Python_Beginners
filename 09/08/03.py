n = int(input())
for i in range(n):
    s = input()
    if len(s) == 2 and '0' <= s[0] <= '9' and 'А' <= s[1] <= 'П':
        print('YES')
    else:
        print('NO')
