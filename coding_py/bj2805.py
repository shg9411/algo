import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = sorted(list(map(int, input().split())))
left = 1
right = tree[-1]
mv = 0

while left <= right:
    mid = (left+right)//2
    res = 0
    for t in tree:
        if t > mid:
            res+=t-mid
    if res>=m:
        left = mid+1
        mv = max(mv,mid)
    else:
        right = mid-1
print(mv)