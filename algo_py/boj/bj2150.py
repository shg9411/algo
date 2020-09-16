import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
sn = cnt = 0

def dfs(u):
    global sn
    global cnt
    cnt+=1
    dfsn[u] = cnt
    stack.append(u)

    res = dfsn[u]
    for v in adj[u]:
        if dfsn[v]==0:
            res = min(res,dfs(v))
        elif not finished[v]:
            res = min(res,dfsn[v])
    
    if res == dfsn[u]:
        tmpScc = []
        while 1:
            tmp = stack.pop()
            tmpScc.append(tmp)
            finished[tmp] = True
            sccn[tmp] = sn
            if tmp==u:
                break
        tmpScc.sort()
        ans.append(tmpScc)
        sn+=1
    return res


if __name__ == '__main__':
    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]
    dfsn = [0 for _ in range(V+1)]
    sccn = [0 for _ in range(V+1)]
    finished = [False for _ in range(V+1)]
    ans = []
    stack = []
    for _ in range(E):
        u,v = map(int,input().split())
        adj[u].append(v)
    for i in range(1,V+1):
        if dfsn[i]==0:
            dfs(i)
    ans.sort()
    print(sn)
    for scc in ans:
        sys.stdout.write(' '.join(map(str,scc))+' -1\n')