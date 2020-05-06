import sys

for line in sys.stdin.read().splitlines():
    res = [0,0,0,0]
    for char in line:
        if char==' ':
            res[3]+=1
        elif char.isdigit():
            res[2]+=1
        elif char.isupper():
            res[1]+=1
        else:
            res[0]+=1
    print(' '.join(map(str,res)))