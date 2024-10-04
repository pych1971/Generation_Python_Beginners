# объявление функции
def is_one_away(word1, word2):
    dif_chars = 0
    for i in range(min(len(word1), len(word2))):
        if word1[i] != word2[i]:
            dif_chars += 1
    return len(word1) == len(word2) and dif_chars == 1


# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))
