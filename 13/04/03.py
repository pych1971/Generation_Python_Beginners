# объявление функции
def get_factors(num):
    sub = []
    for i in range(1, num + 1):
        if num % i == 0:
            sub.append(i)
    return sub


# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))
