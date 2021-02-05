import sys
input = sys.stdin.readline


def solve():
    p = list(input().rstrip().replace('RR', ''))
    n = int(input())
    res = input().rstrip()[1:-1].split(',')
    i = j = rev = 0
    for cmd in p:
        if cmd == 'R':
            rev = not rev
        elif rev:
            j += 1
        else:
            i += 1
    if i > n-j:
        return 'error'
    else:
        res = res[i:n-j]
        return '['+','.join(res[::-1] if rev else res)+']'


if __name__ == '__main__':
    r = []
    for _ in range(int(input())):
        r.append(solve())
    sys.stdout.write('\n'.join(r))
