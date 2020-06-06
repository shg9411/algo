import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    chk=[list(map(int, input().split()))]
    cnt=K
    for _ in range(K-1):
        X,Y=map(int,input().split())
        for [r,c] in chk:
            if (r,c)==(X-1,Y) or (r,c)==(X+1,Y) or (r,c)==(X,Y-1) or (r,c)==(X,Y+1):
                cnt-=1
                break
        chk.append([X,Y])
    print(cnt)