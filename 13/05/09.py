# объявление функции
def convert_to_python_case(text):
    new_text = ''
    for i in text:
        if i.isupper():
            new_text += '_' + i.lower()
        else:
            new_text += i
    return new_text[1:]


# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
