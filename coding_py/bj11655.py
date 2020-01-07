s = input().rstrip()
res =''
for char in s:
    if char.isupper():
        if ord(char)<=77:
            res+=chr(ord(char)+13)
        else:
            res+=chr(ord(char)-13)
    elif char.islower():
        if ord(char)<=109:
            res+=chr(ord(char)+13)
        else:
            res+=chr(ord(char)-13)
    else:
        res+=char
print(res)