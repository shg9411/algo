import sys
input = sys.stdin.readline
res = []
m = int(input())
n = 0
for _ in range(m):
    cmd = input().split()
    if cmd[0]=='add':
        n |= 1<<(int(cmd[1])-1)
    elif cmd[0]=='remove':
        n &= ~(1<<(int(cmd[1])-1))
    elif cmd[0]=='check':
        print(0 if n&(1<<(int(cmd[1])-1))==0 else 1)
    elif cmd[0]=='toggle':
        n ^= (1<<(int(cmd[1])-1))
    elif cmd[0]=='all':
        n = (1<<20)-1
    elif cmd[0]=='empty':
        n = 0