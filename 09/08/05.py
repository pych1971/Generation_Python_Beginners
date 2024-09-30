s1, s2, s3 = input(), input(), input()
s_max = max(s1, s2, s3)
s_min = min(s1, s2, s3)
s_mid = ''
if s1 != s_max and s1 != s_min:
    s_mid = s1
elif s2 != s_max and s2 != s_min:
    s_mid = s2
else:
    s_mid = s3
print(s_min, s_mid, s_max)
