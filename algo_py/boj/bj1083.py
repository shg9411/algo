N = int(input())
arr = list(map(int, input().split()))
S = int(input())
tmp = 0
tmpIdx = tmpVal = 0
while S and tmp < N:
    tmpIdx = tmp
    tmpVal = arr[tmpIdx]
    for i in range(tmp, N):
        if arr[i] > tmpVal and i-tmp <= S:
            tmpIdx = i
            tmpVal = arr[i]
    arr.pop(tmpIdx)
    arr.insert(tmp, tmpVal)
    S -= tmpIdx-tmp
    tmp += 1
print(*arr)
