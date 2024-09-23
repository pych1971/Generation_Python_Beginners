stop = False
for a in range(1, 151):
    if stop:
        break
    for b in range(a, 151):
        if stop:
            break
        for c in range(b, 151):
            if stop:
                break
            for d in range(c, 151):
                if stop:
                    break
                for e in range(1, 151):
                    if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
                        print(a + b + c + d + e)
                        stop = True
                        break
