import sys
import collections
sys.setrecursionlimit(100000)
res = []
def MakeGraph(graph, E):
    for _ in range(E):
        a, b =  map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    return graph

def DFS(vert, group, check):
    vis[vert]=group
    if not graph[vert]:
        return 0
    for i in graph[vert]:
        if vis[i] == vis[vert]:
            return 1
        elif vis[i] == False:
            check=DFS(i, -group, check)+check
            if check >0:
                break
    return check
for _ in range(int(sys.stdin.readline())):
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V+1)]
    graph = MakeGraph(graph, E)
    vis = [False]*(V+1)
    check =0
    for i in range(1, V+1):
        if vis[i]==False:
            if DFS(i, 1, check):
                check =1
                break
    res.append('NO' if check else 'YES')
print(res)