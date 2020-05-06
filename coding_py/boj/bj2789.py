delete = 'CAMBRIDGE'
result = []
for c in input():
    if c not in delete:
        result.append(c)
print(''.join(result))
