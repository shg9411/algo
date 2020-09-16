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
            x = t >> 1
            if not t % 2 and dist[x] > dist[t]:
                dist[x] = dist[t]
                q.appendleft(x)
            if t >= 1 and dist[t-1] > dist[t]+1:
                dist[t-1] = dist[t]+1
                q.append(t-1)
            if t+1 < MAX and dist[t+1] > dist[t]+1:
                dist[t+1] = dist[t]+1
                q.append(t+1)
        print(dist[n])


if __name__ == "__main__":
    solve()