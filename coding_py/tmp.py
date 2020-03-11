nx = [0, 1]
ny = [1, 0]

arr = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4,
                                                                                                                                            5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]


def dfs(x, y, res):
    if x == len(arr)-1 and y == len(arr[0])-1:
        print(res)
        return

    for i in range(2):
        tmpx = x+nx[i]
        tmpy = y+ny[i]
        if tmpx < len(arr) and tmpy < len(arr[0]):
            dfs(tmpx, tmpy, res+str(arr[tmpx][tmpy])+' ')


dfs(0, 0, res=str(arr[0][0])+' ')
