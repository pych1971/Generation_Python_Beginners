n = int(input())
result = ''
for i in range(1, n + 1):
    s = input()
    if s == '' or s.isspace():
        result += str(i) + ': COMMENT SHOULD BE DELETED\n'
    else:
        result += str(i) + ': ' + s + '\n'
print(result)
