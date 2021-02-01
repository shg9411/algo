import io
import os
import sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def solve():
    n = int(input())
    nxt = [0]+list(map(int, input().split()))
    visited = [0]*(n+1)
    r = 0
    for i in range(1, n+1):
        if visited[i]:
            continue
        now = i
        while not visited[now]:
            visited[now]=1
            now=nxt[now]
        other=i
        while other!=now:
            r+=1
            other=nxt[other]
    return r


if __name__ == '__main__':
    res = []
    for _ in range(int(input())):
        res.append(solve())
    print('\n'.join(map(str, res)))