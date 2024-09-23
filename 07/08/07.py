for n in range(1, 100 // 10 + 1):
    for k in range(1, 100 // 5 + 1):
        for m in range(1, 100 * 2 + 1):
            if 10 * n + 5 * k + 0.5 * m == 100 and n + k + m == 100:
                print(n, k, m)
