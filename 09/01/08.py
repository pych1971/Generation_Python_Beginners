total_plus = total_star = 0
for i in input():
    if i == '+':
        total_plus += 1
    elif i == '*':
        total_star += 1
print('Символ + встречается', total_plus, 'раз')
print('Символ * встречается', total_star, 'раз')
