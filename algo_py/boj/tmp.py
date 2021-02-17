import sys
input = sys.stdin.readline
t = int(input())
inp = [[] for _ in range(10000)]
ans = [[] for _ in range(t)]
update = [0]*10000
dist = [0]*10001
path = [0]*10000
chk = [0]*10000
que = [0]*10010
chr = ['D', 'S', 'L', 'R']
for i in range(t):
    a, b = map(int, input().split())
    inp[a].append((b, i))

for i in range(10000):
    if not inp[i]:
        continue
    n = 0
    for j, k in inp[i]:
        if not chk[j]:
            n += 1
            chk[j] = 1
    dist[i] = 0
    path[i] = 0
    update[i] = i+1
    a = b = 0
    que[a] = i
    a += 1
    while n:
        no = que[b]
        b += 1
        nxt = [no << 1, no-1 if no else 9999, no %
               1000*10+no//1000, no//10+no % 10*1000]
        if nxt[0] >= 10000:
            nxt[0] -= 10000
        for j in range(4):
            if update[nxt[j]] != i+1:
                update[nxt[j]] = i+1
                if chk[nxt[j]]:
                    n -= 1
                    chk[nxt[j]] = 0
                dist[nxt[j]] = dist[no]+1
                path[nxt[j]] = no*10+j+1
                que[a] = nxt[j]
                a += 1
    for m, idx in inp[i]:
        while path[m]:
            ans[idx].append(chr[path[m] % 10-1])
            m = path[m]//10
for r in ans:
    print(''.join(r[::-1]))
