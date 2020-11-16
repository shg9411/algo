import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
t = int(input())

def solve():
    def find(x):
        if x == parent[x]:
            return x
        parent[x] = find(parent[x])
        return parent[x]
    
    
    def union(x, y):
        x = find(x)
        y = find(y)
        if x != y:
            parent[x] = y
            num[y] += num[x]
            num[x] = 1
        return num[y]
    
    
    res = []
    for _ in range(t):
        f = int(input())
        cnt = 1
        parent = [i for i in range(f*2+1)]
        num = [1]*(f*2+1)
        freind = dict()
        for _ in range(f):
            a, b = input().split()
            if a not in freind:
                freind[a] = cnt
                cnt += 1
            if b not in freind:
                freind[b] = cnt
                cnt += 1
            res.append(union(freind[a], freind[b]))
    print('\n'.join(map(str,res)))

if __name__=='__main__':
    solve()