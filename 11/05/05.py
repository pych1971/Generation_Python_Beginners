correct = 'ДА'
for i in input().split('.'):
    if 0 <= int(i) <= 255:
        continue
    else:
        correct = 'НЕТ'
        break
print(correct)
