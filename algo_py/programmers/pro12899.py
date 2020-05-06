def solution(n):
    tmp = ''
    while 1 <= n:
        trash = n % 3
        tmp = "412"[trash] + tmp
        n = n//3
        if trash == 0:
            n -= 1
    return tmp


solution(10)
