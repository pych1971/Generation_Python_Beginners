weight_max = 0
word_max = ''
weight = 0
for i in range(4):
    s = input()
    for j in s:
        weight += ord(j)
    if weight > weight_max:
        weight_max = weight
        word_max = s
    weight = 0
print(word_max)
