import bisect
from collections import deque


class st:
    def __init__(self):
        self.size = 0
        self.left = []
        self.right = []


N, K = map(int, input().split())
dp = [1 for _ in range(N+1)]
arr = [1]
tmp = [st() for _ in range(N+1)]
large = 1
q = deque()
arr += list(map(int, input().split()))
for i in range(2, N+1):
    for j in range(1, i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)
    for j in range(1, i):
        if arr[j] < arr[i] and dp[j]+1 == dp[i]:
            tmp[arr[i]].left.append(arr[j])
            tmp[arr[j]].right.append(arr[i])
        large = max(large, dp[i])
check = [0 for _ in range(N+1)]
for i in range(1, N+1):
    if large == dp[i]:
        tmp[arr[i]].size += 1
        q.append(arr[i])

l = large
while large > 1:
    large -= 1
    for i in range(len(q)):
        num = q.popleft()
        for j in range(len(tmp[num].left)):
            number = tmp[num].left[j]
            tmp[number].size += tmp[num].size
            if check[number] == 0:
                check[number] = 1
                q.append(number)
sum = 0
while q:
    val = q.popleft()
    tmp[0].right.append(val)
    sum += tmp[val].size
if sum < K:
    print(-1)
else:
    start = 0
    while large <= l:
        large += 1
        tmp[start].right.sort()
        for i in range(len(tmp[start].right)):
            num = tmp[start].right[i]
            if K > tmp[num].size:
                K -= tmp[num].size
            else:
                print(num, end=' ')
                start = num
                break
