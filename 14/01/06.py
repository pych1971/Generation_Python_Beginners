# объявление функции
def is_magic(date):
    date_list = list(map(int, date.split('.')))
    return date_list[0] * date_list[1] == date_list[2] % 100


# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))
