import sys
input = sys.stdin.readline
def calculate(ans, nums):
    k = len(nums)
    if k == 1:
        ans_value = nums[0]
    elif k == 2:
        ans_value = max(min(nums)*2, max(nums))
    elif k == 3:
        if min(nums) == nums[1]:
            ans_value = max(min(nums)*3, max(nums))
        else:
            nums.sort()
            ans_value = max(nums[0]*3, nums[1]*2, nums[2])
    else:
        min_value = min(nums)
        start = 0
        array = [min_value * k]
        for i in range(k):
            if nums[i] == min_value and start != i:
                array.append(calculate(ans, nums[start:i]))
                start = i+1
        array.append(calculate(ans, nums[start:k]))
        ans_value = max(array)
    if ans_value > ans:
        ans = ans_value
    return ans
while True:
    N = list(map(int, input().split()))
    if N[0] == 0:
        break
    print(0, calculate(N[1:]))