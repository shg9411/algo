import heapq


class Solution:
    def solution(self, goods):
        heapq.heapify(goods)
        ans = 0
        tmp = 0
        while goods:
            tmp += heapq.heappop(goods)
            if tmp >= 50:
                ans += tmp-10
                tmp = 0
        if tmp:
            ans+=tmp

        return ans


print(Solution().solution([5,31,15]))
