n = int(input())
total_3 = 0
last_number = n % 10
total_last_number = 0
total_even = 0
sum_more_5 = 0
prod_more_7 = 1
total_0_5 = 0
while n > 0:
    x = n % 10
    if x == 3:
        total_3 += 1
    if x == last_number:
        total_last_number += 1
    if x % 2 == 0:
        total_even += 1
    if x > 5:
        sum_more_5 += x
    if x > 7:
        prod_more_7 *= x
    if x == 0 or x == 5:
        total_0_5 += 1
    n //= 10
print(total_3, total_last_number, total_even, sum_more_5, prod_more_7, total_0_5, sep='\n')
