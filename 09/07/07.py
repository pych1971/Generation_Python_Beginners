n = int(input())
s = input()
s_new = ''
for i in s:
    new_ord = ord(i) - n
    if new_ord < 97:
        new_ord = 123 - (97 - new_ord)
    s_new += chr(new_ord)
print(s_new)
