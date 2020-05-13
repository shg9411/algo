from collections import deque
N, T, G = map(int, input().split())
visited = [False for _ in range(100000)]
if N == G:
    print(0)
    exit()


def B(num):
    if num >= 50000 or num == 0:
        return num
    num *= 2
    length = len(str(num))-1
    return num-(10**length)


pop = False
q = deque([N])
visited[N] = True
cnt = 0
while q:
    cnt += 1
    for _ in range(len(q)):
        tmp = q.popleft()
        if tmp+1 < 100000 and not visited[tmp+1]:
            if tmp+1 == G:
                pop = True
                break
            q.append(tmp+1)
            visited[tmp+1] = True
        tmpB = B(tmp)
        if not visited[tmpB]:
            if tmpB == G:
                pop = True
                break
            q.append(tmpB)
            visited[tmpB] = True
    if pop:
        print(cnt)
        exit()
    if T == cnt:
        break
print("ANG")
