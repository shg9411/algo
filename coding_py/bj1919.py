a = input()
b = input()

ac = [0]*26
bc = [0]*26

for c in a:
    ac[ord(c)-97] += 1
for c in b:
    bc[ord(c)-97] += 1
dif = 0
for i in range(26):
    dif += abs(ac[i]-bc[i])

print(dif)