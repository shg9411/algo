s = input()
if s.startswith('0x'):
    print(int(s, 16))
elif s.startswith('0'):
    print(int(s, 8))
else:
    print(s)
