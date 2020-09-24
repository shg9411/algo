import sys


def solve():
    a = sorted(sys.stdin.read().split()[1:], key=lambda x: x*5)
    r = '~'
    for k in a:
        if k[0] == '0':
            continue
        tmp = a[:]
        tmp.remove(k)
        r = min(r, k+''.join(tmp))
    print(r if r != '~' else "INVALID")


if __name__ == "__main__":
    solve()
