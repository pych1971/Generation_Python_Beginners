s = input()
while '[u-' in s:
    idx = s.find('[u-')
    s = s.replace(s[idx:idx + 8], chr(int(s[idx + 3:idx + 7])))
print(s)
