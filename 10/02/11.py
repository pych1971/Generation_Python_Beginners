s = input()
h1 = s.find('h')
h2 = s.rfind('h')
s_new = s[:h1] + s[h2:h1:-1] + s[h2:]
print(s_new)
