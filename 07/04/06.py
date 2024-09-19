grade = int(input())
total = 0
while 0 < grade < 6:
    if grade == 5:
        total += 1
    grade = int(input())
print(total)
