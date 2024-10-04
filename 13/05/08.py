# объявление функции
def is_correct_bracket(text):
    result = 0
    for i in text:
        if i == '(':
            result += 1
        else:
            result -= 1
        if result < 0:
            return False
    return result == 0


# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))
