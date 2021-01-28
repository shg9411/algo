
def antArray(t):
    origin = '1'
    print(origin)
    for _ in range(t-1):
        origin += ' '
        tmp = origin[0]
        nxt = ''
        cnt = 1
        for idx, char in enumerate(origin[1:]):
            if char == tmp:
                cnt += 1
            else:
                nxt += tmp
                nxt += str(cnt)
                tmp = char
                cnt = 1
        origin = nxt
        print(origin)


antArray(int(input("몇번째 수열까지 구하시겠습니까?\n")))
