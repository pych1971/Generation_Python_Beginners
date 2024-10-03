# объявление функции
def print_digit_sum(num):
    sum = 0
    for i in str(num):
        sum += int(i)
    print(sum)


# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)
