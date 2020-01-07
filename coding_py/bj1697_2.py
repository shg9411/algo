from collections import deque
n, k = map(int, input().split())
visited = [False]*100001
here = deque()
here.append(n)
visited[n] = True
time = 0
if n == k:
    print(0)
    exit()

while 1:
    time += 1
    for _ in range(len(here)):
        tmp = here.popleft()
        pmx = [tmp+1, tmp-1, tmp*2]
        for num in pmx:
            if 0 <= num <= 100000 and not visited[num]:
                visited[num] = True
                here.append(num)
            if num==k:
                print(time)
                exit()
