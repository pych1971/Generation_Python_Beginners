n = int(input())
next_book = input()
order_ok = 'YES'
for i in range(n - 1):
    prev_book, next_book = next_book, input()
    if next_book < prev_book:
        order_ok = 'NO'
print(order_ok)
