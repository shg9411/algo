from collections import deque


def solve():
    n, k = map(int, input().split())
    if k <= n:
        print(n-k)
    else:
        MAX = 100001
        dist = [MAX for _ in range(MAX)]
        dist[k] = 0
        q = deque([k])
        while q:
            t = q.popleft()
            if t == n:
                break
            c = dist[t]
            x = t >> 1
            if not t % 2 and dist[x] > c:
                dist[x] = c
                q.appendleft(x)
            c += 1
            x = t-1
            if x >= 0 and dist[x] > c:
                dist[x] = c
                q.append(x)
            x = t+1
            if x < MAX and dist[x] > c:
                dist[x] = c
                q.append(x)
        print(dist[n])


if __name__ == "__main__":
    solve()
