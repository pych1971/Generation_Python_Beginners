s = input()
total_eng = 0
total_rus = 0
chr_eng = 'eyopaxcETOPAHXCBM'
chr_rus = 'еуорахсЕТОРАНХСВМ'
for i in s:
    total_eng += ord(i) * 3
    if i in chr_eng:
        for j in range(len(chr_eng)):
            if i == chr_eng[j]:
                total_rus += ord(chr_rus[j]) * 3
    else:
        total_rus += ord(i) * 3
print(f'Старая стоимость: {total_eng}🐝')
print(f'Новая стоимость: {total_rus}🐝')
