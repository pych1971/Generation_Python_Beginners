word = input()
total = 0
while word != 'стоп' and word != 'хватит' and word != 'достаточно':
    total += 1
    word = input()
print(total)
