import sys
input = sys.stdin.readline


def solve():
    res = []
    input()
    x = dict()
    for num in input().split():
        if num in x:
            x[num]+=1
        else:
            x[num] = 1
    input()
    for n in input().split():
        res.append(x.get(n,0))
    sys.stdout.write(' '.join(map(str, res)))


if __name__ == '__main__':
    solve()