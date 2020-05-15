alpha = [0 for _ in range(26)]
n = int(input())
string = input().rstrip()
length = len(string)
l = r = cnt = res = 0
while l < length:
    while r < length:
        if cnt > n:
            break
        if alpha[ord(string[r])-ord('a')] == 0:
            alpha[ord(string[r])-ord('a')] += 1
            r += 1
            cnt += 1
            if cnt > n:
                break
        else:
            alpha[ord(string[r])-ord('a')] += 1
            r += 1
        res = max(res, r-l)
    while True:
        alpha[ord(string[l])-ord('a')] -= 1
        if alpha[ord(string[l])-ord('a')] <= 0:
            cnt -= 1
            l += 1
            if cnt <= n:
                break
        else:
            l += 1
print(res)
