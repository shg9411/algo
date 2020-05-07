import sys
n = 10000000
sorted_nums = list()
nums = [0]*10001
_sum = [0]
for i in range(n):
    nums[i % 10000] += 1
for i in range(1, 10001):
    _sum.append(_sum[i-1]+nums[i])
    if _sum[i-1]+nums[i] == n:
        break
for i in range(len(_sum)-1, 0, -1):
    for j in range(_sum[i]-_sum[i-1]):
        sorted_nums.append(i)
        n -= 1
sorted_nums.reverse()
for i in range(len(sorted_nums)):
    # print(sorted_nums[i])
    pass
print(len(sorted_nums))
print(sys.getsizeof(sorted_nums))
