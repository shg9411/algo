var = input().rstrip()
strlen = len(var)

if var[0].isupper() or var[0] == '_':
    print("Error!")
    exit()

upper = False
underSlash = False

for char in var:
    if char.isupper():
        upper = True
    if char == '_':
        underSlash = True
res = ''
if upper and underSlash:
    print("Error!")
elif upper:
    for char in var:
        if char.isupper():
            res += '_'+char.lower()
        else:
            res += char
    print(res)
elif underSlash:
    under = False
    for i in range(strlen):
        if var[i] == '_':
            if under == True or i == strlen-1:
                print("Error!")
                exit()
            under = True
            continue
        if under:
            res += var[i].upper()
            under = False
        else:
            res += var[i]
    print(res)
else:
    print(var)
