from collections import deque
rc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
shf = [-12, 12, -4, 4]
puzzle = ans = 0

for n in range(1, 9):
    ans <<= 4
    ans += n
ans <<= 4

for _ in range(3):
    line = map(int, input().split())
    for num in line:
        puzzle <<= 4
        puzzle += num

check = set()
check.add(puzzle)
q = deque([puzzle])
res = 0

while q:
    size = len(q)
    for _ in range(size):
        tmp = q.popleft()
        if tmp == ans:
            print(res)
            exit()
        where = 0
        while tmp & (15 << where*4):
            where += 1
        r, c = divmod(where, 3)
        for (x, y), shift in zip(rc, shf):
            nr = r+x
            nc = c+y
            if 0 <= nr < 3 and 0 <= nc < 3:
                temp = tmp & (15 << (nr*3+nc)*4)
                nxt = tmp-temp
                if shift > 0:
                    temp <<= shift
                else:
                    temp >>= -shift
                nxt += temp
                if nxt not in check:
                    check.add(nxt)
                    q.append(nxt)
    res += 1

print(-1)
