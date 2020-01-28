def toTwelve(i):
    num = 0
    while 1<= i:
        modNum = i%12
        num += modNum
        i = i//12
    return num


def toHexa(i):
    num = 0
    tmp = str(hex(i))[2:]
    for char in tmp:
        if char.isalpha():
            num += ord(char)-87
        else:
            num += int(char)
    return num


for i in range(1000, 10000):
    ten = sum(map(int, list(str(i))))
    twelve = toTwelve(i)
    hexa = toHexa(i)
    if ten == twelve == hexa:
        print(i)
