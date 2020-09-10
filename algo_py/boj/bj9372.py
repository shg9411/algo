import sys
input = sys.stdin.readline


def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        sys.stdout.write(str(n-1)+'\n')
        for _ in range(m):
            input()
    


if __name__ == '__main__':
    solve()
