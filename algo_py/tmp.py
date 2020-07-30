graph = {0: [1, 2], 1: [0, 2], 2: [1, 0], 3: [4, 5], 4: [3, 5], 5: [4, 3]}

def dfs(graph, start) :
    vis = []
    stack = [start]
    
    while stack :
        n = stack.pop()
        if n not in vis :
            vis.append(n)
            print(n)
            G = graph[n]
            V = list(set(vis))
            for item in G :
                if V.count(item) >= 1:
                    G.remove(item)
            stack.append(G)
    return vis

dfs(graph, 3)