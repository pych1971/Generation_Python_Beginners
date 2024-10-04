# объявление функции
def is_palindrome(text):
    new_text = ''
    for i in text:
        if i not in ' ,.!?-':
            new_text += i
    return new_text.lower() == new_text[-1::-1].lower()


# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))
