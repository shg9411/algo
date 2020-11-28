from collections import Counter


class Solution:
    def solution(self, s, n):
        global ans
        c = Counter(s)

        def dfs(idx, cnt):
            global ans
            if cnt == n:
                v = sorted(c.values())
                for num in v:
                    if num > 0:
                        break
                ans = min(v[-1]-num, ans)
                return
            for i in range(idx, len(s)):
                c[s[i]] -= 1
                dfs(i+1, cnt+1)
                c[s[i]] += 1
        ans = len(s)
        dfs(0, 0)
        return ans


s = "abcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefga"
n = 25
print(Solution().solution(s, n))
#TLE