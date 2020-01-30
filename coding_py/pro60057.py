def solution(s):
    def compress(size):
        res = 0
        before, count = s[:size], 1
        for i in range(size, len(s), size):
            word = s[i:i+size]
            if word == before:
                count += 1
            else:
                if count > 1:
                    res += len(str(count))
                res += size
                before, count = word, 1
        if count > 1:
            res += len(str(count))
        res += len(before)
        return res

    ans = len(s)
    for size in range(1, ans+2//2):
        ans = min(ans, compress(size))
    return ans