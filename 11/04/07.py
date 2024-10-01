negatives = []
zeros = []
positives = []
for _ in range(int(input())):
    x = int(input())
    if x < 0:
        negatives.append(x)
    elif x == 0:
        zeros.append(x)
    else:
        positives.append(x)
print(*negatives, *zeros, *positives, sep='\n')
