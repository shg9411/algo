a, b = map(int, input().split())


def cnt(num):
    num += 1
    tmp = num
    t = 1
    res = 0
    while tmp:
        if num & t:
            res += num % t+(num-num % (t*2))//2
        else:
            res += (num-num % t)//2
        t <<= 1
        tmp >>= 1
    return res


print(cnt(b)-cnt(a-1))
