result = []
for _ in range(3):
    tmp = input()
    if tmp.count('0')==1:
        result.append('A')
    elif tmp.count('0')==2:
        result.append('B')
    elif tmp.count('0')==3:
        result.append('C')
    elif tmp.count('0')==4:
        result.append('D')
    else:
        result.append('E')
print('\n'.join(result))