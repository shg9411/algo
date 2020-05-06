import sys

i = 2
while 1:
    tmp = sys.stdin.readline().rstrip()
    if tmp == 'Was it a cat I saw?':
        break
    print(tmp[::i])
    i += 1
