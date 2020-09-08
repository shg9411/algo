# 랜선 자르기

k, m = list(map(int, input().split()))
array = []
for _ in range(k):
    array.append(int(input()))

start = 1
end = max(array)

result = 0
while (start <= end):
    total = 0
    mid = (start+end) // 2
    for x in array:
        if x > mid:
            total += x//mid
    if total < m:  # 랜선이 필요량보다 적은 경우 (mid 를 작게 해서 잘게 잘라야함)
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)
