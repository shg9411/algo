import sys
input = sys.stdin.readline


def solve():
    n = int(input())
    last = [(idx, num)
            for idx, num in enumerate(map(int, input().split()), start=1)]
    changed = [list(map(int, input().split())) for _ in range(int(input()))]
    if not changed:
        sys.stdout.write(' '.join(map(str, (l[1] for l in last)))+'\n')
    else:
        pass


if __name__ == '__main__':
    for _ in range(int(input())):
        solve()
