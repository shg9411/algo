from collections import deque


def solve(n, k):
    time = [-1 for _ in range(100001)]
    time[n] = 0
    q = deque([n])
    while q:
        tmp = q.popleft()
        if tmp == k:
            break
        if tmp*2 < 100001 and time[tmp*2] == -1:
            time[tmp*2] = tmp
            q.append(tmp*2)
        if tmp+1 < 100001 and time[tmp+1] == -1:
            time[tmp+1] = tmp
            q.append(tmp+1)
        if tmp-1 > -1 and time[tmp-1] == -1:
            time[tmp-1] = tmp
            q.append(tmp-1)
    tmp = [k]
    while tmp[-1] != n:
        tmp.append(time[tmp[-1]])
    print(len(tmp)-1)
    print(' '.join(map(str, tmp[::-1])))


if __name__ == '__main__':
    n, k = map(int, input().split())
    if k < n:
        print(n-k)
        print(' '.join(map(str, [i for i in range(n, k-1, -1)])))
    else:
        solve(n, k)
