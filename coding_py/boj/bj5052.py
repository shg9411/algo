import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    tmp = []
    for _ in range(n):
        tmp.append(input().rstrip())
    tmp.sort()
    text = tmp[0]
    res = True
    for string in tmp[1:]:
        if string.startswith(text):
            res = False
            break
        else:
            text = string
    print("YES" if res else "NO")
