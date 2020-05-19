import sys
from collections import deque
input = sys.stdin.readline
nm = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def solve():
    t = int(input())
    for _ in range(t):
        h, w = map(int, input().split())
        visited = [[False for _ in range(w+2)] for _ in range(h+2)]
        bd = [list('.'*(w+2))]
        for _ in range(h):
            bd.append(['.']+list(input().rstrip())+['.'])
        bd.append(list('.'*(w+2)))
        key = [0 for _ in range(26)]
        for char in input().rstrip():
            try:
                key[ord(char)-97] = 1
            except:
                continue
        res = 0
        q = deque()
        notNow = [deque() for _ in range(26)]
        q.append((0, 0))
        visited[0][0] = True
        while q:
            x, y = q.popleft()
            for _x, _y in nm:
                tx, ty = x+_x, y+_y
                if 0 <= tx < h+2 and 0 <= ty < w+2:
                    if visited[tx][ty] or bd[tx][ty] == '*':
                        continue
                    visited[tx][ty] = True
                    if bd[tx][ty].isupper():
                        if key[ord(bd[tx][ty])-65]:
                            q.append((tx, ty))
                        else:
                            notNow[ord(bd[tx][ty])-65].append((tx, ty))
                    elif bd[tx][ty].islower():
                        q.append((tx, ty))
                        if not key[ord(bd[tx][ty])-97]:
                            key[ord(bd[tx][ty])-97] = 1
                            while notNow[ord(bd[tx][ty])-97]:
                                q.append(notNow[ord(bd[tx][ty])-97].popleft())
                    else:
                        q.append((tx, ty))
                        if bd[tx][ty] == '$':
                            res += 1
        print(res)


if __name__ == '__main__':
    solve()
