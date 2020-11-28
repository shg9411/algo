
class Solution:
    def solution(self, page, broken):
        a = str(page)
        page = int(a)
        d = set('0123456789')
        if broken:
            d = d.difference(str(broken))

        d = sorted(d)
        ans = abs(page-100)
        if d:
            l = len(a)
            if page > 9:
                k1 = int(d[-1] * (l-1))
                ans = min(ans, abs(k1 - page) + l-1)
            k1 = int(
                d[1]+'0'*l) if d[0] == '0' and len(d) > 1 else int(d[0] * (l+1))
            ans = min(ans, abs(k1 - page) + l+1)
            e = [int(i) for i in d]
            f = e.copy()
            for _ in range(l - 1):
                f = [10*i + j for i in f for j in e]
            ans = l + min(ans-l, *(abs(i-page) for i in f))
        return (ans)


print(Solution().solution(99999, [0, 2, 3, 4, 5, 6, 7, 8, 9]))
