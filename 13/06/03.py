# объявление функции
def solve(a, b, c):
    d = b ** 2 - 4 * a * c
    if d == 0:
        return -b / 2 / a, -b / 2 / a
    else:
        res1 = (-b + d ** 0.5) / 2 / a
        res2 = (-b - d ** 0.5) / 2 / a
        return min(res1, res2), max(res1, res2)


# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)
