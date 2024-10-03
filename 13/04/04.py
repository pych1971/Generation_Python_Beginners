# объявление функции
def number_of_factors(num):
    sub = 0
    for i in range(1, num + 1):
        if num % i == 0:
            sub += 1
    return sub


# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))
