# объявление функции
def is_password_good(password):
    up = False
    down = False
    dig = False
    for i in password:
        if i.isalpha() and i.isupper():
            up = True
        elif i.isalpha() and i.islower():
            down = True
        elif i.isdigit():
            dig = True
    return len(password) >= 8 and up and down and dig


# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))
