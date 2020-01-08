import sys
input = sys.stdin.readline

k, n = map(int, input().split())
line = sorted([int(input()) for _ in range(k)])

left = 1
right = line[-1]
mv = 0

while left <= right:
    mid = (left+right)//2
    res = 0
    for l in line:
        res += l//mid
    if res >= n:
        left = mid+1
        if mid>mv:
            mv = mid
    else :
        right = mid-1
print(mv)
