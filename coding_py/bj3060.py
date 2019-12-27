import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    food = int(input())
    pig = list(map(int, input().split()))
    day = 1
    while sum(pig) <= food:
        day += 1
        pig2 = [0]*6
        for i in range(6):
            pig2[i] = pig[i] + pig[(i+1) % 6] + pig[(i-1) % 6] + pig[(i+3) % 6]
        pig = pig2
    print(day)
