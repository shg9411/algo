a = input()
if a[:2] == '10':
    print(10+int(a[2:]))
else:
    print(int(a[0])+int(a[1:]))
