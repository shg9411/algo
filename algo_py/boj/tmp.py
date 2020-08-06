def dfs(idx, cnt):
    global maxv

    if maxv == N:  # max이므로 더이상 순회할 필요가 없음
        return

    if cnt == K-5:
        # True인 애들을 통해서
        res = 0
        for j in range(N):
            flag = 0
            for z in range(len(texts[j])):
                if D[ord(texts[j][z])-97] == True:
                    pass
                else:
                    flag = 1
                    break
            if flag == 0:
                res += 1
        if res > maxv:
            maxv = res
        return

    for i in range(idx, len(l)):
        if D[ord(l[i])-97] == False:
            cnt += 1
            D[ord(l[i]) - 97] = True
            dfs(i, cnt)
            cnt -= 1
            D[ord(l[i]) - 97] = False


if __name__ == '__main__':
    N, K = map(int, input().split())

    if K < 5:
        print(0)

    else:
        D = [False]*26
        D[0], D[2], D[8], D[13], D[19] = True, True, True, True, True
        l = []
        texts = []
        maxv = 0

        for _ in range(N):
            text = input()
            text = text[4:len(text)-4]
            for i in range(len(text)):
                if D[ord(text[i])-97] == False and text[i] not in l:  # 여기서 false는 5개 빼려고 한 것
                    l.append(text[i])
            texts.append(text)

        dfs(0, cnt=0)

        print(maxv)
