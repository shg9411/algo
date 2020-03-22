import sys
input = sys.stdin.readline


def getCount(name, tmp):
    for char in name:
        if char == 'L':
            tmp[0] += 1
        elif char == 'O':
            tmp[1] += 1
        elif char == 'V':
            tmp[2] += 1
        elif char == 'E':
            tmp[3] += 1
    return tmp


boy = input()
n = int(input())
tmp = [0, 0, 0, 0]
arr = getCount(boy, tmp)
qqqqq = [input().rstrip() for _ in range(n)]
qqqqq.sort()
val = 0
res = qqqqq[0]
for name in qqqqq:
    tmp2 = arr[:]
    girl = getCount(name, tmp2)
    tmpVal = ((girl[0]+girl[1])*(girl[0]+girl[2])*(girl[0]+girl[3])
              * (girl[1]+girl[2])*(girl[1]+girl[3])*(girl[2]+girl[3])) % 100
    if tmpVal > val:
        val = tmpVal
        res = name
print(res)
