l, m = list(map(int, input().split())), list(map(int, input().split()))
print(*[l[i] + m[i] for i in range(len(l))])
