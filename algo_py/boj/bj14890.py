def row_solve(arr):
    global cnt
    chk = [[False] * n for _ in range(n)]
    for i in range(n):
        j = 0
        go_flag = True
        while j < n - 1:
            if arr[i][j] == arr[i][j + 1]:
                j += 1
                continue
            elif arr[i][j] - arr[i][j + 1] == 1:  # 높->낮
                if arr[i][j + 1:j+1+L].count(arr[i][j+1]) == L:
                    chk[i][j + 1:j + 1 + L] = [True] * L
                    j = j + L
                    continue
                else:
                    go_flag = False
                    break
            elif arr[i][j] - arr[i][j + 1] == -1:  # 낮->높
                if arr[i][j+1 - L:j+1].count(arr[i][j]) == L and True not in chk[i][j+1 - L:j+1]:
                    chk[i][j+1 - L:j+1] = [True] * L
                    j += 1
                    continue
                else:
                    go_flag = False
                    break
            else:
                go_flag = False
                break

        if go_flag:
            cnt += 1


n, L = map(int, input().split())
map_data = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
row_solve(map_data)
row_solve(list(zip(*map_data)))
print(cnt)
