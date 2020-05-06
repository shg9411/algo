import sys
input = sys.stdin.readline


def dfs(i, j, cnt):
    global result
    for k in range(4):
        i_tem = i + dx[k]
        j_tem = j + dy[k]
        if -1 < i_tem < R and -1 < j_tem < C and not bank[ord(data[i_tem][j_tem])-65]:
            bank[ord(data[i_tem][j_tem])-65] = True
            result = max(result, cnt+1)
            dfs(i_tem, j_tem, cnt+1)
            bank[ord(data[i_tem][j_tem])-65] = False


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


R, C = map(int, input().split())
data = [input().rstrip() for _ in range(R)]
result = 1
bank = [False for _ in range(26)]
bank[ord(data[0][0])-65] = True
dfs(0, 0, 1)
print(result)
