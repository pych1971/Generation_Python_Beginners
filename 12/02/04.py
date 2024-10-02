number = input().split('-')
if number[0] == '7':
    number.pop(0)
if len(number) == 3 and len(number[0]) == len(number[1]) == 3 and len(number[2]) == 4 and (
        number[0] + number[1] + number[2]).isdigit():
    print('YES')
else:
    print('NO')
