n = int(input()[1:])
program = []
for i in range(n):
    program.append(input())
for i in program:
    if '#' in i:
        print(i[:i.find('#')].rstrip())
    else:
        print(i)
