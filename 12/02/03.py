numbers = list(map(int, input().split()))
print(*numbers, sep='+', end='=')
print(sum(numbers))
