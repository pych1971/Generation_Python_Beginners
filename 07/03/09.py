biggest = 0
next_biggest = 0
for i in range(int(input())):
    x = int(input())
    if x > biggest:
        next_biggest, biggest = biggest, x
    elif x > next_biggest:
        next_biggest = x
print(biggest, next_biggest, sep='\n')
