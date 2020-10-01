import sys
input = sys.stdin.readline

def solve():
    s = sorted([input().rstrip() for _ in range(int(input()))])
    t=s[0]
    for m in s[1:]:
        if m.startswith(t):
            return "NO"
        else:
            t=m
    return "YES"


if __name__=='__main__':
    for _ in range(int(input())):
        print(solve())