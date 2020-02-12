import collections
f,s,g,u,d=map(int,input().split())
queue=collections.deque()
visited=[0 for _ in range(1000002)]


def bfs(now):
    if s==g:
        print(0)
        return

    if g>s:
        if u == 0:
            print('use the stairs')
            return
        if u>=f:
            print('use the stairs')
            return

    if g<s:
        if d == 0:
            print('use the stairs')
            return

        if d>=f:
            print('use the stairs')
            return

    if d>=f or u>=f:
        print('use the stairs')
        return

    queue.append(now)
    cnt=0
    while queue:
        cnt+=1
        for _ in range(len(queue)):
            v = queue.popleft()
            #print(cnt,v,g)
            if v==g:
                print(cnt-1)
                return

            if v+u<=f:
                if not visited[v+u]:
                    queue.append(v+u)
                    visited[v + u]=1
            if v-d>=1:
                if not visited[v-d]:
                    queue.append(v-d)
                    visited[v -d]=1

        #print(queue)

bfs(s)