total = 0
for i in input().split():
    if i.lower() in ['a', 'an', 'the']:
        total += 1
print(f'Общее количество артиклей: {total}')
