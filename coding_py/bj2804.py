a, b = input().split()
for idx, char in enumerate(a):
    if b.find(char) >= 0:
        change = b.find(char)
        break

for i in range(len(b)):
    if i != change:
        print('.'*idx+b[i]+'.'*(len(a)-idx-1))
    else:
        print(a)
