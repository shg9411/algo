after = input()
before = []
for c in after:
    if ord(c) < 68:
        before.append(chr(ord(c)+23))
    else:
        before.append(chr(ord(c)-3))
print(''.join(before))
