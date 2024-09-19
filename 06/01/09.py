a, b, c = int(input()), int(input()), int(input())
middle = c
if b <= a <= c or b >= a >= c:
    middle = a
elif a <= b <= c or a >= b >= c:
    middle = b
print(max(a, b, c), middle, min(a, b, c), sep='\n')
