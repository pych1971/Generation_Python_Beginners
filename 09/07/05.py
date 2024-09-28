s = input()
total = 0
for i in s:
    total += ord(i) * 3
print(f"Текст сообщения: '{s}'")
print(f'Стоимость сообщения: {total}🐝')
