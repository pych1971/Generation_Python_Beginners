max = 0
for a in range(50):
    for b in range(50):
        for c in range(50):
            for d in range(50):
                if a ** 3 + b ** 3 == c ** 3 + d ** 3 and a != c and a != d:
                    print(a ** 3 + b ** 3)
