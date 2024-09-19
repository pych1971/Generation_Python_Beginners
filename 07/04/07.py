total = 0
sum = int(input())
while sum > 0:
    total += 1
    if sum >= 25:
        sum -= 25
    elif sum >= 10:
        sum -= 10
    elif sum >= 5:
        sum -= 5
    else:
        sum -= 1
print(total)
