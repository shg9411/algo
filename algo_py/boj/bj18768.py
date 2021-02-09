import math
import sys
input = sys.stdin.readline


def solve():
    n, k = map(int, input().split())
    person = sorted([(-attack+defense, attack, defense) for attack,
                     defense in zip(map(int, input().split()), map(int, input().split()))])
    cnt = math.ceil((n-k)/2)
    cur = res = sum(x[1] for x in person[:cnt])+sum(x[2] for x in person[cnt:])
    i, j = cnt, n-cnt
    while i-j < k:
        cur -= person[i][0]
        i += 1
        j -= 1
        if i-j <= k:
            res = max(res, cur)
    return res


if __name__ == '__main__':
    for _ in range(int(input())):
        print(solve())
