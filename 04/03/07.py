color1, color2 = input(), input()
if color1 == color2 and (color1 == 'красный' or color1 == 'синий' or color1 == 'желтый'):
    print(color1)
elif color1 == 'красный' and color2 == 'синий' or color1 == 'синий' and color2 == 'красный':
    print('фиолетовый')
elif color1 == 'красный' and color2 == 'желтый' or color1 == 'желтый' and color2 == 'красный':
    print('оранжевый')
elif color1 == 'синий' and color2 == 'желтый' or color1 == 'желтый' and color2 == 'синий':
    print('зеленый')
else:
    print('ошибка цвета')
