numbers = list(map(int, input().split()))
squares = [i ** 3 for i in numbers]
for i in squares:
    print(i, end=' ')
