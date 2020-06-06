pwd = input().rstrip()
lv = [False for _ in range(5)]
for char in pwd:
    if char.islower():
        lv[0] = True
        continue
    if char.isupper():
        lv[1] = True
        continue
    if char.isdigit():
        lv[2] = True
        continue
    lv[3] = True
if len(pwd) >= 10:
    lv[4] = True

print("LEVEL{}".format(lv.count(True)))
