import sys

def foo(i):
    if i==1:
        print(1)
        return
    elif i==2:
        print(2)
        return
    tmp = [0]*(i+1)
    tmp[1] = 1
    tmp[2] = 2
    tmp[3] = 4
    for a in range(4,i+1):
        tmp[a] = tmp[a-1]+tmp[a-2]+tmp[a-3]
    print(tmp[i])

a = int(sys.stdin.readline())

for i in range(a):
    foo(int(sys.stdin.readline()))