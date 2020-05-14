import sys
from itertools import islice
from collections import deque
input = sys.stdin.readline
W = input().rstrip()
S = input().rstrip()
N = int(input())
i = 0
j = len(S)-1
length = len(W)
lq = []
rq = deque([])
many = 0
cnt = 0
for _ in range(N):
    cmd = input().rstrip()
    if cmd == 'L':
        while i <= j:
            if ''.join(lq[-length:]) == W:
                for _ in range(length):
                    lq.pop()
                cnt += 1
                break
            lq.append(S[i])
            i += 1
    else:
        while i <= j:
            if len(rq) >= length:
                if ''.join(islice(rq, 0, length)) == W:
                    for _ in range(length):
                        rq.popleft()
                    cnt += 1
                    break
            rq.appendleft(S[j])
            j -= 1
    if i > j:
        break
    many += 1
if many < N:
    for _ in sys.stdin:
        continue
    tmp = ''.join(lq+list(rq))
    stack = []
    bomb = list(W)
    for char in tmp:
        stack.append(char)
        if many < N:
            if char == bomb[-1]:
                if stack[-length:] == bomb:
                    for _ in range(length):
                        stack.pop()
                    many += 1
                    cnt += 1
    tmp = ''.join(stack)
else:
    tmp = ''.join(lq)
    tmp += S[i:j+1]
    tmp += ''.join(rq)
print(cnt)
print(tmp)
print('Perfect!' if W not in tmp else 'You Lose!')
