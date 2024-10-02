l = list(map(int, input().split()))
id_min = l.index(min(l))
id_max = l.index(max(l))
l[id_max], l[id_min] = l[id_min], l[id_max]
print(*l)
