# объявление функции
def is_pangram(text):
    for i in 'abcdefghijklmnopqrstuvwxyz':
        if i not in text.lower():
            return False
    return True


# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))
