import heapq


class Solution:
    def solution(self, votes):
        if len(votes) == 1:
            return 0
        q = []
        for vote in votes[1:]:
            heapq.heappush(q, -vote)
        candi = votes[0]
        while -q[0] >= candi:
            heapq.heappush(q, heapq.heappop(q)+1)
            candi += 1
        return candi-votes[0]


print(Solution().solution([5,10,7,3,8]))
