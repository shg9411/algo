from collections import deque
n, k = map(int, input().split())
visited = [[False, 0] for _ in range(100001)]
here = deque()
here.append(n)
visited[n][0] = True
time = 0
if n == k:
    print(0)
    print(n)
    exit()

while 1:
    time += 1
    for _ in range(len(here)):
        tmp = here.popleft()
        pmx = [tmp+1, tmp-1, tmp*2]
        for num in pmx:
            if 0 <= num <= 100000 and not visited[num][0]:
                visited[num][0] = True
                visited[num][1] = tmp
                here.append(num)
            if num == k:
                print(time)
                res = [num]
                while 1:
                    res.append(visited[res[-1]][1])
                    if res[-1] == n:
                        print(' '.join(map(str, res[::-1])))
                        exit()
