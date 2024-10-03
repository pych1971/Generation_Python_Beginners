# объявление функции
def find_all(target, symbol):
    founded = []
    for i in range(len(target)):
        if target[i] == symbol:
            founded.append(i)
    return founded


# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))
