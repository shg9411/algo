# 핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.
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


s = Solution()
goods = [5,31,15]
print(s.solution(goods))
