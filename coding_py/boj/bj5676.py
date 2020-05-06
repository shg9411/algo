import sys
input = sys.stdin.readline

n, m = map(int, input().split())

f_t = [0 for _ in range(10000)]
#v_t = [0 for _ in range(10000)]


def sum(i):
    res = 0
    while i > 0:
        res += f_t[i]
        i -= (i & -i)
    return res


def update(i, diff):
    while i <= n:
        f_t[i] += diff
        i += (i & -i)


v_t = [0]+list(map(int, input().split()))+[0 for _ in range(10000)]
for _ in range(m):
    a, b, c = input().split()
    '''
    if a == 0:
        if b > c:
            b, c = c, b
        print(sum(c)-sum(b-1))
    else:
        update(b, c-v_t[b])
        v_t[b] = c
    '''
    print(a,b,c)
