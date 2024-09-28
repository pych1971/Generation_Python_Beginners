day, weight = int(input()), float(input())
if weight > 100 - 0.2 * day:
    print('Что-то пошло не так')
else:
    print('Все идет по плану')
print(f'#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {weight} кг, ЦЕЛЬ по ВЕСУ = {100 - 0.2 * day} кг')
