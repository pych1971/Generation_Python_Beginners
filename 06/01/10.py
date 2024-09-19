n = int(input())
n1 = n // 100
n2 = n % 100 // 10
n3 = n % 10
if n1 + n2 + n3 - max(n1, n2, n3) - min(n1, n2, n3) == max(n1, n2, n3) - min(n1, n2, n3):
    print('Число интересное')
else:
    print('Число неинтересное')
