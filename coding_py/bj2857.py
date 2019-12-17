fbi = []
for i in range(1, 6):
    if "FBI" in input():
        fbi.append(str(i))
print(' '.join(fbi) if fbi else 'HE GOT AWAY!')
