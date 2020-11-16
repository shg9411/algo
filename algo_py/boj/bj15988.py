import sys
def solve():
    c=[0,1,2,4]
    MOD=10**9+9
    tmp=3
    t=int(input())
    q=list(map(int,sys.stdin.read().split()))
    m=max(q)
    for i in range(4,m+1):
        tmp=(tmp-c[-4]+c[-1])%MOD
        c.append(tmp)
    r=[]
    for num in q:
        r.append(c[num])
    print('\n'.join(map(str,r)))
if __name__=='__main__':
    solve()