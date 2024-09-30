s1, s2 = input(), input()
s1_res = ''
s2_res = ''
for i in s1:
    if i.isalpha():
        s1_res += i
for i in s2:
    if i.isalpha():
        s2_res += i
if s1_res.lower() == s2_res.lower():
    print('YES')
else:
    print('NO')
