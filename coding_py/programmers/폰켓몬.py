def solution(nums):
    pl = len(nums)//2
    tmp = set(nums)
    if pl>=len(tmp):
        return len(tmp)
    return pl