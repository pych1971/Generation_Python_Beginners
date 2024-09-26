s = input()
symbol_max = s[0]
symbol_count_max = s.count(s[0])
for i in s:
    if s.count(i) >= symbol_count_max:
        symbol_max = i
        symbol_count_max = s.count(i)
print(symbol_max)
