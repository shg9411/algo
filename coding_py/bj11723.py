import sys
input = sys.stdin.readline
m = int(input())
s = set()
for _ in range(m):
    cmd = input().split()
    if cmd[0] == 'empty':
        s = set()
    elif cmd[0] == 'all':
        s = set(range(1, 21))
    else:
        n = int(cmd[1])
        if cmd[0] == 'add':
            s.add(n)
        elif cmd[0] == 'remove':
            s.remove(n)
        elif cmd[0] == 'check':
            print(1 if n in s else 0)
        elif cmd[0] == 'toggle':
            if n in s:
                s.remove(n)
            else:
                s.add(n)
