number = input()
if number[0] in 'АВЕКМНОРСТУХ' and number[4] in 'АВЕКМНОРСТУХ' and number[5] in 'АВЕКМНОРСТУХ' and number[
                                                                                                   1:4].isdigit() and (
        number[7:9].isdigit() and len(number) == 9 or number[7:10].isdigit() and len(number) == 10) and number[
    6] == '_':
    print('YES')
else:
    print('NO')
