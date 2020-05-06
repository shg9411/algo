import sys
from collections import deque
input = sys.stdin.readline

gear = [deque(list(input().rstrip())) for _ in range(4)]

k = int(input())

for _ in range(k):
    num, direct = map(int, input().split())
    move = [0]*4
    move[num-1] = direct
    for i in range(num-2, -1, -1):
        if gear[i][2] == gear[i+1][6]:
            move[i] = 0
        else:
            move[i] = -move[i+1]
    for i in range(num, 4):
        if gear[i][6] == gear[i-1][2]:
            move[i] = 0
        else:
            move[i] = -move[i-1]
    for i in range(num-2, 0, -1):
        if move[i] == 0:
            move[i-1] = 0
    for i in range(num, 3):
        if move[i] == 0:
            move[i+1] = 0
    for i in range(4):
        gear[i].rotate(move[i])


res = 0
for i in range(4):
    if gear[i][0] == '1':
        res += pow(2, i)
print(res)
